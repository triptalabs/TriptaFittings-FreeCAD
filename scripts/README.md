# 📁 Scripts - TriptaFittings-FreeCAD

Esta carpeta contiene todos los scripts de prueba, demostración y utilidades del proyecto.

## 📂 Estructura

```
scripts/
├── README.md                 # Este archivo
├── run_all_tests.py         # Script principal para ejecutar todas las pruebas
├── testing/                 # Scripts de prueba y verificación
│   ├── test_basic.py        # Pruebas básicas del sistema
│   ├── test_freecad_integration.py  # Pruebas de integración con FreeCAD
│   └── check_freecad.py     # Verificación de instalación de FreeCAD
└── demos/                   # Scripts de demostración
    ├── demo_automatic.py    # Demo automático de funcionalidades
    └── demo_interactive.py  # Demo interactivo con menú
```

## 🚀 Uso Rápido

### Ejecutar todas las pruebas
```bash
python scripts/run_all_tests.py
```

### Pruebas individuales
```bash
# Pruebas básicas
python scripts/testing/test_basic.py

# Verificar FreeCAD
python scripts/testing/check_freecad.py

# Demo automático
python scripts/demos/demo_automatic.py

# Demo interactivo
python scripts/demos/demo_interactive.py
```

## 📋 Descripción de Scripts

### Scripts de Prueba (`testing/`)

#### `test_basic.py`
- **Propósito**: Verificar que el sistema básico funciona correctamente
- **Pruebas**: Importaciones, carga de datos, validaciones
- **Uso**: Primera prueba a ejecutar después de la instalación

#### `check_freecad.py`
- **Propósito**: Verificar si FreeCAD está instalado y configurado
- **Pruebas**: Comando freecad, rutas, módulos Python
- **Uso**: Antes de usar funcionalidades que requieren FreeCAD

#### `test_freecad_integration.py`
- **Propósito**: Probar la integración completa con FreeCAD
- **Pruebas**: Creación de documentos, objetos 3D, spreadsheets
- **Uso**: Después de instalar FreeCAD para verificar la integración

### Scripts de Demostración (`demos/`)

#### `demo_automatic.py`
- **Propósito**: Mostrar todas las funcionalidades automáticamente
- **Características**: No requiere interacción del usuario
- **Uso**: Para verificar que todo funciona correctamente

#### `demo_interactive.py`
- **Propósito**: Explorar funcionalidades de manera interactiva
- **Características**: Menú con opciones para explorar
- **Uso**: Para aprender sobre las capacidades del sistema

## 🔧 Script Principal

### `run_all_tests.py`
- **Propósito**: Ejecutar todas las pruebas y demos en secuencia
- **Características**: 
  - Ejecuta pruebas básicas
  - Verifica instalación de FreeCAD
  - Ejecuta demo automático
  - Proporciona resumen de resultados
- **Uso**: Para verificación completa del sistema

## 📊 Resultados Esperados

### Pruebas Básicas ✅
- Importaciones exitosas
- Carga de datos correcta
- Validaciones pasadas
- 9 presets de Ferrule y 9 de Gasket cargados

### Verificación FreeCAD ⚠️
- Si FreeCAD está instalado: Todas las verificaciones pasan
- Si FreeCAD no está instalado: Muestra instrucciones de instalación

### Demo Automático ✅
- Carga de datos exitosa
- Listado de tamaños disponibles
- Verificación de compatibilidad
- Validación de estándares

## 🛠️ Solución de Problemas

### Error: "Module not found"
```bash
# Asegúrate de ejecutar desde el directorio raíz del proyecto
cd TriptaFittings-FreeCAD
python scripts/testing/test_basic.py
```

### Error: "FreeCAD not found"
```bash
# Instalar FreeCAD siguiendo la guía
# docs/installation/install_freecad_windows.md
```

### Error: "Permission denied"
```bash
# En Windows, ejecutar como administrador
# O verificar permisos de escritura en el directorio
```

## 📖 Documentación

- **Documentación**: `docs/` carpeta
- **Instalación**: `docs/installation/` carpeta
- **Uso**: `docs/usage/` carpeta
- **Issues**: Crear issue en el repositorio

---

