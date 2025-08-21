# -*- coding: utf-8 -*-
"""Definición de comandos para el workbench TriptaFittings.

Los comandos siguen la estructura habitual de FreeCAD, pero se
implementan de manera simplificada para permitir su prueba sin la
presencia del propio FreeCAD.
"""
from __future__ import annotations

from typing import Dict, Any

try:
    from ..ui.interface import UserInterface
except ImportError:
    # Fallback para cuando ui no está disponible
    class UserInterface:
        def __init__(self):
            pass
        def generate_model(self, component, size):
            return {"name": f"{component}_{size}in", "status": "demo"}
from .gui import WB_ICON


class _BaseCreateCommand:
    """Comando base que genera un modelo usando :class:`UserInterface`."""

    def __init__(self, component: str) -> None:
        self.component = component
        self.ui = UserInterface()

    # Métodos esperados por FreeCAD
    def Activated(self) -> Dict[str, Any]:  # pragma: no cover - simple wrapper
        """Ejecuta la generación del modelo con un tamaño de ejemplo."""
        # Para propósitos de prueba utilizamos un tamaño fijo de 3.0"
        return self.ui.generate_model(self.component, 3.0)

    def GetResources(self) -> Dict[str, str]:
        """Recursos gráficos y metadatos del comando."""
        name = self.component.capitalize()
        return {
            "MenuText": f"Create {name}",
            "ToolTip": f"Genera un modelo de {name}",
            "Pixmap": WB_ICON,
        }


class CreateFerruleCommand(_BaseCreateCommand):
    def __init__(self) -> None:
        super().__init__("ferrule")


class CreateGasketCommand(_BaseCreateCommand):
    def __init__(self) -> None:
        super().__init__("gasket")


COMMANDS = {
    "Tripta_CreateFerrule": CreateFerruleCommand(),
    "Tripta_CreateGasket": CreateGasketCommand(),
}
