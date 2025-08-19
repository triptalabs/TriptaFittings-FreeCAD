# -*- coding: utf-8 -*-
"""Generador simple de modelos de Ferrule.

Este módulo implementa un generador mínimo que transforma un ``Preset``
en una representación de geometría basada en diccionarios.  El objetivo
es proveer una interfaz similar a la que utilizará FreeCAD en versiones
futuras del proyecto, permitiendo validar el flujo de datos durante el
Sprint 2 sin depender de FreeCAD.
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


class FerruleGenerator:
    """Generador de modelos de Ferrule basado en ``Preset``."""

    def __init__(self, preset: Preset) -> None:
        if preset.component_type != "ferrule":
            raise ValueError("FerruleGenerator requiere un preset de tipo 'ferrule'")
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
        }

    def update_spreadsheet(self, spreadsheet: Dict[str, Any]) -> None:
        """Actualiza una estructura tipo *spreadsheet* con los parámetros.

        La función recibe cualquier objeto semejante a un diccionario y
        actualiza/añade los parámetros del ``Preset``.
        """
        spreadsheet.update(self.preset.get_parameters_dict())
