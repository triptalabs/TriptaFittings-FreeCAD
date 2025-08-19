# -*- coding: utf-8 -*-
"""Tests unitarios para ``GasketGenerator``."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data.preset import Preset
from models.gasket_generator import GasketGenerator


class TestGasketGenerator(unittest.TestCase):
    def setUp(self):
        self.gasket_data = {
            'Size': '3"',
            'DN': 'DN80',
            'FlangeOD_mm': 106.0,
            'GasketOD_mm': 106.0,
            'GasketID_mm': 81.2,
            'BeadC2_mm': 97.0,
            'ProfileH_mm': 4.3,
            'SeatLipWidth_mm': 1.0,
            'Standard': 'DIN 32676 A'
        }
        self.preset = Preset('gasket', self.gasket_data)
        self.generator = GasketGenerator(self.preset)

    def test_generate_geometry(self):
        geometry = self.generator.generate_geometry()
        self.assertEqual(geometry['name'], 'Gasket_3.0in_DN80')
        params = geometry['parameters']
        self.assertEqual(params['GasketOD_mm'], 106.0)
        self.assertEqual(params['GasketID_mm'], 81.2)

    def test_update_spreadsheet(self):
        sheet = {}
        self.generator.update_spreadsheet(sheet)
        self.assertIn('ProfileH_mm', sheet)
        self.assertEqual(sheet['BeadC2_mm'], 97.0)

    def test_invalid_preset_type(self):
        ferrule_data = {
            'Size': '3"',
            'DN': 'DN80',
            'FlangeOD_mm': 106.0,
            'C2_mm': 97.0,
            'TubeID_mm': 81.2,
            'PassageDia_mm': 81.0,
            'HeightTube_mm': 24.0,
            'HeightProfile_mm': 4.3,
            'SeatLipWidth_mm': 1.0,
            'Standard': 'DIN 32676 A'
        }
        ferrule_preset = Preset('ferrule', ferrule_data)
        with self.assertRaises(ValueError):
            GasketGenerator(ferrule_preset)


if __name__ == '__main__':
    unittest.main()
