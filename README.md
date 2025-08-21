# TriptaFittings - Plugin para FreeCAD

[![FreeCAD](https://img.shields.io/badge/FreeCAD-0.20+-blue.svg)](https://www.freecad.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Generador automático de modelos paramétricos de **Ferrule (Férula)** y **Gasket (Junta)** para FreeCAD, basado en estándares **DIN 32676 A**.

## 🎯 Características

- ✅ **Generación automática** de modelos 3D paramétricos
- ✅ **Presets estándar** DIN 32676 A (1.5" a 12")
- ✅ **Interfaz intuitiva** para selección de tamaños
- ✅ **Integración nativa** con FreeCAD
- ✅ **Spreadsheets automáticas** con parámetros
- ✅ **Exportación** a formatos estándar (STEP, IGES, STL)
- ✅ **Gestión básica** de modelos generados en sesión

## 📋 Requisitos

- **FreeCAD**: Versión 0.20 o superior
- **Python**: Versión 3.8 o superior
- **Sistema Operativo**: Windows, macOS, Linux

## 🚀 Instalación

### Inicio Rápido

1. **Clonar el repositorio**:
```bash
git clone https://github.com/triptalabs/TriptaFittings-FreeCAD.git
cd TriptaFittings-FreeCAD
```

2. **Probar el sistema**:
```bash
python tools/run_tests.py
```

3. **Instalar FreeCAD** (opcional para funcionalidades completas):
   - Ver [Guía de Instalación de FreeCAD](docs/installation/install_freecad_windows.md)

### Método 1: Addon Manager (Recomendado)

1. Abrir FreeCAD
2. Ir a **Tools → Addon Manager**
3. Buscar "TriptaFittings"
4. Hacer clic en **Install**

### Método 2: Instalación Manual

1. Descargar el repositorio:
```bash
git clone https://github.com/triptalabs/TriptaFittings-FreeCAD.git
```

2. Copiar la carpeta `TriptaFittings` a:
   - **Windows**: `%APPDATA%\FreeCAD\Mod\`
   - **macOS**: `~/Library/Application Support/FreeCAD/Mod/`
   - **Linux**: `~/.FreeCAD/Mod/`

3. Reiniciar FreeCAD

### Documentación Completa

- **[Guía de Instalación](docs/installation/install_guide.md)**: Instrucciones detalladas
- **[Instalación de FreeCAD](docs/installation/install_freecad_windows.md)**: Guía específica para Windows
- **[Documentación General](docs/README.md)**: Índice completo de documentación

## 🎮 Uso

### Pruebas y Demos

```bash
# Ejecutar todas las pruebas
python tools/run_tests.py

# Demo automático de funcionalidades
python examples/basic_usage.py

# Demo interactivo
python examples/interactive_demo.py

# Diagnóstico del sistema
python tools/diagnose_plugin.py
```

### Generar un Modelo (FreeCAD)

1. **Activar el Workbench**: View → Workbenches → TriptaFittings
2. **Seleccionar Componente**: Ferrule o Gasket
3. **Elegir Tamaño**: 1.5", 2", 2.5", 3", 4", 6", 8", 10", 12"
4. **Hacer clic en "Generate Model"**

### Explorar Datos

```python
from src.triptafittings.core.data_manager import DataManager

# Crear gestor de datos
dm = DataManager()
dm.load_all_data()

# Obtener tamaños disponibles
sizes = dm.get_available_sizes()
print(f"Tamaños: {sizes}")

# Obtener presets
ferrule_presets = dm.get_presets_by_type('ferrule')
gasket_presets = dm.get_presets_by_type('gasket')
```

### Parámetros Disponibles

#### Ferrule (Férula)
- `PassageDia`: Diámetro del paso
- `TubeID`: Diámetro interior del tubo
- `FlangeOD`: Diámetro exterior de la brida
- `C2`: Dimensión C2
- `SeatLipWidth`: Ancho del labio del asiento
- `HeightTube`: Altura del tubo
- `HeightProfile`: Altura del perfil

#### Gasket (Junta)
- `GasketOD`: Diámetro exterior de la junta
- `GasketID`: Diámetro interior de la junta
- `ProfileH`: Altura del perfil
- `C2`: Dimensión C2
- `SeatLipWidth`: Ancho del labio del asiento

## 📊 Estándares Soportados

- **DIN 32676 A**: Estándar alemán para conexiones de tubería
- **Tamaños**: 1.5" a 12" (DN40 a DN300)
- **Materiales**: Compatible con todos los materiales de FreeCAD

## 🛠️ Desarrollo

### Estructura del Proyecto

```
TriptaFittings-FreeCAD/
├── 📁 src/                          # Código fuente principal
│   └── triptafittings/
│       ├── workbench/               # Workbench FreeCAD
│       │   ├── init_gui.py          # Inicialización del workbench
│       │   ├── commands.py          # Comandos
│       │   └── gui.py               # Interfaz gráfica
│       ├── core/                    # Lógica principal
│       │   ├── config.py            # Configuración
│       │   ├── data_manager.py      # Gestión de datos
│       │   └── model_manager.py     # Gestión de modelos
│       ├── generators/              # Generadores de modelos
│       │   ├── ferrule.py          # Generador de férulas
│       │   └── gasket.py           # Generador de juntas
│       ├── data/                    # Datos y presets
│       │   ├── preset.py
│       │   ├── csv_loader.py
│       │   └── presets/
│       │       ├── ferrule_din32676A_1p5_to_12in.csv
│       │       └── gasket_din32676A_1p5_to_12in.csv
│       └── ui/                      # Interfaz de usuario
│           └── interface.py         # Interfaz principal
├── 📁 tests/                        # Tests unificados
│   ├── unit/                        # Tests unitarios
│   ├── integration/                 # Tests de integración
│   └── fixtures/                    # Datos de prueba
├── 📁 examples/                     # Ejemplos y demos
│   ├── basic_usage.py
│   ├── interactive_demo.py
│   └── freecad_files/
├── 📁 docs/                         # Documentación organizada
│   ├── README.md                    # Índice de documentación
│   ├── installation.md             # Guía de instalación
│   ├── usage.md                     # Guía de uso
│   ├── development.md               # Guía de desarrollo
│   └── installation/                # Documentación detallada
├── 📁 tools/                        # Herramientas de desarrollo
│   ├── install_plugin.py
│   ├── run_tests.py
│   ├── diagnose_plugin.py
│   └── activate_plugin.py
├── 📁 resources/                    # Recursos del plugin
│   └── icons/
│       └── triptafittings.svg
├── 📄 __init__.py                   # Plugin principal
├── 📄 InitGui.py                    # Entrada para FreeCAD
├── 📄 package.xml                   # Metadatos del plugin
├── 📄 setup.py                      # Instalación con pip
├── 📄 README.md                     # Este archivo
└── 📄 LICENSE
```

### Contribuir

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 📖 Documentación

- **Issues**: [GitHub Issues](https://github.com/triptalabs/TriptaFittings-FreeCAD/issues)
- **Discusiones**: [GitHub Discussions](https://github.com/triptalabs/TriptaFittings-FreeCAD/discussions)
- **Email**: info@triptalabs.com

---

**Desarrollado con ❤️ por [TriptaLabs](https://triptalabs.com)**
