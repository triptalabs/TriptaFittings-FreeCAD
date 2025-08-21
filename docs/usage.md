# Guía de Uso - TriptaFittings

## 🎮 Uso Básico

### 1. Activar el Workbench
1. Abrir FreeCAD
2. Ir a **View → Workbenches → TriptaFittings**

### 2. Generar un Modelo
1. Seleccionar componente: **Ferrule** o **Gasket**
2. Elegir tamaño: 1.5", 2", 2.5", 3", 4", 6", 8", 10", 12"
3. Hacer clic en **"Generate Model"**

## 🛠️ Funciones Avanzadas

### Uso Programático

```python
from src.triptafittings.ui.interface import UserInterface

# Crear interfaz
ui = UserInterface()

# Listar tamaños disponibles
sizes = ui.list_available_sizes('ferrule')
print(f"Tamaños disponibles: {sizes}")

# Generar modelo
model = ui.generate_model('ferrule', 3.0)
print(f"Modelo generado: {model['name']}")
```

### Explorar Datos

```python
from src.triptafittings.core.data_manager import DataManager

# Crear gestor de datos
dm = DataManager()
dm.load_all_data()

# Obtener presets
ferrule_presets = dm.get_presets_by_type('ferrule')
gasket_presets = dm.get_presets_by_type('gasket')
```

## 📊 Parámetros Disponibles

### Ferrule (Férula)
- `PassageDia`: Diámetro del paso
- `TubeID`: Diámetro interior del tubo  
- `FlangeOD`: Diámetro exterior de la brida
- `C2`: Dimensión C2
- `SeatLipWidth`: Ancho del labio del asiento
- `HeightTube`: Altura del tubo
- `HeightProfile`: Altura del perfil

### Gasket (Junta)
- `GasketOD`: Diámetro exterior de la junta
- `GasketID`: Diámetro interior de la junta
- `ProfileH`: Altura del perfil
- `C2`: Dimensión C2
- `SeatLipWidth`: Ancho del labio del asiento

## 🎯 Ejemplos

Ver la carpeta [`examples/`](../examples/) para ejemplos completos:
- [`basic_usage.py`](../examples/basic_usage.py) - Uso básico
- [`interactive_demo.py`](../examples/interactive_demo.py) - Demo interactivo
- [`freecad_files/`](../examples/freecad_files/) - Archivos de ejemplo

## 📝 Estándares Soportados

- **DIN 32676 A**: Estándar alemán para conexiones de tubería
- **Tamaños**: 1.5" a 12" (DN40 a DN300)
- **Materiales**: Compatible con todos los materiales de FreeCAD
