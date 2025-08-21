# -*- coding: utf-8 -*-
"""Inicialización del Workbench de TriptaFittings.

Este módulo define la clase ``TriptaFittingsWorkbench`` que FreeCAD
utilizaría para registrar el workbench.  Se implementa una versión
simplificada para permitir pruebas unitarias sin depender de la API
de FreeCAD.
"""
from __future__ import annotations

from typing import List

from TriptaFittingsGui import WB_ICON, list_toolbar_commands
from TriptaFittingsCmd import COMMANDS


class TriptaFittingsWorkbench:
    """Workbench mínimo compatible con la API de FreeCAD."""

    # Metadatos mostrados por FreeCAD
    MenuText = "TriptaFittings"
    ToolTip = "Generador de fittings sanitarios"
    Icon = WB_ICON

    def __init__(self) -> None:
        self.commands: List[str] = []
        self.toolbar: List[str] = []
        self.menu: List[str] = []

    def Initialize(self) -> List[str]:
        """Inicializa el workbench registrando los comandos disponibles."""
        self.commands = list(COMMANDS.keys())
        toolbar_cmds = list_toolbar_commands()
        self.toolbar.extend(toolbar_cmds)
        self.menu.extend(toolbar_cmds)
        # En FreeCAD se registrarían los comandos con Gui.addCommand
        return self.commands

    def Activated(self) -> None:  # pragma: no cover - comportamiento vacío
        """Se llama cuando el workbench se activa en FreeCAD."""
        return None

    def Deactivated(self) -> None:  # pragma: no cover - comportamiento vacío
        """Se llama cuando el workbench se desactiva."""
        return None

    def GetClassName(self) -> str:
        """Nombre de clase usado por FreeCAD para identificar el WB."""
        return "Gui::PythonWorkbench"


# Registrar el workbench con FreeCAD
try:
    import FreeCAD
    import FreeCADGui as Gui
    
    # Registrar el workbench
    Gui.addWorkbench(TriptaFittingsWorkbench())
    print("✅ TriptaFittings workbench registrado correctamente")
    
except ImportError:
    # FreeCAD no está disponible (para pruebas)
    pass
except Exception as e:
    print(f"❌ Error al registrar workbench: {e}")
