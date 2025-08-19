# -*- coding: utf-8 -*-
"""Interfaz de usuario simple para TriptaFittings.

Esta interfaz de texto permite a los usuarios consultar los presets
 disponibles y generar modelos mediante los generadores implementados en
 los sprints previos.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from models.data_manager import DataManager
from models.ferrule_generator import FerruleGenerator
from models.gasket_generator import GasketGenerator


class UserInterface:
    """Capa ligera para interactuar con el sistema.

    Encapsula a ``DataManager`` y expone métodos de alto nivel que pueden
    ser utilizados por una futura interfaz gráfica.  Esta implementación
    es intencionalmente mínima para validar el flujo de trabajo del
    **Sprint 3** sin depender de FreeCAD.
    """

    def __init__(self, data_directory: Optional[str] = None) -> None:
        self._manager = DataManager(data_directory)
        # Cargar todos los datos al inicializar la interfaz.
        self._manager.load_all_data()

    def list_available_sizes(self, component: str | None = None) -> List[float]:
        """Retorna los tamaños disponibles para el componente indicado."""
        return self._manager.get_available_sizes(component)

    def list_available_dns(self, component: str | None = None) -> List[str]:
        """Retorna los DN disponibles para el componente indicado."""
        return self._manager.get_available_dns(component)

    def generate_model(self, component: str, size: float) -> Dict[str, Any]:
        """Genera la geometría para un tamaño y componente específicos.

        Parameters
        ----------
        component:
            ``"ferrule"`` o ``"gasket"``.
        size:
            Tamaño del preset en pulgadas.
        Returns
        -------
        Dict[str, Any]
            Representación simplificada del modelo.
        Raises
        ------
        ValueError
            Si el componente es inválido o el tamaño no existe.
        """
        preset = self._manager.get_preset_by_size(component, size)
        if preset is None:
            raise ValueError(
                f"No se encontró preset para {component} con tamaño {size}"
            )

        kind = component.lower()
        if kind == "ferrule":
            generator = FerruleGenerator(preset)
        elif kind == "gasket":
            generator = GasketGenerator(preset)
        else:  # pragma: no cover - validación redundante
            raise ValueError(f"Tipo de componente inválido: {component}")

        return generator.generate_geometry()
