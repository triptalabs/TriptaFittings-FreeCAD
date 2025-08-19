# Sprint 3: Interfaz de Usuario - Documentación Técnica

## 📋 Resumen Ejecutivo
El **Sprint 3** añade una capa de interacción sencilla que permite al
usuario explorar los presets disponibles y generar modelos a partir de
ellos.  Esta interfaz en modo texto sirve como base para una futura GUI
en FreeCAD.

## 🏗️ Componentes Implementados

### `ui/user_interface.py`
- Clase ``UserInterface`` que encapsula a ``DataManager``.
- Métodos para listar tamaños y DN disponibles.
- Método ``generate_model`` que invoca a ``FerruleGenerator`` o
  ``GasketGenerator`` según el componente solicitado.

## 🔧 Ejemplo de Uso
```python
from ui.user_interface import UserInterface

ui = UserInterface()
print(ui.list_available_sizes())      # [1.5, 2.0, ..., 12.0]
model = ui.generate_model('ferrule', 3.0)
print(model['name'])                  # 'Ferrule_3.0in_DN80'
```

## 🧪 Tests
- ``tests/test_user_interface.py`` valida la lista de tamaños y DN,
  así como la generación de modelos y el manejo de errores.

## 🔮 Próximos Pasos
- Reemplazar esta interfaz de texto por diálogos de FreeCAD.
- Añadir controles gráficos para selección de parámetros.
- Integrar con un ``Workbench`` dedicado.

---
**Documento generado**: 18 de Agosto 2025
