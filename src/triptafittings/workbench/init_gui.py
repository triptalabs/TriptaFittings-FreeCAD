# -*- coding: utf-8 -*-
"""Inicialización del Workbench de TriptaFittings.

Este módulo define la clase ``TriptaFittingsWorkbench`` que se integra
completamente con FreeCAD, incluyendo toolbar, menús y comandos funcionales.
Versión corregida para FreeCAD 1.0+
"""
from __future__ import annotations

import os
from typing import List

from .gui import WB_ICON, list_toolbar_commands
from .commands import COMMANDS

# Importar Gui.Workbench si está disponible
try:
    import FreeCADGui as Gui
    # Verificar si Workbench está disponible
    if hasattr(Gui, 'Workbench'):
        WorkbenchBase = Gui.Workbench
    else:
        # Crear una clase base simple para modo consola
        class WorkbenchBase:
            def __init__(self):
                pass
            def Initialize(self):
                pass
            def Activated(self):
                pass
            def Deactivated(self):
                pass
            def GetClassName(self):
                return "Gui::PythonWorkbench"
except ImportError:
    # Para testing sin FreeCAD
    class WorkbenchBase:
        def __init__(self):
            pass
        def Initialize(self):
            pass
        def Activated(self):
            pass
        def Deactivated(self):
            pass
        def GetClassName(self):
            return "Gui::PythonWorkbench"

class TriptaFittingsWorkbench(WorkbenchBase):
    """Workbench completamente integrado con FreeCAD."""

    # Metadatos mostrados por FreeCAD
    MenuText = "TriptaFittings"
    ToolTip = "Generador de fittings sanitarios DIN 32676 A"
    Icon = WB_ICON

    def __init__(self) -> None:
        self.commands: List[str] = []
        self.toolbar: List[str] = []
        self.menu: List[str] = []

    def Initialize(self) -> None:
        """Inicializa el workbench registrando comandos, toolbar y menús."""
        try:
            import FreeCADGui as Gui
            
            # Obtener lista de comandos para toolbar
            toolbar_cmds = list_toolbar_commands()
            self.commands = list(COMMANDS.keys())
            self.toolbar = toolbar_cmds
            self.menu = toolbar_cmds
            
            # Registrar todos los comandos con FreeCAD
            for cmd_name, cmd_obj in COMMANDS.items():
                Gui.addCommand(cmd_name, cmd_obj)
                print("Comando registrado:", cmd_name)
            
            print("Workbench TriptaFittings inicializado correctamente")
            
        except ImportError:
            # FreeCAD no está disponible (modo testing)
            toolbar_cmds = list_toolbar_commands()
            self.commands = list(COMMANDS.keys())
            self.toolbar = toolbar_cmds
            self.menu = toolbar_cmds
            print("Modo testing - workbench configurado")
        except Exception as e:
            print("Error al inicializar workbench:", str(e))

    def Activated(self) -> None:
        """Se llama cuando el workbench se activa en FreeCAD."""
        print("TriptaFittings workbench activado")

    def Deactivated(self) -> None:
        """Se llama cuando el workbench se desactiva."""
        print("TriptaFittings workbench desactivado")

    def GetClassName(self) -> str:
        """Nombre de clase usado por FreeCAD para identificar el WB."""
        return "Gui::PythonWorkbench"


# No registrar automáticamente aquí - se hace desde InitGui.py
