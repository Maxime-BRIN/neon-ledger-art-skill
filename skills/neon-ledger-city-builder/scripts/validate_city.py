#!/usr/bin/env python3
"""Validate a Neon Ledger city registry and its masterplans (stdlib only).

Checks deliberately do not certify Godot navigation, aesthetics, approvals or licences.
"""
import json
import math
import pathlib
import sys
from collections import defaultdict

EPS = 1e-6


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def fail(errors, where, message):
    errors.append(f"{where}: {message}")


def finite(n):
    return isinstance(n, (float, int)) and not isinstance(n, bool) and math.isfinite(n)


def check_point(point, where, errors):
    if not isinstance(point, dict) or not all(finite(point.get(k)) for k in ("x", "z")):
        fail(errors, where, "invalid point; requires finite x and z")
        return False
    return True


def check_rect(rect, where, bounds, errors):
    if not isinstance(rect, dict) or not all(finite(rect.get(k)) for k in ("min_x", "max_x", "min_z", "max_z")):
        fail(errors, where, "invalid rectangular footprint")
        return False
    x1, x2, z1, z2 = (rect[k] for k in ("min_x", "max_x", "min_z", "max_z"))
    if x1 >= x2 or z1 >= z2:
        fail(errors, where, "min must be strictly less than max")
        return False
    if x1 < -EPS or z1 < -EPS or x2 > bounds[0] + EPS or z2 > bounds[1] + EPS:
        fail(errors, where, "footprint outside zone bounds")
    return True


def overlap(a, b):
    return min(a["max_x"], b["max_x"]) - max(a["min_x"], b["min_x"]) > EPS and min(a["max_z"], b["max_z"]) - max(a["min_z"], b["min_z"]) > EPS


def contains(outer, inner):
    return all((outer["min_x"] <= inner["min_x"] + EPS, outer["max_x"] + EPS >= inner["max_x"], outer["min_z"] <= inner["min_z"] + EPS, outer["max_z"] + EPS >= inner["max_z"]))


def point_in_rect(point, rect):
    return rect["min_x"] - EPS <= point["x"] <= rect["max_x"] + EPS and rect["min_z"] - EPS <= point["z"] <= rect["max_z"] + EPS


def segment_covered(p, q, rectangles):
    """Exact for straight segments within a union of axis-aligned rectangles.

    Computes parameter coverage on t in [0,1], not naive point sampling.
    """
    intervals = []
    for r in rectangles:
        lo, hi = 0., 1.
        for key, a, b in (("x", r["min_x"], r["max_x"]), ("z", r["min_z"], r["max_z"])):
            start, delta = p[key], q[key] - p[key]
            if abs(delta) < EPS:
                if start < a - EPS or start > b + EPS:
                    lo, hi = 1., 0.
                    break
            else:
                t1, t2 = (a - start) / delta, (b - start) / delta
                lo, hi = max(lo, min(t1, t2)), min(hi, max(t1, t2))
        if hi + EPS >= lo:
            intervals.append((max(0., lo), min(1., hi)))
    intervals.sort()
    covered = 0.
    for lo, hi in intervals:
        if lo > covered + EPS:
            return False
        covered = max(covered, hi)
        if covered >= 1 - EPS:
            return True
    return False


def validate_zone(zone):
    errors, warnings = [], []
    where = zone.get("zone_id", "<zone>")
    bounds = zone.get("bounds", {})
    width, length = bounds.get("width_x"), bounds.get("length_z")
    if not (finite(width) and finite(length) and width > 0 and length > 0):
        return [f"{where}: invalid zone bounds"], warnings
    if not check_point(zone.get("origin_global"), where + " origin", errors):
        return errors, warnings
    seen = set()
    built = []
    for obj_type in ("buildings", "roads", "connectors", "routes", "pois"):
        objs = zone.get(obj_type, [])
        if not isinstance(objs, list):
            fail(errors, where, f"{obj_type} must be list")
            return errors, warnings
        for obj in objs:
            oid = obj.get("id") if isinstance(obj, dict) else None
            if not isinstance(oid, str) or not oid.strip() or oid in seen:
                fail(errors, where, f"missing or duplicate object ID {oid!r}")
            seen.add(oid)
    for b in zone.get("buildings", []):
        ident = f'{where}/{b.get("id")}'
        r, f = b.get("reserved_footprint"), b.get("built_footprint")
        valid_r = check_rect(r, ident + " reserved", (width, length), errors)
        valid_f = check_rect(f, ident + " built", (width, length), errors)
        if valid_r and valid_f and not contains(r, f):
            fail(errors, ident, "built footprint not within reserved footprint")
        if not finite(b.get("height_m")) or b["height_m"] <= 0 or not isinstance(b.get("floors"), int) or b["floors"] < 1:
            fail(errors, ident, "height_m/floors invalid")
        if valid_f:
            built.append((b["id"], f))
    roads = []
    for road in zone.get("roads", []):
        for i, rect in enumerate(road.get("segments", [])):
            if check_rect(rect, f'{where}/{road.get("id")}[{i}]', (width, length), errors):
                roads.append((road["id"], rect))
    for i, (bid, rect) in enumerate(built):
        for other_id, other_rect in built[i + 1:]:
            if overlap(rect, other_rect):
                fail(errors, where, f"buildings {bid} and {other_id} overlap")
        for road_id, road_rect in roads:
            if overlap(rect, road_rect):
                fail(errors, where, f"building {bid} overlaps road {road_id}")
    rects = [r for _, r in roads]
    for c in zone.get("connectors", []):
        ident = f'{where}/{c.get("id")}'
        p = c.get("position")
        if not check_point(p, ident, errors):
            continue
        edge = c.get("edge")
        if edge not in ("north", "south", "west", "east"):
            fail(errors, ident, "invalid edge")
        else:
            correct = {"north": abs(p["z"] - length) < EPS, "south": abs(p["z"]) < EPS, "west": abs(p["x"]) < EPS, "east": abs(p["x"] - width) < EPS}[edge]
            if not correct:
                fail(errors, ident, f"connector not on {edge} boundary")
        if not finite(c.get("width_m")) or c["width_m"] <= 0:
            fail(errors, ident, "invalid connector width")
        if not any(point_in_rect(p, r) for r in rects):
            fail(errors, ident, "connector not connected to a road segment")
    for route in zone.get("routes", []):
        points = route.get("points", [])
        if len(points) < 2:
            fail(errors, where, f'route {route.get("id")} has <2 points')
            continue
        for i, p in enumerate(points):
            if not check_point(p, f'{where}/{route.get("id")}[{i}]', errors):
                break
            if not (0 - EPS <= p["x"] <= width + EPS and 0 - EPS <= p["z"] <= length + EPS):
                fail(errors, where, f'route {route.get("id")} point outside bounds')
        else:
            for p, q in zip(points, points[1:]):
                if not segment_covered(p, q, rects):
                    fail(errors, where, f'route {route.get("id")} leaves circulation reserved rectangles')
    for poi in zone.get("pois", []):
        p = poi.get("position")
        if check_point(p, f'{where}/poi {poi.get("id")}', errors) and not (0 - EPS <= p["x"] <= width + EPS and 0 - EPS <= p["z"] <= length + EPS):
            fail(errors, where, f'poi {poi.get("id")} outside zone')
    if not zone.get("roads"):
        warnings.append(f"{where}: no roads specified")
    return errors, warnings


def world_bounds(zone):
    o, b = zone["origin_global"], zone["bounds"]
    return {"min_x": o["x"], "max_x": o["x"] + b["width_x"], "min_z": o["z"], "max_z": o["z"] + b["length_z"]}


def validate_registry(path):
    registry = load(path)
    errors, warnings = [], []
    base = pathlib.Path(path).resolve().parent
    district_ids = [d.get("id") for d in registry.get("districts", [])]
    if len(district_ids) != len(set(district_ids)):
        fail(errors, "registry", "duplicate district IDs")
    zone_entries = registry.get("zones", [])
    ids = [z.get("id") for z in zone_entries]
    if len(ids) != len(set(ids)):
        fail(errors, "registry", "duplicate zone IDs")
    if set(ids + district_ids) & set(registry.get("retired_ids", [])):
        fail(errors, "registry", "reused retired ID")
    loaded = {}
    for entry in zone_entries:
        zid = entry.get("id")
        if entry.get("district_id") not in district_ids:
            fail(errors, zid, "district_id not in registry")
        rel = pathlib.Path(entry.get("masterplan", ""))
        if rel.is_absolute() or ".." in rel.parts or not str(rel):
            fail(errors, zid, "unsafe masterplan path")
            continue
        fpath = base / rel
        if not fpath.is_file():
            fail(errors, zid, f"missing masterplan {rel}")
            continue
        try:
            zone = load(fpath)
        except (ValueError, OSError) as exc:
            fail(errors, zid, f"unreadable masterplan {exc}")
            continue
        loaded[zid] = zone
        if zone.get("zone_id") != zid or zone.get("district_id") != entry.get("district_id"):
            fail(errors, zid, "registry and masterplan ID mismatch")
        a, w = validate_zone(zone)
        errors.extend(a)
        warnings.extend(w)
        if entry.get("status") == "locked" and not any(a.get("stage") == "dressing" and a.get("approved_by") not in ("agent", "AI", "") for a in entry.get("approvals", [])):
            fail(errors, zid, "locked without recorded human dressing approval")
    zones = list(loaded.items())
    for i, (aid, za) in enumerate(zones):
        for bid, zb in zones[i + 1:]:
            if overlap(world_bounds(za), world_bounds(zb)):
                fail(errors, "registry", f"world bounds overlap {aid} and {bid}")
    for aid, za in zones:
        for connector in za.get("connectors", []):
            bid = connector.get("target_zone_id")
            if bid is None:
                continue
            if bid not in loaded:
                fail(errors, aid, f"connector references missing zone {bid}")
                continue
            ax = za["origin_global"]["x"] + connector["position"]["x"]
            az = za["origin_global"]["z"] + connector["position"]["z"]
            candidates = [c for c in loaded[bid].get("connectors", []) if c.get("target_zone_id") == aid]
            if not any(abs(ax - (loaded[bid]["origin_global"]["x"] + c["position"]["x"])) <= EPS and abs(az - (loaded[bid]["origin_global"]["z"] + c["position"]["z"])) <= EPS and min(connector["width_m"], c["width_m"]) > 0 for c in candidates):
                fail(errors, aid, f"connector to {bid} has no reciprocal aligned connector")
    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_city.py <city_master_index.json | zone_masterplan.json>")
        return 2
    path = pathlib.Path(sys.argv[1])
    try:
        data = load(path)
        errors, warnings = validate_zone(data) if "zone_id" in data else validate_registry(path)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}")
        return 2
    for w in warnings:
        print("WARNING:", w)
    for e in errors:
        print("ERROR:", e)
    if errors:
        print(f"FAILED: {len(errors)} error(s)")
        return 1
    print("PASS: geometry and local registry checks passed; Godot, human approvals and licences NOT verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
