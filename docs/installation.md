# Guía de Instalación - TriptaFittings

Esta guía te ayudará a instalar TriptaFittings en tu sistema.

## 🚀 Instalación Rápida

### Opción 1: Addon Manager (Recomendado)
1. Abrir FreeCAD
2. Ir a **Tools → Addon Manager**
3. Buscar "TriptaFittings"
4. Hacer clic en **Install**

### Opción 2: Instalación Manual
```bash
# Clonar el repositorio
git clone https://github.com/triptalabs/TriptaFittings-FreeCAD.git

# Ejecutar script de instalación
cd TriptaFittings-FreeCAD
python tools/install_plugin.py
```

### Opción 3: Instalación desde Código Fuente
```bash
# Clonar y copiar manualmente
git clone https://github.com/triptalabs/TriptaFittings-FreeCAD.git
cd TriptaFittings-FreeCAD

# Copiar a directorio de FreeCAD
# Windows: %APPDATA%\FreeCAD\Mod\
# macOS: ~/Library/Application Support/FreeCAD/Mod/
# Linux: ~/.FreeCAD/Mod/
```

## 📋 Requisitos

- **FreeCAD**: Versión 0.20 o superior
- **Python**: Versión 3.8 o superior  
- **Sistema Operativo**: Windows, macOS, Linux

## ✅ Verificación

Para verificar que la instalación fue exitosa:

```bash
# Ejecutar diagnóstico
python tools/diagnose_plugin.py

# Ejecutar tests
python tools/run_tests.py
```

## 🔧 Resolución de Problemas

Ver [installation/install_guide.md](installation/install_guide.md) para instrucciones detalladas.

Para problemas específicos de Windows, consulta [installation/install_freecad_windows.md](installation/install_freecad_windows.md).
