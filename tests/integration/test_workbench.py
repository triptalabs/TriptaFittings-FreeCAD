# -*- coding: utf-8 -*-
"""Tests para la integración del workbench del Sprint 4."""
import os
import sys

# Asegurar que la ruta raíz esté en ``sys.path`` para las importaciones
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..', 'src'))

from src.triptafittings.workbench.init_gui import TriptaFittingsWorkbench
from src.triptafittings.workbench import commands as TriptaFittingsCmd
from src.triptafittings.workbench import gui as TriptaFittingsGui


def test_workbench_initialization():
    wb = TriptaFittingsWorkbench()
    cmds = wb.Initialize()
    assert "Tripta_CreateFerrule" in cmds
    assert "Tripta_CreateGasket" in cmds
    assert wb.Icon == TriptaFittingsGui.WB_ICON
    assert wb.GetClassName() == "Gui::PythonWorkbench"


def test_commands_resources_and_activation():
    ferrule_cmd = TriptaFittingsCmd.COMMANDS["Tripta_CreateFerrule"]
    gasket_cmd = TriptaFittingsCmd.COMMANDS["Tripta_CreateGasket"]

    # Verificar recursos de los comandos
    res_f = ferrule_cmd.GetResources()
    res_g = gasket_cmd.GetResources()
    for res in (res_f, res_g):
        assert os.path.exists(res["Pixmap"])
        assert "MenuText" in res and "ToolTip" in res

    # Activar comando y comprobar modelo generado
    model = ferrule_cmd.Activated()
    assert model["name"] == "Ferrule_3.0in_DN80"
    model = gasket_cmd.Activated()
    assert model["name"] == "Gasket_3.0in_DN80"


def test_gui_module_lists_commands_and_icon():
    assert TriptaFittingsGui.WB_ICON.endswith(".svg")
    assert os.path.exists(TriptaFittingsGui.WB_ICON)
    toolbar_cmds = TriptaFittingsGui.list_toolbar_commands()
    assert toolbar_cmds == ["Tripta_CreateFerrule", "Tripta_CreateGasket"]
