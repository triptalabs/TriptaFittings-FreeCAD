# -*- coding: utf-8 -*-
"""
Clase Preset para representar datos de Ferrule y Gasket
Basado en estándares DIN 32676 A
"""

from typing import Dict, Any, Optional
import re


class Preset:
    """
    Clase para representar un preset de Ferrule o Gasket
    Contiene todos los parámetros necesarios para generar el modelo 3D
    """
    
    def __init__(self, component_type: str, data: Dict[str, Any]):
        """
        Inicializa un preset con los datos proporcionados
        
        Args:
            component_type: Tipo de componente ('ferrule' o 'gasket')
            data: Diccionario con los datos del preset
        """
        self.component_type = component_type.lower()
        self._validate_component_type()
        
        # Validar y asignar datos
        self._validate_and_assign_data(data)
    
    def _validate_component_type(self):
        """Valida que el tipo de componente sea válido"""
        valid_types = ['ferrule', 'gasket']
        if self.component_type not in valid_types:
            raise ValueError(f"Tipo de componente inválido: {self.component_type}. "
                           f"Tipos válidos: {valid_types}")
    
    def _validate_and_assign_data(self, data: Dict[str, Any]):
        """Valida y asigna los datos del preset"""
        # Campos comunes para ambos tipos
        self.size = self._extract_size(data.get('Size', ''))
        self.dn = data.get('DN', '')
        self.standard = data.get('Standard', 'DIN 32676 A')
        
        # Validar campos obligatorios
        if not self.size or not self.dn:
            raise ValueError("Los campos Size y DN son obligatorios")
        
        # Asignar campos específicos según el tipo
        if self.component_type == 'ferrule':
            self._assign_ferrule_data(data)
        elif self.component_type == 'gasket':
            self._assign_gasket_data(data)
    
    def _extract_size(self, size_str: str) -> float:
        """Extrae el valor numérico del tamaño de la cadena"""
        if not size_str:
            return 0.0
        
        # Buscar patrón como "1.5"" o "2""
        match = re.search(r'(\d+(?:\.\d+)?)', size_str)
        if match:
            return float(match.group(1))
        return 0.0
    
    def _assign_ferrule_data(self, data: Dict[str, Any]):
        """Asigna datos específicos de Ferrule"""
        self.flange_od_mm = self._validate_float(data.get('FlangeOD_mm', 0))
        self.c2_mm = self._validate_float(data.get('C2_mm', 0))
        self.tube_id_mm = self._validate_float(data.get('TubeID_mm', 0))
        self.passage_dia_mm = self._validate_float(data.get('PassageDia_mm', 0))
        self.height_tube_mm = self._validate_float(data.get('HeightTube_mm', 0))
        self.height_profile_mm = self._validate_float(data.get('HeightProfile_mm', 0))
        self.seat_lip_width_mm = self._validate_float(data.get('SeatLipWidth_mm', 0))
        
        # Validar que los datos sean coherentes
        self._validate_ferrule_coherence()
    
    def _assign_gasket_data(self, data: Dict[str, Any]):
        """Asigna datos específicos de Gasket"""
        self.flange_od_mm = self._validate_float(data.get('FlangeOD_mm', 0))
        self.gasket_od_mm = self._validate_float(data.get('GasketOD_mm', 0))
        self.gasket_id_mm = self._validate_float(data.get('GasketID_mm', 0))
        self.bead_c2_mm = self._validate_float(data.get('BeadC2_mm', 0))
        self.profile_h_mm = self._validate_float(data.get('ProfileH_mm', 0))
        self.seat_lip_width_mm = self._validate_float(data.get('SeatLipWidth_mm', 0))
        
        # Validar que los datos sean coherentes
        self._validate_gasket_coherence()
    
    def _validate_float(self, value: Any) -> float:
        """Valida y convierte un valor a float"""
        try:
            return float(value)
        except (ValueError, TypeError):
            raise ValueError(f"Valor inválido para float: {value}")
    
    def _validate_ferrule_coherence(self):
        """Valida la coherencia de los datos de Ferrule"""
        if self.tube_id_mm <= 0:
            raise ValueError("TubeID debe ser mayor que 0")
        if self.passage_dia_mm <= 0:
            raise ValueError("PassageDia debe ser mayor que 0")
        if self.flange_od_mm <= self.tube_id_mm:
            raise ValueError("FlangeOD debe ser mayor que TubeID")
    
    def _validate_gasket_coherence(self):
        """Valida la coherencia de los datos de Gasket"""
        if self.gasket_id_mm <= 0:
            raise ValueError("GasketID debe ser mayor que 0")
        if self.gasket_od_mm <= self.gasket_id_mm:
            raise ValueError("GasketOD debe ser mayor que GasketID")
        if self.flange_od_mm != self.gasket_od_mm:
            raise ValueError("FlangeOD debe ser igual a GasketOD para Gasket")
    
    def get_parameters_dict(self) -> Dict[str, Any]:
        """Retorna un diccionario con todos los parámetros del preset"""
        params = {
            'Size': self.size,
            'DN': self.dn,
            'Standard': self.standard,
            'ComponentType': self.component_type
        }
        
        if self.component_type == 'ferrule':
            params.update({
                'FlangeOD_mm': self.flange_od_mm,
                'C2_mm': self.c2_mm,
                'TubeID_mm': self.tube_id_mm,
                'PassageDia_mm': self.passage_dia_mm,
                'HeightTube_mm': self.height_tube_mm,
                'HeightProfile_mm': self.height_profile_mm,
                'SeatLipWidth_mm': self.seat_lip_width_mm
            })
        elif self.component_type == 'gasket':
            params.update({
                'FlangeOD_mm': self.flange_od_mm,
                'GasketOD_mm': self.gasket_od_mm,
                'GasketID_mm': self.gasket_id_mm,
                'BeadC2_mm': self.bead_c2_mm,
                'ProfileH_mm': self.profile_h_mm,
                'SeatLipWidth_mm': self.seat_lip_width_mm
            })
        
        return params
    
    def get_name(self) -> str:
        """Retorna el nombre del preset para nomenclatura"""
        return f"{self.component_type.capitalize()}_{self.size}in_{self.dn}"
    
    def __str__(self) -> str:
        """Representación en string del preset"""
        return f"{self.get_name()} ({self.standard})"
    
    def __repr__(self) -> str:
        """Representación detallada del preset"""
        return f"Preset(component_type='{self.component_type}', size={self.size}, dn='{self.dn}')"
    
    def is_compatible_with(self, other: 'Preset') -> bool:
        """
        Verifica si este preset es compatible con otro
        (mismo tamaño y DN)
        """
        return (self.size == other.size and 
                self.dn == other.dn and 
                self.standard == other.standard)
    
    def is_valid(self) -> bool:
        """
        Verifica si el preset es válido
        
        Returns:
            True si el preset tiene datos válidos
        """
        # Verificar campos básicos
        if not self.size or self.size <= 0:
            return False
        
        if not self.dn:
            return False
        
        if not self.standard:
            return False
        
        # Verificar campos específicos según el tipo
        if self.component_type == 'ferrule':
            return (hasattr(self, 'flange_od_mm') and self.flange_od_mm > 0 and
                    hasattr(self, 'tube_id_mm') and self.tube_id_mm > 0 and
                    hasattr(self, 'passage_dia_mm') and self.passage_dia_mm > 0)
        
        elif self.component_type == 'gasket':
            return (hasattr(self, 'flange_od_mm') and self.flange_od_mm > 0 and
                    hasattr(self, 'gasket_od_mm') and self.gasket_od_mm > 0 and
                    hasattr(self, 'gasket_id_mm') and self.gasket_id_mm > 0)
        
        return False
