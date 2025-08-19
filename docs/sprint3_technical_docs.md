# Sprint 3: Interfaz de Usuario - Documentación Técnica

## 📋 Resumen Ejecutivo
El **Sprint 3** introduce un diálogo lógico (`TriptaFittingsDialog`) que
permite seleccionar componentes y tamaños para generar modelos a partir
de los presets disponibles.  Esta implementación evita dependencias
gráficas para facilitar las pruebas automáticas y preparar la futura
integración con FreeCAD.

## 🏗️ Componentes Implementados

### `ui/tripta_fittings_dialog.py`
- Clase ``TriptaFittingsDialog`` basada en ``DataManager``.
- Métodos para seleccionar componente y tamaño, mostrar parámetros y
  generar el modelo correspondiente.
- Manejo básico de mensajes de estado mediante ``last_message``.

## 🔧 Ejemplo de Uso
```python
from models import DataManager
from ui import TriptaFittingsDialog

dm = DataManager()
dialog = TriptaFittingsDialog(dm)
dialog.set_component('ferrule')
dialog.set_size(3.0)
geometry = dialog.generate_model()
```

## 🧪 Tests
- ``tests/test_tripta_dialog.py``

Los tests cubren la selección de componentes, la actualización de
parámetros y la generación de modelos para Ferrule y Gasket.

## 🔮 Próximos Pasos
- Integrar la clase con una interfaz gráfica basada en PySide/FreeCAD.
- Permitir edición directa de parámetros en la UI.
- Añadir validaciones visuales en tiempo real.

---
**Documento generado:** 18 de Agosto 2025

