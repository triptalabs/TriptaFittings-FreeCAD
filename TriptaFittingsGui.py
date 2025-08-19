# -*- coding: utf-8 -*-
"""Utilidades gráficas para el workbench de TriptaFittings.

Este módulo centraliza rutas de recursos e información relacionada
con la interfaz gráfica.  Está diseñado para operar incluso en
entornos donde FreeCAD no está disponible, lo que permite ejecutar
las pruebas unitarias en un entorno puro de Python.
"""
from __future__ import annotations

import os
from typing import List

# Directorio base del módulo (raíz del paquete)
MODULE_DIR = os.path.dirname(__file__)

# Ruta al ícono principal del workbench
WB_ICON = os.path.join(MODULE_DIR, "resources", "triptafittings.svg")

# Comandos que se mostrarán tanto en la toolbar como en el menú
TOOLBAR_COMMANDS: List[str] = [
    "Tripta_CreateFerrule",
    "Tripta_CreateGasket",
]


def list_toolbar_commands() -> List[str]:
    """Retorna la lista de comandos disponibles para la toolbar."""
    return list(TOOLBAR_COMMANDS)
