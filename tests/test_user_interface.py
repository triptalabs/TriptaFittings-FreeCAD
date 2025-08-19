# -*- coding: utf-8 -*-
"""Tests para la interfaz de usuario del Sprint 3."""
import os
import sys

import pytest

# Añadir la ruta raíz para importaciones
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ui.user_interface import UserInterface


def test_listar_tamanos_y_dns():
    ui = UserInterface()
    tamanos = ui.list_available_sizes('ferrule')
    assert 1.5 in tamanos and 3.0 in tamanos
    dns = ui.list_available_dns('gasket')
    assert 'DN40' in dns and 'DN80' in dns


def test_generar_modelo_ferrule():
    ui = UserInterface()
    geometry = ui.generate_model('ferrule', 3.0)
    assert geometry['name'] == 'Ferrule_3.0in_DN80'
    params = geometry['parameters']
    assert params['Size'] == 3.0
    assert params['DN'] == 'DN80'


def test_generar_modelo_gasket():
    ui = UserInterface()
    geometry = ui.generate_model('gasket', 3.0)
    assert geometry['name'] == 'Gasket_3.0in_DN80'
    params = geometry['parameters']
    assert params['Size'] == 3.0
    assert params['DN'] == 'DN80'


def test_error_tamano_inexistente():
    ui = UserInterface()
    with pytest.raises(ValueError):
        ui.generate_model('ferrule', 999)

