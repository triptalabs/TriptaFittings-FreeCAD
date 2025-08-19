# -*- coding: utf-8 -*-
"""Tests para la gestión de modelos generados (Sprint 5)."""
import os
import sys

# Añadir ruta raíz para importaciones
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ui.user_interface import UserInterface


def test_model_management_flow():
    ui = UserInterface()

    ferrule = ui.generate_model('ferrule', 3.0)
    gasket = ui.generate_model('gasket', 3.0)

    # Listar todos los modelos
    all_models = ui.list_generated_models()
    assert len(all_models) == 2

    # Filtrar por componente
    only_ferrules = ui.list_generated_models('ferrule')
    assert [m['name'] for m in only_ferrules] == [ferrule['name']]

    # Eliminar por nombre
    assert ui.remove_model(ferrule['name']) is True
    remaining = ui.list_generated_models()
    assert len(remaining) == 1 and remaining[0]['name'] == gasket['name']

    # Limpiar todos los modelos
    ui.clear_models()
    assert ui.list_generated_models() == []
