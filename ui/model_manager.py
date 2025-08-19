# -*- coding: utf-8 -*-
"""Gestor sencillo de modelos generados.

Este módulo mantiene un registro en memoria de los modelos generados
 durante una sesión.  Permite listarlos, eliminarlos individualmente o
 limpiar grupos completos según su tipo de componente.
"""
from __future__ import annotations

from typing import Dict, List, Any, Optional


class ModelManager:
    """Gestiona los modelos generados en una sesión."""

    def __init__(self) -> None:
        # Diccionario indexado por nombre de modelo
        self._models: Dict[str, Dict[str, Any]] = {}

    def add_model(self, model: Dict[str, Any]) -> str:
        """Agrega un modelo al gestor.

        Parameters
        ----------
        model: Dict[str, Any]
            Estructura que representa al modelo.  Debe contener las claves
            ``name`` y ``component``.

        Returns
        -------
        str
            Nombre con el que se almacenó el modelo.
        """
        name = model.get("name")
        if not name:
            raise ValueError("El modelo debe contener un nombre")
        if "component" not in model:
            raise ValueError("El modelo debe indicar su componente")
        self._models[name] = model
        return name

    def list_models(self, component: Optional[str] = None) -> List[Dict[str, Any]]:
        """Lista los modelos almacenados.

        Parameters
        ----------
        component: Optional[str]
            Filtra por tipo de componente (ej. ``"ferrule"`` o ``"gasket"``).
        """
        if component is None:
            return list(self._models.values())
        return [m for m in self._models.values() if m.get("component") == component]

    def remove_model(self, name: str) -> bool:
        """Elimina un modelo por nombre.

        Returns
        -------
        bool
            ``True`` si el modelo existía y fue eliminado.
        """
        return self._models.pop(name, None) is not None

    def clear(self, component: Optional[str] = None) -> None:
        """Elimina todos los modelos o solo los de cierto componente."""
        if component is None:
            self._models.clear()
        else:
            to_delete = [k for k, v in self._models.items() if v.get("component") == component]
            for key in to_delete:
                del self._models[key]
