# Guía de Desarrollo - TriptaFittings

## 🏗️ Arquitectura del Proyecto

```
src/triptafittings/
├── workbench/          # Integración con FreeCAD
├── core/              # Lógica principal
├── generators/        # Generadores de modelos
├── data/             # Datos y presets
└── ui/               # Interfaz de usuario
```

## 🧪 Testing

### Ejecutar Tests
```bash
# Todos los tests
python tools/run_tests.py

# Solo tests unitarios
python -m pytest tests/unit/

# Solo tests de integración  
python -m pytest tests/integration/
```

### Estructura de Tests
```
tests/
├── unit/             # Tests unitarios
├── integration/      # Tests de integración
└── fixtures/         # Datos de prueba
```

## 🛠️ Herramientas de Desarrollo

### Scripts Útiles
```bash
# Diagnóstico del sistema
python tools/diagnose_plugin.py

# Activar plugin en FreeCAD
python tools/activate_plugin.py

# Instalar plugin
python tools/install_plugin.py
```

### Estilo de Código
- Seguir PEP 8
- Usar type hints
- Documentar con docstrings
- Tests para toda funcionalidad nueva

## 📦 Estructura de Módulos

### Core (`src/triptafittings/core/`)
- `data_manager.py` - Gestión de datos y presets
- `config.py` - Configuración del sistema
- `model_manager.py` - Gestión de modelos generados

### Generators (`src/triptafittings/generators/`)
- `ferrule.py` - Generador de férulas
- `gasket.py` - Generador de juntas

### Data (`src/triptafittings/data/`)
- `preset.py` - Clase para presets
- `csv_loader.py` - Cargador de datos CSV
- `presets/` - Archivos de datos

## 🔧 Agregar Nuevos Componentes

1. **Crear generador** en `src/triptafittings/generators/`
2. **Agregar presets** en `src/triptafittings/data/presets/`
3. **Escribir tests** en `tests/unit/` y `tests/integration/`
4. **Actualizar documentación**

## 🚀 Contribuir

1. Fork el repositorio
2. Crear rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📝 Convenciones

### Naming
- Archivos: `snake_case`
- Clases: `PascalCase`  
- Funciones/variables: `snake_case`
- Constantes: `UPPER_CASE`

### Imports
```python
# Imports relativos para módulos internos
from ..core.data_manager import DataManager
from .preset import Preset

# Imports absolutos para librerías externas
import os
import sys
from typing import List, Dict
```
