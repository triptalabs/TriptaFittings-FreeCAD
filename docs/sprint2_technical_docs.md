# Sprint 2: Generadores de Modelos - Documentación Técnica

## 📋 Resumen Ejecutivo
El **Sprint 2** introduce los generadores de modelos para los componentes
*Ferrule* y *Gasket*.  Estos generadores transforman los parámetros
almacenados en `Preset` en estructuras de datos listas para su futura
integración con FreeCAD.

## 🏗️ Componentes Implementados

### `models/ferrule_generator.py`
- Clase ``FerruleGenerator``
- Método ``generate_geometry`` devuelve un diccionario con el nombre del
  modelo y sus parámetros.
- Método ``update_spreadsheet`` actualiza un objeto tipo diccionario con
  los parámetros del preset.

### `models/gasket_generator.py`
- Clase ``GasketGenerator`` con la misma interfaz que el generador de
  ferrules, adaptada a los parámetros de juntas.

## 🔧 Ejemplo de Uso
```python
from data.preset import Preset
from models.ferrule_generator import FerruleGenerator

preset = Preset('ferrule', {...})
model = FerruleGenerator(preset)
geometry = model.generate_geometry()
```

## 🧪 Tests
- ``tests/test_ferrule_generator.py``
- ``tests/test_gasket_generator.py``

Los tests validan la generación de geometría, la actualización de
spreadsheets y la validación del tipo de preset.

## 🔮 Próximos Pasos
- Integrar los generadores con archivos ``.FCStd`` reales de FreeCAD.
- Añadir tests de integración y validación directa dentro de FreeCAD.
- Automatizar la nomenclatura y almacenamiento de modelos generados.

---
**Documento generado:** 18 de Agosto 2025
