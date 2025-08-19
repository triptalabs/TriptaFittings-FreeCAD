# -*- coding: utf-8 -*-
"""
Tests unitarios para la clase DataManager
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import tempfile
import shutil

# Agregar el directorio raíz al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.data_manager import DataManager
from data.preset import Preset


class TestDataManager(unittest.TestCase):
    """Tests para la clase DataManager"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        # Crear directorio temporal para tests
        self.test_dir = tempfile.mkdtemp()
        
        # Datos de ejemplo
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
        
        # Crear presets de ejemplo
        self.ferrule_preset = Preset('ferrule', self.ferrule_data)
        self.gasket_preset = Preset('gasket', self.gasket_data)
    
    def tearDown(self):
        """Limpieza después de cada test"""
        # Eliminar directorio temporal
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    @patch('models.data_manager.CSVLoader')
    def test_data_manager_initialization(self, mock_csv_loader):
        """Test inicialización del DataManager"""
        data_manager = DataManager(self.test_dir)
        
        self.assertFalse(data_manager._loaded)
        self.assertEqual(len(data_manager._load_errors), 0)
        self.assertEqual(len(data_manager._ferrule_presets), 0)
        self.assertEqual(len(data_manager._gasket_presets), 0)
        
        # Verificar que se inicializó el CSVLoader
        mock_csv_loader.assert_called_once_with(self.test_dir)
    
    @patch('models.data_manager.CSVLoader')
    def test_load_all_data_success(self, mock_csv_loader):
        """Test carga exitosa de todos los datos"""
        # Configurar mock
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.return_value = [self.ferrule_preset]
        mock_loader_instance.load_gasket_data.return_value = [self.gasket_preset]
        
        data_manager = DataManager(self.test_dir)
        result = data_manager.load_all_data()
        
        self.assertTrue(result)
        self.assertTrue(data_manager._loaded)
        self.assertEqual(len(data_manager._ferrule_presets), 1)
        self.assertEqual(len(data_manager._gasket_presets), 1)
        self.assertEqual(len(data_manager._load_errors), 0)
        
        # Verificar que se construyeron los índices
        self.assertIn(3.0, data_manager._ferrule_by_size)
        self.assertIn('DN80', data_manager._ferrule_by_dn)
        self.assertIn(3.0, data_manager._gasket_by_size)
        self.assertIn('DN80', data_manager._gasket_by_dn)
    
    @patch('models.data_manager.CSVLoader')
    def test_load_all_data_failure(self, mock_csv_loader):
        """Test fallo en la carga de datos"""
        # Configurar mock para que falle
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.side_effect = Exception("Error de carga")
        
        data_manager = DataManager(self.test_dir)
        result = data_manager.load_all_data()
        
        self.assertFalse(result)
        self.assertFalse(data_manager._loaded)
        self.assertEqual(len(data_manager._load_errors), 1)
        self.assertIn("Error de carga", data_manager._load_errors[0])
    
    @patch('models.data_manager.CSVLoader')
    def test_get_preset_by_size(self, mock_csv_loader):
        """Test búsqueda de preset por tamaño"""
        # Configurar mock y cargar datos
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.return_value = [self.ferrule_preset]
        mock_loader_instance.load_gasket_data.return_value = [self.gasket_preset]
        
        data_manager = DataManager(self.test_dir)
        data_manager.load_all_data()
        
        # Test búsqueda exitosa
        ferrule_result = data_manager.get_preset_by_size('ferrule', 3.0)
        gasket_result = data_manager.get_preset_by_size('gasket', 3.0)
        
        self.assertEqual(ferrule_result, self.ferrule_preset)
        self.assertEqual(gasket_result, self.gasket_preset)
        
        # Test búsqueda fallida
        not_found = data_manager.get_preset_by_size('ferrule', 99.0)
        self.assertIsNone(not_found)
        
        # Test tipo de componente inválido
        invalid = data_manager.get_preset_by_size('invalid', 3.0)
        self.assertIsNone(invalid)
    
    @patch('models.data_manager.CSVLoader')
    def test_get_preset_by_dn(self, mock_csv_loader):
        """Test búsqueda de preset por DN"""
        # Configurar mock y cargar datos
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.return_value = [self.ferrule_preset]
        mock_loader_instance.load_gasket_data.return_value = [self.gasket_preset]
        
        data_manager = DataManager(self.test_dir)
        data_manager.load_all_data()
        
        # Test búsqueda exitosa
        ferrule_result = data_manager.get_preset_by_dn('ferrule', 'DN80')
        gasket_result = data_manager.get_preset_by_dn('gasket', 'DN80')
        
        self.assertEqual(ferrule_result, self.ferrule_preset)
        self.assertEqual(gasket_result, self.gasket_preset)
        
        # Test búsqueda fallida
        not_found = data_manager.get_preset_by_dn('ferrule', 'DN999')
        self.assertIsNone(not_found)
    
    @patch('models.data_manager.CSVLoader')
    def test_get_available_sizes(self, mock_csv_loader):
        """Test obtención de tamaños disponibles"""
        # Configurar mock y cargar datos
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.return_value = [self.ferrule_preset]
        mock_loader_instance.load_gasket_data.return_value = [self.gasket_preset]
        
        data_manager = DataManager(self.test_dir)
        data_manager.load_all_data()
        
        # Test todos los tamaños
        all_sizes = data_manager.get_available_sizes()
        self.assertEqual(all_sizes, [3.0])
        
        # Test tamaños específicos
        ferrule_sizes = data_manager.get_available_sizes('ferrule')
        self.assertEqual(ferrule_sizes, [3.0])
        
        gasket_sizes = data_manager.get_available_sizes('gasket')
        self.assertEqual(gasket_sizes, [3.0])
        
        # Test tipo inválido
        invalid_sizes = data_manager.get_available_sizes('invalid')
        self.assertEqual(invalid_sizes, [])
    
    @patch('models.data_manager.CSVLoader')
    def test_get_available_dns(self, mock_csv_loader):
        """Test obtención de DNs disponibles"""
        # Configurar mock y cargar datos
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.return_value = [self.ferrule_preset]
        mock_loader_instance.load_gasket_data.return_value = [self.gasket_preset]
        
        data_manager = DataManager(self.test_dir)
        data_manager.load_all_data()
        
        # Test todos los DNs
        all_dns = data_manager.get_available_dns()
        self.assertEqual(all_dns, ['DN80'])
        
        # Test DNs específicos
        ferrule_dns = data_manager.get_available_dns('ferrule')
        self.assertEqual(ferrule_dns, ['DN80'])
        
        gasket_dns = data_manager.get_available_dns('gasket')
        self.assertEqual(gasket_dns, ['DN80'])
    
    @patch('models.data_manager.CSVLoader')
    def test_get_compatible_presets(self, mock_csv_loader):
        """Test obtención de presets compatibles"""
        # Configurar mock y cargar datos
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.return_value = [self.ferrule_preset]
        mock_loader_instance.load_gasket_data.return_value = [self.gasket_preset]
        
        data_manager = DataManager(self.test_dir)
        data_manager.load_all_data()
        
        # Test presets compatibles
        ferrule, gasket = data_manager.get_compatible_presets(3.0)
        self.assertEqual(ferrule, self.ferrule_preset)
        self.assertEqual(gasket, self.gasket_preset)
        
        # Test tamaño no encontrado
        ferrule, gasket = data_manager.get_compatible_presets(99.0)
        self.assertIsNone(ferrule)
        self.assertIsNone(gasket)
    
    @patch('models.data_manager.CSVLoader')
    def test_get_all_presets(self, mock_csv_loader):
        """Test obtención de todos los presets"""
        # Configurar mock y cargar datos
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.return_value = [self.ferrule_preset]
        mock_loader_instance.load_gasket_data.return_value = [self.gasket_preset]
        
        data_manager = DataManager(self.test_dir)
        data_manager.load_all_data()
        
        # Test todos los presets
        all_presets = data_manager.get_all_presets()
        self.assertEqual(len(all_presets), 2)
        self.assertIn(self.ferrule_preset, all_presets)
        self.assertIn(self.gasket_preset, all_presets)
        
        # Test presets específicos
        ferrule_presets = data_manager.get_all_presets('ferrule')
        self.assertEqual(ferrule_presets, [self.ferrule_preset])
        
        gasket_presets = data_manager.get_all_presets('gasket')
        self.assertEqual(gasket_presets, [self.gasket_preset])
    
    @patch('models.data_manager.CSVLoader')
    def test_get_data_summary(self, mock_csv_loader):
        """Test obtención de resumen de datos"""
        # Configurar mock y cargar datos
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.return_value = [self.ferrule_preset]
        mock_loader_instance.load_gasket_data.return_value = [self.gasket_preset]
        
        data_manager = DataManager(self.test_dir)
        
        # Test antes de cargar
        summary_before = data_manager.get_data_summary()
        self.assertFalse(summary_before['loaded'])
        self.assertEqual(summary_before['ferrule_count'], 0)
        self.assertEqual(summary_before['gasket_count'], 0)
        
        # Cargar datos
        data_manager.load_all_data()
        
        # Test después de cargar
        summary_after = data_manager.get_data_summary()
        self.assertTrue(summary_after['loaded'])
        self.assertEqual(summary_after['ferrule_count'], 1)
        self.assertEqual(summary_after['gasket_count'], 1)
        self.assertEqual(summary_after['total_presets'], 2)
        self.assertEqual(summary_after['available_sizes'], [3.0])
        self.assertEqual(summary_after['available_dns'], ['DN80'])
    
    @patch('models.data_manager.CSVLoader')
    def test_reload_data(self, mock_csv_loader):
        """Test recarga de datos"""
        # Configurar mock
        mock_loader_instance = MagicMock()
        mock_csv_loader.return_value = mock_loader_instance
        mock_loader_instance.load_ferrule_data.return_value = [self.ferrule_preset]
        mock_loader_instance.load_gasket_data.return_value = [self.gasket_preset]
        
        data_manager = DataManager(self.test_dir)
        
        # Cargar datos inicialmente
        data_manager.load_all_data()
        self.assertTrue(data_manager._loaded)
        self.assertEqual(len(data_manager._ferrule_presets), 1)
        
        # Recargar datos
        result = data_manager.reload_data()
        self.assertTrue(result)
        self.assertTrue(data_manager._loaded)
        self.assertEqual(len(data_manager._ferrule_presets), 1)
        self.assertEqual(len(data_manager._gasket_presets), 1)


if __name__ == '__main__':
    unittest.main()
