# -*- coding: utf-8 -*-
"""
Tests unitarios para la clase Preset
"""

import unittest
from unittest.mock import patch
import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data.preset import Preset


class TestPreset(unittest.TestCase):
    """Tests para la clase Preset"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        # Datos de ejemplo para Ferrule
        self.ferrule_data = {
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
        
        # Datos de ejemplo para Gasket
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
    
    def test_ferrule_preset_creation(self):
        """Test creación de preset de Ferrule"""
        preset = Preset('ferrule', self.ferrule_data)
        
        self.assertEqual(preset.component_type, 'ferrule')
        self.assertEqual(preset.size, 3.0)
        self.assertEqual(preset.dn, 'DN80')
        self.assertEqual(preset.standard, 'DIN 32676 A')
        self.assertEqual(preset.flange_od_mm, 106.0)
        self.assertEqual(preset.tube_id_mm, 81.2)
        self.assertEqual(preset.passage_dia_mm, 81.0)
    
    def test_gasket_preset_creation(self):
        """Test creación de preset de Gasket"""
        preset = Preset('gasket', self.gasket_data)
        
        self.assertEqual(preset.component_type, 'gasket')
        self.assertEqual(preset.size, 3.0)
        self.assertEqual(preset.dn, 'DN80')
        self.assertEqual(preset.standard, 'DIN 32676 A')
        self.assertEqual(preset.flange_od_mm, 106.0)
        self.assertEqual(preset.gasket_od_mm, 106.0)
        self.assertEqual(preset.gasket_id_mm, 81.2)
    
    def test_invalid_component_type(self):
        """Test error con tipo de componente inválido"""
        with self.assertRaises(ValueError) as context:
            Preset('invalid_type', self.ferrule_data)
        
        self.assertIn('Tipo de componente inválido', str(context.exception))
    
    def test_missing_required_fields(self):
        """Test error con campos obligatorios faltantes"""
        incomplete_data = {'Size': '3"'}  # Falta DN
        
        with self.assertRaises(ValueError) as context:
            Preset('ferrule', incomplete_data)
        
        self.assertIn('campos Size y DN son obligatorios', str(context.exception))
    
    def test_size_extraction(self):
        """Test extracción de tamaño de diferentes formatos"""
        # Test con comillas
        data1 = self.ferrule_data.copy()
        data1['Size'] = '1.5"'
        preset1 = Preset('ferrule', data1)
        self.assertEqual(preset1.size, 1.5)
        
        # Test sin comillas
        data2 = self.ferrule_data.copy()
        data2['Size'] = '2.0'
        preset2 = Preset('ferrule', data2)
        self.assertEqual(preset2.size, 2.0)
        
        # Test con espacios
        data3 = self.ferrule_data.copy()
        data3['Size'] = ' 4.0 " '
        preset3 = Preset('ferrule', data3)
        self.assertEqual(preset3.size, 4.0)
    
    def test_ferrule_coherence_validation(self):
        """Test validación de coherencia para Ferrule"""
        # Test con TubeID inválido
        invalid_data = self.ferrule_data.copy()
        invalid_data['TubeID_mm'] = 0
        
        with self.assertRaises(ValueError) as context:
            Preset('ferrule', invalid_data)
        
        self.assertIn('TubeID debe ser mayor que 0', str(context.exception))
        
        # Test con FlangeOD menor que TubeID
        invalid_data2 = self.ferrule_data.copy()
        invalid_data2['FlangeOD_mm'] = 50.0  # Menor que TubeID (81.2)
        
        with self.assertRaises(ValueError) as context:
            Preset('ferrule', invalid_data2)
        
        self.assertIn('FlangeOD debe ser mayor que TubeID', str(context.exception))
    
    def test_gasket_coherence_validation(self):
        """Test validación de coherencia para Gasket"""
        # Test con GasketOD menor que GasketID
        invalid_data = self.gasket_data.copy()
        invalid_data['GasketOD_mm'] = 50.0  # Menor que GasketID (81.2)
        
        with self.assertRaises(ValueError) as context:
            Preset('gasket', invalid_data)
        
        self.assertIn('GasketOD debe ser mayor que GasketID', str(context.exception))
        
        # Test con FlangeOD diferente a GasketOD
        invalid_data2 = self.gasket_data.copy()
        invalid_data2['FlangeOD_mm'] = 100.0  # Diferente a GasketOD (106.0)
        
        with self.assertRaises(ValueError) as context:
            Preset('gasket', invalid_data2)
        
        self.assertIn('FlangeOD debe ser igual a GasketOD', str(context.exception))
    
    def test_get_parameters_dict(self):
        """Test obtención de diccionario de parámetros"""
        ferrule_preset = Preset('ferrule', self.ferrule_data)
        gasket_preset = Preset('gasket', self.gasket_data)
        
        # Test Ferrule
        ferrule_params = ferrule_preset.get_parameters_dict()
        self.assertEqual(ferrule_params['ComponentType'], 'ferrule')
        self.assertEqual(ferrule_params['FlangeOD_mm'], 106.0)
        self.assertEqual(ferrule_params['TubeID_mm'], 81.2)
        
        # Test Gasket
        gasket_params = gasket_preset.get_parameters_dict()
        self.assertEqual(gasket_params['ComponentType'], 'gasket')
        self.assertEqual(gasket_params['GasketOD_mm'], 106.0)
        self.assertEqual(gasket_params['GasketID_mm'], 81.2)
    
    def test_get_name(self):
        """Test generación de nombre del preset"""
        ferrule_preset = Preset('ferrule', self.ferrule_data)
        gasket_preset = Preset('gasket', self.gasket_data)
        
        self.assertEqual(ferrule_preset.get_name(), 'Ferrule_3.0in_DN80')
        self.assertEqual(gasket_preset.get_name(), 'Gasket_3.0in_DN80')
    
    def test_compatibility_check(self):
        """Test verificación de compatibilidad entre presets"""
        ferrule_preset = Preset('ferrule', self.ferrule_data)
        gasket_preset = Preset('gasket', self.gasket_data)
        
        # Deberían ser compatibles (mismo tamaño y DN)
        self.assertTrue(ferrule_preset.is_compatible_with(gasket_preset))
        
        # Crear preset incompatible
        incompatible_data = self.gasket_data.copy()
        incompatible_data['Size'] = '4"'
        incompatible_data['DN'] = 'DN100'
        incompatible_preset = Preset('gasket', incompatible_data)
        
        self.assertFalse(ferrule_preset.is_compatible_with(incompatible_preset))
    
    def test_string_representations(self):
        """Test representaciones en string"""
        preset = Preset('ferrule', self.ferrule_data)
        
        # Test __str__
        str_repr = str(preset)
        self.assertIn('Ferrule_3.0in_DN80', str_repr)
        self.assertIn('DIN 32676 A', str_repr)
        
        # Test __repr__
        repr_repr = repr(preset)
        self.assertIn("Preset(component_type='ferrule'", repr_repr)
        self.assertIn("size=3.0", repr_repr)
        self.assertIn("dn='DN80'", repr_repr)


if __name__ == '__main__':
    unittest.main()
