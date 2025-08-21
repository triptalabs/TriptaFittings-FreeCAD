# -*- coding: utf-8 -*-
"""
Gestor de datos para TriptaFittings
Punto central para gestionar presets de Ferrule y Gasket
"""

from typing import List, Dict, Any, Optional, Tuple
import logging
from pathlib import Path

try:
    from ..data.csv_loader import CSVLoader
    from ..data.preset import Preset
except ImportError:
    # Para ejecución directa del script
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from data.csv_loader import CSVLoader
    from data.preset import Preset


class DataManager:
    """
    Gestor central de datos para el plugin TriptaFittings
    Maneja la carga, cacheo y búsqueda de presets
    """
    
    def __init__(self, data_directory: str = None):
        """
        Inicializa el gestor de datos
        
        Args:
            data_directory: Directorio donde están los archivos CSV
        """
        self.logger = logging.getLogger(__name__)
        
        # Inicializar cargador CSV
        self.csv_loader = CSVLoader(data_directory)
        
        # Cache de presets para búsquedas rápidas
        self._ferrule_presets: List[Preset] = []
        self._gasket_presets: List[Preset] = []
        
        # Diccionarios para búsquedas optimizadas
        self._ferrule_by_size: Dict[float, Preset] = {}
        self._ferrule_by_dn: Dict[str, Preset] = {}
        self._gasket_by_size: Dict[float, Preset] = {}
        self._gasket_by_dn: Dict[str, Preset] = {}
        
        # Estado de carga
        self._loaded = False
        self._load_errors = []
    
    def load_all_data(self) -> bool:
        """
        Carga todos los datos de presets desde los archivos CSV
        
        Returns:
            True si la carga fue exitosa, False en caso contrario
        """
        self.logger.info("Iniciando carga de todos los datos de presets")
        
        try:
            # Cargar datos de Ferrule
            self._ferrule_presets = self.csv_loader.load_ferrule_data()
            self.logger.info(f"Cargados {len(self._ferrule_presets)} presets de Ferrule")
            
            # Cargar datos de Gasket
            self._gasket_presets = self.csv_loader.load_gasket_data()
            self.logger.info(f"Cargados {len(self._gasket_presets)} presets de Gasket")
            
            # Construir índices de búsqueda
            self._build_search_indices()
            
            # Validar compatibilidad entre Ferrule y Gasket
            self._validate_compatibility()
            
            self._loaded = True
            self.logger.info("Carga de datos completada exitosamente")
            return True
            
        except Exception as e:
            self._load_errors.append(str(e))
            self.logger.error(f"Error al cargar datos: {e}")
            return False
    
    def _build_search_indices(self):
        """Construye índices optimizados para búsquedas rápidas"""
        # Índices para Ferrule
        for preset in self._ferrule_presets:
            self._ferrule_by_size[preset.size] = preset
            self._ferrule_by_dn[preset.dn] = preset
        
        # Índices para Gasket
        for preset in self._gasket_presets:
            self._gasket_by_size[preset.size] = preset
            self._gasket_by_dn[preset.dn] = preset
        
        self.logger.debug(f"Índices construidos: {len(self._ferrule_by_size)} Ferrule, {len(self._gasket_by_size)} Gasket")
    
    def _validate_compatibility(self):
        """Valida que existan presets compatibles entre Ferrule y Gasket"""
        ferrule_sizes = set(self._ferrule_by_size.keys())
        gasket_sizes = set(self._gasket_by_size.keys())
        
        missing_gaskets = ferrule_sizes - gasket_sizes
        missing_ferrules = gasket_sizes - ferrule_sizes
        
        if missing_gaskets:
            self.logger.warning(f"Faltan presets de Gasket para tamaños: {missing_gaskets}")
        
        if missing_ferrules:
            self.logger.warning(f"Faltan presets de Ferrule para tamaños: {missing_ferrules}")
    
    def get_preset_by_size(self, component: str, size: float) -> Optional[Preset]:
        """
        Obtiene un preset por tamaño y tipo de componente
        
        Args:
            component: Tipo de componente ('ferrule' o 'gasket')
            size: Tamaño en pulgadas (ej: 1.5, 2.0, etc.)
            
        Returns:
            Preset correspondiente o None si no se encuentra
        """
        if not self._loaded:
            self.logger.warning("Datos no cargados. Llamando a load_all_data()")
            if not self.load_all_data():
                return None
        
        component = component.lower()
        
        if component == 'ferrule':
            return self._ferrule_by_size.get(size)
        elif component == 'gasket':
            return self._gasket_by_size.get(size)
        else:
            self.logger.error(f"Tipo de componente inválido: {component}")
            return None
    
    def get_preset_by_dn(self, component: str, dn: str) -> Optional[Preset]:
        """
        Obtiene un preset por DN y tipo de componente
        
        Args:
            component: Tipo de componente ('ferrule' o 'gasket')
            dn: DN del componente (ej: 'DN40', 'DN80', etc.)
            
        Returns:
            Preset correspondiente o None si no se encuentra
        """
        if not self._loaded:
            self.logger.warning("Datos no cargados. Llamando a load_all_data()")
            if not self.load_all_data():
                return None
        
        component = component.lower()
        
        if component == 'ferrule':
            return self._ferrule_by_dn.get(dn)
        elif component == 'gasket':
            return self._gasket_by_dn.get(dn)
        else:
            self.logger.error(f"Tipo de componente inválido: {component}")
            return None
    
    def get_available_sizes(self, component: str = None) -> List[float]:
        """
        Obtiene la lista de tamaños disponibles
        
        Args:
            component: Tipo de componente específico ('ferrule', 'gasket') o None para ambos
            
        Returns:
            Lista de tamaños disponibles ordenados
        """
        if not self._loaded:
            self.logger.warning("Datos no cargados. Llamando a load_all_data()")
            if not self.load_all_data():
                return []
        
        if component is None:
            # Combinar tamaños de ambos componentes
            all_sizes = set(self._ferrule_by_size.keys()) | set(self._gasket_by_size.keys())
        elif component.lower() == 'ferrule':
            all_sizes = set(self._ferrule_by_size.keys())
        elif component.lower() == 'gasket':
            all_sizes = set(self._gasket_by_size.keys())
        else:
            self.logger.error(f"Tipo de componente inválido: {component}")
            return []
        
        return sorted(list(all_sizes))
    
    def get_available_dns(self, component: str = None) -> List[str]:
        """
        Obtiene la lista de DNs disponibles
        
        Args:
            component: Tipo de componente específico ('ferrule', 'gasket') o None para ambos
            
        Returns:
            Lista de DNs disponibles ordenados
        """
        if not self._loaded:
            self.logger.warning("Datos no cargados. Llamando a load_all_data()")
            if not self.load_all_data():
                return []
        
        if component is None:
            # Combinar DNs de ambos componentes
            all_dns = set(self._ferrule_by_dn.keys()) | set(self._gasket_by_dn.keys())
        elif component.lower() == 'ferrule':
            all_dns = set(self._ferrule_by_dn.keys())
        elif component.lower() == 'gasket':
            all_dns = set(self._gasket_by_dn.keys())
        else:
            self.logger.error(f"Tipo de componente inválido: {component}")
            return []
        
        # Ordenar DNs numéricamente
        return sorted(all_dns, key=lambda x: int(x[2:]))  # Extraer número de 'DN40' -> 40
    
    def get_compatible_presets(self, size: float) -> Tuple[Optional[Preset], Optional[Preset]]:
        """
        Obtiene presets compatibles de Ferrule y Gasket para un tamaño dado
        
        Args:
            size: Tamaño en pulgadas
            
        Returns:
            Tupla (ferrule_preset, gasket_preset) - uno puede ser None
        """
        ferrule = self.get_preset_by_size('ferrule', size)
        gasket = self.get_preset_by_size('gasket', size)
        
        return ferrule, gasket
    
    def get_all_presets(self, component: str = None) -> List[Preset]:
        """
        Obtiene todos los presets de un componente o ambos
        
        Args:
            component: Tipo de componente específico ('ferrule', 'gasket') o None para ambos
            
        Returns:
            Lista de todos los presets
        """
        if not self._loaded:
            self.logger.warning("Datos no cargados. Llamando a load_all_data()")
            if not self.load_all_data():
                return []
        
        if component is None:
            return self._ferrule_presets + self._gasket_presets
        elif component.lower() == 'ferrule':
            return self._ferrule_presets.copy()
        elif component.lower() == 'gasket':
            return self._gasket_presets.copy()
        else:
            self.logger.error(f"Tipo de componente inválido: {component}")
            return []
    
    def get_data_summary(self) -> Dict[str, Any]:
        """
        Obtiene un resumen de los datos cargados
        
        Returns:
            Diccionario con estadísticas de los datos
        """
        if not self._loaded:
            return {
                'loaded': False,
                'errors': self._load_errors,
                'ferrule_count': 0,
                'gasket_count': 0,
                'available_sizes': [],
                'available_dns': []
            }
        
        return {
            'loaded': True,
            'errors': self._load_errors,
            'ferrule_count': len(self._ferrule_presets),
            'gasket_count': len(self._gasket_presets),
            'available_sizes': self.get_available_sizes(),
            'available_dns': self.get_available_dns(),
            'total_presets': len(self._ferrule_presets) + len(self._gasket_presets)
        }
    
    def validate_data_integrity(self) -> Dict[str, Any]:
        """
        Valida la integridad de todos los datos
        
        Returns:
            Diccionario con resultados de validación
        """
        return self.csv_loader.validate_data_integrity()
    
    def reload_data(self) -> bool:
        """
        Recarga todos los datos desde los archivos CSV
        
        Returns:
            True si la recarga fue exitosa
        """
        self.logger.info("Recargando datos de presets")
        
        # Limpiar cache
        self._ferrule_presets = []
        self._gasket_presets = []
        self._ferrule_by_size.clear()
        self._ferrule_by_dn.clear()
        self._gasket_by_size.clear()
        self._gasket_by_dn.clear()
        self._loaded = False
        self._load_errors.clear()
        
        # Recargar
        return self.load_all_data()
    
    def get_presets_by_type(self, component_type: str) -> List[Preset]:
        """
        Retorna todos los presets de un tipo específico
        
        Args:
            component_type: Tipo de componente ('ferrule' o 'gasket')
            
        Returns:
            Lista de presets del tipo especificado
        """
        if not self._loaded:
            self.logger.warning("Datos no cargados. Llamando a load_all_data()")
            if not self.load_all_data():
                return []
        
        if component_type.lower() == 'ferrule':
            return self._ferrule_presets.copy()
        elif component_type.lower() == 'gasket':
            return self._gasket_presets.copy()
        else:
            self.logger.error(f"Tipo de componente inválido: {component_type}")
            return []
    
    def get_preset_by_size_and_type(self, size: float, component_type: str) -> Optional[Preset]:
        """
        Retorna un preset específico por tamaño y tipo
        
        Args:
            size: Tamaño en pulgadas
            component_type: Tipo de componente ('ferrule' o 'gasket')
            
        Returns:
            Preset correspondiente o None si no se encuentra
        """
        if not self._loaded:
            self.logger.warning("Datos no cargados. Llamando a load_all_data()")
            if not self.load_all_data():
                return None
        
        if component_type.lower() == 'ferrule':
            return self._ferrule_by_size.get(size)
        elif component_type.lower() == 'gasket':
            return self._gasket_by_size.get(size)
        else:
            self.logger.error(f"Tipo de componente inválido: {component_type}")
            return None
