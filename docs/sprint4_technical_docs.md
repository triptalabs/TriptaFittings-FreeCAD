# Sprint 4: Integración con FreeCAD Workbench - Documentación Técnica

## 📋 Resumen Ejecutivo
El **Sprint 4** introduce la estructura necesaria para que el plugin se
comporte como un *workbench* de FreeCAD.  Aunque las pruebas se
realizan en un entorno aislado sin FreeCAD, los módulos creados siguen
la misma interfaz que utilizaría la aplicación real.

## 🏗️ Componentes Implementados

### `TriptaFittingsGui.py`
- Define la ruta del ícono principal del workbench.
- Expone la lista de comandos que se añaden a la toolbar y al menú.

### `TriptaFittingsCmd.py`
- Implementa los comandos ``CreateFerrule`` y ``CreateGasket``.
- Cada comando utiliza la ``UserInterface`` para generar un modelo de
  ejemplo con tamaño ``3.0"``.
- Provee metadatos mediante ``GetResources`` compatibles con FreeCAD.

### `InitGui.py`
- Define la clase ``TriptaFittingsWorkbench`` que FreeCAD utilizaría
  para registrar el workbench.
- El método ``Initialize`` registra los comandos y prepara las listas de
  toolbar y menú.
- Incluye métodos ``Activated`` y ``Deactivated`` como stubs.

### `resources/triptafittings.svg`
- Ícono vectorial utilizado tanto por el workbench como por los
  comandos.

## 🔧 Ejemplo de Uso
```python
from InitGui import TriptaFittingsWorkbench
wb = TriptaFittingsWorkbench()
commands = wb.Initialize()
print(commands)  # ['Tripta_CreateFerrule', 'Tripta_CreateGasket']
```

## 🧪 Tests
- ``tests/test_workbench.py`` valida la inicialización del workbench,
  la existencia de los comandos y la generación de modelos de ejemplo.

## 🔮 Próximos Pasos
- Integrar con la API real de FreeCAD y registrar los comandos mediante
  ``Gui.addCommand``.
- Añadir menús contextuales sobre objetos dentro del árbol de FreeCAD.
- Preparar empaquetado para distribución vía Addon Manager.

---
**Documento generado:** 18 de Agosto 2025
