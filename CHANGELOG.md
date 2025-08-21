# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2025-01-21

### 🗂️ Changed
- **Reorganización completa del proyecto** para mejor mantenibilidad y escalabilidad
- Reestructuración de directorios siguiendo convenciones estándar de Python
- Separación clara entre código fuente (`src/`), tests (`tests/`), ejemplos (`examples/`), herramientas (`tools/`) y documentación (`docs/`)
- Mejora en la organización de módulos y paquetes

### ✨ Added
- Nueva estructura de directorios más profesional y organizada:
  - `src/triptafittings/` - Código fuente principal
  - `tests/unit/` y `tests/integration/` - Tests organizados por tipo
  - `examples/` - Ejemplos y demos del plugin
  - `tools/` - Herramientas de desarrollo
  - `docs/` - Documentación unificada
- Script unificado de tests (`tools/run_tests.py`)
- Archivo `setup.py` para instalación con pip
- Documentación mejorada (`docs/installation.md`, `docs/usage.md`, `docs/development.md`)
- Archivo `.gitignore` actualizado

### 🔧 Fixed
- Imports actualizados para la nueva estructura
- Compatibilidad mejorada con FreeCAD
- Referencias corregidas en `package.xml`

### 📝 Technical Details
- Migración de archivos del workbench a `src/triptafittings/workbench/`
- Componentes core movidos a `src/triptafittings/core/`
- Generadores reorganizados en `src/triptafittings/generators/`
- Tests unificados y con imports corregidos
- Mantenimiento de compatibilidad hacia atrás con FreeCAD

## [0.1.0] - 2025-01-20

### ✨ Added
- Versión inicial del plugin TriptaFittings
- Generadores básicos para Ferrule y Gasket
- Integración inicial con FreeCAD
- Sistema de presets basado en estándares DIN 32676 A
- Tests unitarios básicos
- Documentación inicial
