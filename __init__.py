# -*- coding: utf-8 -*-
"""
TriptaFittings - Plugin para FreeCAD
Generador automático de modelos paramétricos de Ferrule y Gasket
Basado en estándares DIN 32676 A

Autor: TriptaLabs
Versión: 1.0.0
"""

__version__ = "1.0.0"
__author__ = "TriptaLabs"
__email__ = "info@triptalabs.com"
__url__ = "https://github.com/triptalabs/TriptaFittings-FreeCAD"
__license__ = "MIT"

# Importaciones principales
try:
    import FreeCAD
    import FreeCADGui
    import Part
    import Spreadsheet
except ImportError as e:
    print(f"Error al importar módulos de FreeCAD: {e}")

# Importaciones del plugin
from . import models
from . import data

def get_version():
    """Retorna la versión actual del plugin"""
    return __version__

def get_author():
    """Retorna el autor del plugin"""
    return __author__

def get_description():
    """Retorna la descripción del plugin"""
    return "Generador automático de modelos paramétricos de Ferrule y Gasket para FreeCAD"
