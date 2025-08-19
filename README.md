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

## 📋 Requisitos

- **FreeCAD**: Versión 0.20 o superior
- **Python**: Versión 3.8 o superior
- **Sistema Operativo**: Windows, macOS, Linux

## 🚀 Instalación

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

## 🎮 Uso

### Generar un Modelo

1. **Activar el Workbench**: View → Workbenches → TriptaFittings
2. **Seleccionar Componente**: Ferrule o Gasket
3. **Elegir Tamaño**: 1.5", 2", 2.5", 3", 4", 6", 8", 10", 12"
4. **Hacer clic en "Generate Model"**

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
├── __init__.py             # Plugin principal
├── InitGui.py              # Inicialización del workbench
├── TriptaFittingsGui.py    # Interfaz gráfica
├── TriptaFittingsCmd.py    # Comandos
├── models/                 # Generadores de modelos
│   ├── __init__.py
│   ├── data_manager.py
│   ├── ferrule_generator.py
│   └── gasket_generator.py
├── data/                   # Datos y presets
│   ├── __init__.py
│   ├── preset.py
│   ├── csv_loader.py
│   └── *.csv
├── resources/              # Recursos (iconos, etc.)
├── docs/                   # Documentación
├── FreeCADfiles/          # Archivos de ejemplo
├── tmp/                   # Archivos temporales (ignorado por git)
├── package.xml            # Metadatos del plugin
├── .gitignore            # Archivos ignorados por git
└── README.md
```

### Contribuir

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 🤝 Soporte

- **Issues**: [GitHub Issues](https://github.com/triptalabs/TriptaFittings-FreeCAD/issues)
- **Discusiones**: [GitHub Discussions](https://github.com/triptalabs/TriptaFittings-FreeCAD/discussions)
- **Email**: info@triptalabs.com

## 🙏 Agradecimientos

- **FreeCAD Community**: Por el excelente software base
- **DIN Standards**: Por los estándares industriales
- **Contribuidores**: Por sus valiosas contribuciones

---

**Desarrollado con ❤️ por [TriptaLabs](https://triptalabs.com)**
