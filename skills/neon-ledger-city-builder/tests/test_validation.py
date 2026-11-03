import copy
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_city import validate_zone, validate_registry, segment_covered
from render_masterplan_svg import render

class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.zone = json.loads((ROOT / 'examples/zone_masterplan.json').read_text(encoding='utf-8'))

    def test_example_passes(self):
        errors, warnings = validate_zone(self.zone)
        self.assertEqual(errors, [])
        errors, warnings = validate_registry(ROOT / 'examples/city_master_index.json')
        self.assertEqual(errors, [])

    def test_building_road_collision_fails(self):
        z = copy.deepcopy(self.zone)
        z['buildings'][0]['built_footprint']['max_x'] = 18
        z['buildings'][0]['reserved_footprint']['max_x'] = 18
        errors, _ = validate_zone(z)
        self.assertTrue(any('overlaps road' in e for e in errors))

    def test_duplicate_id_fails(self):
        z = copy.deepcopy(self.zone)
        z['pois'][0]['id'] = 'B01'
        errors, _ = validate_zone(z)
        self.assertTrue(any('duplicate object ID' in e for e in errors))

    def test_disconnected_route_fails(self):
        z = copy.deepcopy(self.zone)
        z['routes'][0]['points'].insert(1, {'x':2, 'z':30})
        errors, _ = validate_zone(z)
        self.assertTrue(any('leaves circulation' in e for e in errors))

    def test_segment_union_coverage(self):
        a = {'min_x':0,'max_x':5,'min_z':0,'max_z':5}
        b = {'min_x':5,'max_x':10,'min_z':0,'max_z':5}
        self.assertTrue(segment_covered({'x':1,'z':2},{'x':9,'z':2},[a,b]))
        self.assertFalse(segment_covered({'x':1,'z':2},{'x':9,'z':8},[a,b]))

    def test_svg_contains_contract_ids(self):
        svg = render(self.zone)
        self.assertIn('B01', svg)
        self.assertIn('V01', svg)
        self.assertIn('C-SOUTH', json.dumps(self.zone))
        self.assertIn('Échelle', svg)
        self.assertIn('<svg', svg)

if __name__ == '__main__':
    unittest.main()
