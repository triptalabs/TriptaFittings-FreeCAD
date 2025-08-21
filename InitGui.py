# -*- coding: utf-8 -*-
"""Punto de entrada para FreeCAD - InitGui.py

Este archivo es requerido por FreeCAD para registrar el workbench.
"""

# Import del workbench desde la nueva estructura
from src.triptafittings.workbench.init_gui import TriptaFittingsWorkbench

# Compatibilidad con versiones anteriores
try:
    import FreeCADGui as Gui
    Gui.addWorkbench(TriptaFittingsWorkbench())
except ImportError:
    # FreeCAD no está disponible (modo testing)
    pass
