#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup script para TriptaFittings."""

from setuptools import setup, find_packages
from pathlib import Path

# Leer README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

# Leer versión desde el módulo
version = "0.1.1"

setup(
    name="triptafittings",
    version=version,
    description="Generador automático de modelos paramétricos de Ferrule y Gasket para FreeCAD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # Información del autor
    author="TriptaLabs",
    author_email="info@triptalabs.com",
    url="https://github.com/triptalabs/TriptaFittings-FreeCAD",
    
    # Configuración de paquetes
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    
    # Archivos de datos
    package_data={
        "triptafittings.data.presets": ["*.csv"],
        "": ["*.svg", "*.xml"],
    },
    
    # Metadatos del proyecto
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Manufacturing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering",
    ],
    
    # Requisitos
    python_requires=">=3.8",
    install_requires=[
        # Sin dependencias externas por ahora
    ],
    
    # Dependencias opcionales para desarrollo
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
    },
    
    # Scripts de línea de comandos
    entry_points={
        "console_scripts": [
            "triptafittings-test=tools.run_tests:main",
            "triptafittings-diagnose=tools.diagnose_plugin:main",
        ],
    },
    
    # Información adicional
    keywords="freecad, cad, parametric, modeling, piping, fittings, ferrule, gasket",
    license="MIT",
    zip_safe=False,
)
