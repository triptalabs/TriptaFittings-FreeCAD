# -*- coding: utf-8 -*-
"""
Cargador de archivos CSV para presets de Ferrule y Gasket
Maneja la carga y validación de datos desde archivos CSV
"""

import csv
import os
from typing import List, Dict, Any, Optional
from pathlib import Path
import logging

try:
    from .preset import Preset
except ImportError:
    # Para ejecución directa del script
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from data.preset import Preset


class CSVLoader:
    """
    Clase para cargar y parsear archivos CSV de presets
    Maneja la validación de formato y conversión de datos
    """
    
    def __init__(self, data_directory: str = None):
        """
        Inicializa el cargador CSV
        
        Args:
            data_directory: Directorio donde están los archivos CSV
        """
        if data_directory is None:
            # Obtener el directorio actual del módulo
            current_dir = Path(__file__).parent
            self.data_directory = current_dir
        else:
            self.data_directory = Path(data_directory)
        
        # Configurar logging
        self.logger = logging.getLogger(__name__)
        
        # Archivos CSV esperados
        self.ferrule_csv = "presets_ferrule_din32676A_1p5_to_12in.csv"
        self.gasket_csv = "Presets_Gasket_DIN_32676_A__1_5_12_in_.csv"
    
    def load_ferrule_data(self) -> List[Preset]:
        """
        Carga los datos de Ferrule desde el archivo CSV
        
        Returns:
            Lista de objetos Preset para Ferrule
            
        Raises:
            FileNotFoundError: Si el archivo no existe
            ValueError: Si hay errores en el formato de datos
        """
        csv_path = self.data_directory / self.ferrule_csv
        
        if not csv_path.exists():
            raise FileNotFoundError(f"Archivo de presets de Ferrule no encontrado: {csv_path}")
        
        self.logger.info(f"Cargando datos de Ferrule desde: {csv_path}")
        
        try:
            presets = []
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                # Validar headers
                self._validate_ferrule_headers(reader.fieldnames)
                
                for row_num, row in enumerate(reader, start=2):  # Empezar en 2 (header es 1)
                    try:
                        # Limpiar datos
                        cleaned_row = self._clean_row_data(row)
                        
                        # Crear preset
                        preset = Preset('ferrule', cleaned_row)
                        presets.append(preset)
                        
                        self.logger.debug(f"Preset cargado: {preset}")
                        
                    except ValueError as e:
                        self.logger.error(f"Error en fila {row_num}: {e}")
                        raise ValueError(f"Error en fila {row_num}: {e}")
            
            self.logger.info(f"Cargados {len(presets)} presets de Ferrule")
            return presets
            
        except Exception as e:
            self.logger.error(f"Error al cargar archivo de Ferrule: {e}")
            raise
    
    def load_gasket_data(self) -> List[Preset]:
        """
        Carga los datos de Gasket desde el archivo CSV
        
        Returns:
            Lista de objetos Preset para Gasket
            
        Raises:
            FileNotFoundError: Si el archivo no existe
            ValueError: Si hay errores en el formato de datos
        """
        csv_path = self.data_directory / self.gasket_csv
        
        if not csv_path.exists():
            raise FileNotFoundError(f"Archivo de presets de Gasket no encontrado: {csv_path}")
        
        self.logger.info(f"Cargando datos de Gasket desde: {csv_path}")
        
        try:
            presets = []
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                # Validar headers
                self._validate_gasket_headers(reader.fieldnames)
                
                for row_num, row in enumerate(reader, start=2):  # Empezar en 2 (header es 1)
                    try:
                        # Limpiar datos
                        cleaned_row = self._clean_row_data(row)
                        
                        # Crear preset
                        preset = Preset('gasket', cleaned_row)
                        presets.append(preset)
                        
                        self.logger.debug(f"Preset cargado: {preset}")
                        
                    except ValueError as e:
                        self.logger.error(f"Error en fila {row_num}: {e}")
                        raise ValueError(f"Error en fila {row_num}: {e}")
            
            self.logger.info(f"Cargados {len(presets)} presets de Gasket")
            return presets
            
        except Exception as e:
            self.logger.error(f"Error al cargar archivo de Gasket: {e}")
            raise
    
    def _validate_ferrule_headers(self, headers: List[str]):
        """Valida que los headers del CSV de Ferrule sean correctos"""
        expected_headers = [
            'Size', 'DN', 'FlangeOD_mm', 'C2_mm', 'TubeID_mm', 
            'PassageDia_mm', 'HeightTube_mm', 'HeightProfile_mm', 
            'SeatLipWidth_mm', 'Standard'
        ]
        
        if not headers:
            raise ValueError("El archivo CSV no tiene headers")
        
        missing_headers = set(expected_headers) - set(headers)
        if missing_headers:
            raise ValueError(f"Headers faltantes en CSV de Ferrule: {missing_headers}")
    
    def _validate_gasket_headers(self, headers: List[str]):
        """Valida que los headers del CSV de Gasket sean correctos"""
        expected_headers = [
            'Size', 'DN', 'FlangeOD_mm', 'GasketOD_mm', 'GasketID_mm',
            'BeadC2_mm', 'ProfileH_mm', 'SeatLipWidth_mm', 'Standard'
        ]
        
        if not headers:
            raise ValueError("El archivo CSV no tiene headers")
        
        missing_headers = set(expected_headers) - set(headers)
        if missing_headers:
            raise ValueError(f"Headers faltantes en CSV de Gasket: {missing_headers}")
    
    def _clean_row_data(self, row: Dict[str, str]) -> Dict[str, Any]:
        """
        Limpia y convierte los datos de una fila CSV
        
        Args:
            row: Fila del CSV como diccionario
            
        Returns:
            Diccionario con datos limpios
        """
        cleaned = {}
        
        for key, value in row.items():
            if value is None or value.strip() == '':
                # Mantener valores vacíos como están
                cleaned[key] = value
            else:
                # Limpiar espacios en blanco
                cleaned[key] = value.strip()
        
        return cleaned
    
    def get_available_files(self) -> Dict[str, bool]:
        """
        Verifica qué archivos CSV están disponibles
        
        Returns:
            Diccionario con el estado de cada archivo
        """
        files_status = {}
        
        ferrule_path = self.data_directory / self.ferrule_csv
        gasket_path = self.data_directory / self.gasket_csv
        
        files_status['ferrule'] = ferrule_path.exists()
        files_status['gasket'] = gasket_path.exists()
        
        return files_status
    
    def validate_data_integrity(self) -> Dict[str, Any]:
        """
        Valida la integridad de todos los archivos CSV
        
        Returns:
            Diccionario con resultados de validación
        """
        results = {
            'ferrule': {'valid': False, 'errors': [], 'presets_count': 0},
            'gasket': {'valid': False, 'errors': [], 'presets_count': 0}
        }
        
        # Validar Ferrule
        try:
            ferrule_presets = self.load_ferrule_data()
            results['ferrule']['valid'] = True
            results['ferrule']['presets_count'] = len(ferrule_presets)
        except Exception as e:
            results['ferrule']['errors'].append(str(e))
        
        # Validar Gasket
        try:
            gasket_presets = self.load_gasket_data()
            results['gasket']['valid'] = True
            results['gasket']['presets_count'] = len(gasket_presets)
        except Exception as e:
            results['gasket']['errors'].append(str(e))
        
        return results
