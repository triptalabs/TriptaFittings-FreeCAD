# -*- coding: utf-8 -*-
"""Tests para el diálogo lógico de Sprint 3."""

import pytest

from models import DataManager
from ui import TriptaFittingsDialog


@pytest.fixture(scope="module")
def dialog() -> TriptaFittingsDialog:
    dm = DataManager()
    return TriptaFittingsDialog(dm)


def test_component_and_size_selection(dialog):
    dialog.set_component("ferrule")
    sizes = dialog.get_available_sizes()
    assert 1.5 in sizes
    dialog.set_size(1.5)
    params = dialog.get_current_parameters()
    assert params["Size"] == 1.5
    assert dialog.get_current_dn().startswith("DN")


def test_generate_model_gasket(dialog):
    dialog.set_component("gasket")
    dialog.set_size(2.0)
    geometry = dialog.generate_model()
    assert geometry["name"].startswith("Gasket")
    assert geometry["parameters"]["Size"] == 2.0


def test_invalid_component(dialog):
    with pytest.raises(ValueError):
        dialog.set_component("valvula")


def test_invalid_size(dialog):
    dialog.set_component("ferrule")
    with pytest.raises(ValueError):
        dialog.set_size(99.0)


def test_parameters_change_with_size(dialog):
    dialog.set_component("ferrule")
    dialog.set_size(1.5)
    params_small = dialog.get_current_parameters()
    dialog.set_size(3.0)
    params_large = dialog.get_current_parameters()
    assert params_small["FlangeOD_mm"] != params_large["FlangeOD_mm"]

