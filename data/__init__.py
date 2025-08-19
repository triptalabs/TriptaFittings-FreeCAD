# -*- coding: utf-8 -*-
"""
Módulo de datos para TriptaFittings
Contiene las clases para manejo de presets y datos CSV
"""

from .preset import Preset
from .csv_loader import CSVLoader

__all__ = [
    'Preset',
    'CSVLoader'
]
