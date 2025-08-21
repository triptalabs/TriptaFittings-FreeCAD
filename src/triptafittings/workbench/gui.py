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

# Ruta al ícono principal del workbench (relativa al directorio del plugin)
PLUGIN_ROOT = os.path.join(MODULE_DIR, "..", "..", "..")
WB_ICON = os.path.join(PLUGIN_ROOT, "resources", "icons", "triptafittings.svg")

# Comandos que se mostrarán tanto en la toolbar como en el menú
TOOLBAR_COMMANDS: List[str] = [
    "Tripta_OpenDialog",
    "Tripta_CreateFerrule", 
    "Tripta_CreateGasket",
]


def list_toolbar_commands() -> List[str]:
    """Retorna la lista de comandos disponibles para la toolbar."""
    return list(TOOLBAR_COMMANDS)


def get_command_icon(command_name: str) -> str:
    """Retorna la ruta del icono específico para un comando."""
    icon_mapping = {
        "Tripta_OpenDialog": "open_dialog.svg",
        "Tripta_CreateFerrule": "create_ferrule.svg",
        "Tripta_CreateGasket": "create_gasket.svg",
    }
    
    icon_filename = icon_mapping.get(command_name, "triptafittings.svg")
    return os.path.join(PLUGIN_ROOT, "resources", "icons", icon_filename)
