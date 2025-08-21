# -*- coding: utf-8 -*-
"""Definición de comandos para el workbench TriptaFittings.

Los comandos siguen la estructura habitual de FreeCAD e integran
la nueva interfaz gráfica TriptaFittingsDialog para el issue #10.
"""
from __future__ import annotations

from typing import Dict, Any

try:
    from ..ui.dialog import TriptaFittingsDialog, show_triptafittings_dialog
    from ..ui.interface import UserInterface
except ImportError:
    # Fallback para cuando ui no está disponible
    class TriptaFittingsDialog:
        def __init__(self, parent=None):
            pass
        def exec_(self):
            return True
        def get_generated_models(self):
            return []
    
    def show_triptafittings_dialog(parent=None):
        return TriptaFittingsDialog(parent)
    
    class UserInterface:
        def __init__(self):
            pass
        def generate_model(self, component, size):
            return {"name": f"{component}_{size}in", "status": "demo"}

from .gui import WB_ICON


class _BaseCreateCommand:
    """Comando base que abre el diálogo de TriptaFittings."""

    def __init__(self, component: str) -> None:
        self.component = component
        self.ui = UserInterface()

    # Métodos esperados por FreeCAD
    def Activated(self) -> Dict[str, Any]:
        """Abre el diálogo de TriptaFittings con el componente preseleccionado."""
        try:
            # Obtener ventana padre de FreeCAD si está disponible
            parent = None
            try:
                import FreeCADGui as Gui
                parent = Gui.getMainWindow()
            except ImportError:
                pass
            
            # Crear y mostrar diálogo
            dialog = show_triptafittings_dialog(parent)
            
            # Preseleccionar el componente correspondiente
            if hasattr(dialog, 'component_combo'):
                component_name = self.component.capitalize()
                index = dialog.component_combo.findText(component_name)
                if index >= 0:
                    dialog.component_combo.setCurrentIndex(index)
            
            # Mostrar diálogo
            result = dialog.exec_()
            
            if result:
                # Obtener modelos generados
                models = dialog.get_generated_models()
                return {
                    "status": "success",
                    "component": self.component,
                    "models_generated": len(models),
                    "models": models
                }
            else:
                return {
                    "status": "cancelled",
                    "component": self.component,
                    "models_generated": 0
                }
        
        except Exception as e:
            # Fallback a generación simple si falla el diálogo
            print(f"Error en diálogo, usando fallback: {e}")
            return self.ui.generate_model(self.component, 3.0)

    def GetResources(self) -> Dict[str, str]:
        """Recursos gráficos y metadatos del comando."""
        name = self.component.capitalize()
        return {
            "MenuText": f"Create {name}",
            "ToolTip": f"Abre el diálogo para generar un modelo de {name}",
            "Pixmap": WB_ICON,
        }


class CreateFerruleCommand(_BaseCreateCommand):
    def __init__(self) -> None:
        super().__init__("ferrule")


class CreateGasketCommand(_BaseCreateCommand):
    def __init__(self) -> None:
        super().__init__("gasket")


class OpenTriptaFittingsDialogCommand:
    """Comando para abrir el diálogo principal sin preselección."""
    
    def Activated(self) -> Dict[str, Any]:
        """Abre el diálogo principal de TriptaFittings."""
        try:
            # Obtener ventana padre de FreeCAD si está disponible
            parent = None
            try:
                import FreeCADGui as Gui
                parent = Gui.getMainWindow()
            except ImportError:
                pass
            
            # Crear y mostrar diálogo
            dialog = show_triptafittings_dialog(parent)
            result = dialog.exec_()
            
            if result:
                models = dialog.get_generated_models()
                return {
                    "status": "success",
                    "models_generated": len(models),
                    "models": models
                }
            else:
                return {"status": "cancelled", "models_generated": 0}
        
        except Exception as e:
            print(f"Error al abrir diálogo TriptaFittings: {e}")
            return {"status": "error", "error": str(e)}
    
    def GetResources(self) -> Dict[str, str]:
        """Recursos gráficos y metadatos del comando."""
        return {
            "MenuText": "TriptaFittings Generator",
            "ToolTip": "Abre el generador principal de TriptaFittings",
            "Pixmap": WB_ICON,
        }


COMMANDS = {
    "Tripta_OpenDialog": OpenTriptaFittingsDialogCommand(),
    "Tripta_CreateFerrule": CreateFerruleCommand(),
    "Tripta_CreateGasket": CreateGasketCommand(),
}
