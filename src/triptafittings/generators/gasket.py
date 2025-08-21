# -*- coding: utf-8 -*-
"""Generador simple de modelos de Gasket.

Proporciona una implementación mínima para transformar un ``Preset`` de
tipo gasket en una estructura de datos que represente la geometría.  Se
utiliza durante el Sprint 2 para validar el flujo sin requerir FreeCAD.
"""
from __future__ import annotations

from typing import Dict, Any

try:
    from ..data.preset import Preset
except ImportError:  # pragma: no cover - soporte para ejecución directa
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from data.preset import Preset


class GasketGenerator:
    """Generador de modelos de Gasket basado en ``Preset``."""

    def __init__(self, preset: Preset) -> None:
        if preset.component_type != "gasket":
            raise ValueError("GasketGenerator requiere un preset de tipo 'gasket'")
        self.preset = preset

    def generate_geometry(self) -> Dict[str, Any]:
        """Genera una representación simplificada de la geometría.

        Returns
        -------
        Dict[str, Any]
            Diccionario con nombre y parámetros del modelo.
        """
        return {
            "name": self.preset.get_name(),
            "parameters": self.preset.get_parameters_dict(),
            "component": "gasket",
        }

    def update_spreadsheet(self, spreadsheet: Dict[str, Any]) -> None:
        """Actualiza una estructura tipo *spreadsheet* con los parámetros."""
        spreadsheet.update(self.preset.get_parameters_dict())
