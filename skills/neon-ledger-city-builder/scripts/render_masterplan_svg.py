#!/usr/bin/env python3
"""Render an inspectable top-down SVG from canonical zone JSON (stdlib only)."""
import argparse
import html
import json
from pathlib import Path


def esc(value):
    return html.escape(str(value), quote=True)


def render(zone):
    bounds = zone['bounds']
    w, h = float(bounds['width_x']), float(bounds['length_z'])
    unit = min(12, 1000 / max(w, h))
    pad, sidebar = 70, 260
    W, H = int(w * unit + 2 * pad + sidebar), int(h * unit + 2 * pad + 45)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Masterplan {esc(zone["name"])}">',
             '<style>text{font-family:Arial,sans-serif;fill:#192536}.small{font-size:11px}.label{font-size:12px;font-weight:bold}.tiny{font-size:9px}</style>',
             '<rect width="100%" height="100%" fill="#f7f9fc"/>',
             f'<text x="{pad}" y="27" font-size="20" font-weight="bold">{esc(zone["name"])} — {esc(zone["zone_id"])} · MASTERPLAN</text>',
             f'<text x="{pad}" y="44" class="small">Échelle : 1 unité JSON = 1 m · Origine globale X={zone["origin_global"]["x"]}, Z={zone["origin_global"]["z"]} · Vue du dessus</text>']
    def sx(x): return pad + x * unit
    def sy(z): return pad + (h - z) * unit
    def rect(r, color, stroke, opacity=1):
        return f'<rect x="{sx(r["min_x"]):.1f}" y="{sy(r["max_z"]):.1f}" width="{(r["max_x"]-r["min_x"])*unit:.1f}" height="{(r["max_z"]-r["min_z"])*unit:.1f}" fill="{color}" stroke="{stroke}" stroke-width="1.5" opacity="{opacity}"/>'
    parts.append(f'<rect x="{pad}" y="{pad}" width="{w*unit:.1f}" height="{h*unit:.1f}" fill="#f1eddf" stroke="#25364f" stroke-width="2"/>')
    step = 5 if max(w, h) <= 160 else (10 if max(w, h) <= 400 else 25)
    for x in range(0, int(w)+1, step):
        parts.append(f'<path d="M {sx(x):.1f} {sy(0):.1f} V {sy(h):.1f}" stroke="#c8d0d9" stroke-width="0.5"/>')
        parts.append(f'<text x="{sx(x):.1f}" y="{sy(0)+15:.1f}" text-anchor="middle" class="tiny">{x}</text>')
    for z in range(0, int(h)+1, step):
        parts.append(f'<path d="M {sx(0):.1f} {sy(z):.1f} H {sx(w):.1f}" stroke="#c8d0d9" stroke-width="0.5"/>')
        parts.append(f'<text x="{sx(0)-8:.1f}" y="{sy(z)+3:.1f}" text-anchor="end" class="tiny">{z}</text>')
    for road in zone.get('roads', []):
        for r in road['segments']:
            parts.append(rect(r, '#d7e7ee', '#769ead'))
    for b in zone.get('buildings', []):
        parts.append(rect(b['reserved_footprint'], 'none', '#a5a58e'))
        parts.append(rect(b['built_footprint'], '#768da3', '#374e63'))
        r = b['built_footprint']
        x, z = (r['min_x']+r['max_x'])/2, (r['min_z']+r['max_z'])/2
        parts.append(f'<text x="{sx(x):.1f}" y="{sy(z):.1f}" text-anchor="middle" fill="#ffffff" style="fill:#fff;font:bold {max(8,min(12,unit*1.0)):.0f}px Arial">{esc(b["id"])}</text>')
    for route in zone.get('routes', []):
        pts = ' '.join(f'{sx(p["x"]):.1f},{sy(p["z"]):.1f}' for p in route['points'])
        parts.append(f'<polyline points="{pts}" stroke="#ee7d2d" fill="none" stroke-width="2.5" stroke-dasharray="7 4"/>')
    for c in zone.get('connectors', []):
        p = c['position']
        parts.append(f'<circle cx="{sx(p["x"]):.1f}" cy="{sy(p["z"]):.1f}" r="5" fill="#278b6a" stroke="white" stroke-width="1.5"/>')
    for poi in zone.get('pois', []):
        p = poi['position']
        parts.append(f'<circle cx="{sx(p["x"]):.1f}" cy="{sy(p["z"]):.1f}" r="4" fill="#c33b69" stroke="white"/>')
        parts.append(f'<text x="{sx(p["x"])+7:.1f}" y="{sy(p["z"])-5:.1f}" class="tiny">{esc(poi["id"])}</text>')
    side = pad + w * unit + 25
    parts.extend([f'<text x="{side:.1f}" y="75" class="label">N ↑  /  Z ↑</text>',
                  f'<text x="{side:.1f}" y="101" class="label">BÂTIMENTS</text>'])
    pos = 120
    for b in zone.get('buildings', []):
        parts.append(f'<text x="{side:.1f}" y="{pos}" class="small">{esc(b["id"])} · {esc(b["name"][:26])}</text>')
        parts.append(f'<text x="{side:.1f}" y="{pos+13}" class="tiny">{esc(b["height_m"])} m · {esc(b["floors"])} niveaux · {esc(b["function"][:27])}</text>')
        pos += 32
    pos += 12
    parts.append(f'<text x="{side:.1f}" y="{pos}" class="label">VOIRIES</text>')
    for road in zone.get('roads', []):
        pos += 18
        parts.append(f'<text x="{side:.1f}" y="{pos}" class="small">{esc(road["id"])} · {esc(road["name"][:31])}</text>')
    pos += 30
    parts.append(f'<text x="{side:.1f}" y="{pos}" class="label">LÉGENDE</text>')
    for label, color in [('Emprise bâtie', '#768da3'),('Voirie réservée', '#d7e7ee'),('Connecteur', '#278b6a'),('Point d’intérêt', '#c33b69'),('Parcours (tirets)', '#ee7d2d')]:
        pos += 19
        parts.append(f'<rect x="{side:.1f}" y="{pos-10}" width="12" height="12" fill="{color}" stroke="#637283"/><text x="{side+20:.1f}" y="{pos}" class="small">{label}</text>')
    scale = min(10, int(w))
    parts.append(f'<path d="M {pad} {H-18} h {scale*unit:.1f}" stroke="#182c40" stroke-width="4"/><text x="{pad+scale*unit/2:.1f}" y="{H-26}" text-anchor="middle" class="small">{scale} m</text>')
    parts.append('</svg>')
    return '\n'.join(parts) + '\n'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('masterplan')
    p.add_argument('-o','--output', required=True)
    args = p.parse_args()
    with open(args.masterplan, encoding='utf-8') as file:
        zone = json.load(file)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(zone), encoding='utf-8')
    print(f'Wrote {output}')


if __name__ == '__main__':
    main()
