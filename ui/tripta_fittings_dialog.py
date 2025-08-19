# -*- coding: utf-8 -*-
"""Diálogo simplificado para generar modelos en TriptaFittings.

Este módulo implementa una versión sin dependencias gráficas del diálogo
de usuario planificado para FreeCAD.  Su objetivo es permitir pruebas
de la lógica de selección de presets y generación de modelos durante el
Sprint 3 sin requerir un entorno gráfico.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

from models import DataManager, FerruleGenerator, GasketGenerator


@dataclass
class TriptaFittingsDialog:
    """Diálogo lógico para seleccionar y generar componentes.

    Parameters
    ----------
    data_manager:
        Gestor de datos desde el cual se obtienen los presets disponibles.
    """

    data_manager: DataManager
    component: Optional[str] = None
    size: Optional[float] = None
    _current_preset: Optional[Any] = field(default=None, init=False)
    last_message: str = field(default="", init=False)

    def __post_init__(self) -> None:
        self.data_manager.load_all_data()

    # ------------------------------------------------------------------
    # Selección de componente y tamaño
    # ------------------------------------------------------------------
    def set_component(self, component: str) -> None:
        component = component.lower()
        if component not in ("ferrule", "gasket"):
            raise ValueError("Componente inválido")
        self.component = component
        self.size = None
        self._current_preset = None

    def get_available_components(self) -> List[str]:
        return ["ferrule", "gasket"]

    def get_available_sizes(self) -> List[float]:
        if not self.component:
            raise ValueError("Debe seleccionar un componente primero")
        return self.data_manager.get_available_sizes(self.component)

    def set_size(self, size: float) -> None:
        if not self.component:
            raise ValueError("Seleccione un componente antes del tamaño")
        available = self.get_available_sizes()
        if size not in available:
            raise ValueError("Tamaño inválido")
        self.size = size
        self._current_preset = self.data_manager.get_preset_by_size(
            self.component, size
        )

    # ------------------------------------------------------------------
    # Visualización de parámetros
    # ------------------------------------------------------------------
    def get_current_dn(self) -> Optional[str]:
        return getattr(self._current_preset, "dn", None)

    def get_current_parameters(self) -> Dict[str, Any]:
        if not self._current_preset:
            return {}
        return self._current_preset.get_parameters_dict()

    # ------------------------------------------------------------------
    # Generación de modelos
    # ------------------------------------------------------------------
    def generate_model(self) -> Dict[str, Any]:
        if not self._current_preset:
            raise ValueError("Debe seleccionar componente y tamaño válidos")
        if self.component == "ferrule":
            generator = FerruleGenerator(self._current_preset)
        else:
            generator = GasketGenerator(self._current_preset)

        geometry = generator.generate_geometry()
        self.last_message = "Model generated"
        return geometry

