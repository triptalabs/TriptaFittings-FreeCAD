# 🚀 Guía de Instalación y Uso - TriptaFittings-FreeCAD

## 📋 Requisitos Previos

### Software Necesario
- **Python**: Versión 3.8 o superior
- **FreeCAD**: Versión 0.20 o superior (opcional para funcionalidades completas)

### Verificación de Requisitos
```bash
# Verificar Python
python --version

# Verificar si FreeCAD está disponible (opcional)
python -c "import FreeCAD; print('FreeCAD disponible')"
```

## 🔧 Instalación

### Opción 1: Prueba Rápida (Sin FreeCAD)

Si solo quieres probar el sistema de datos y funcionalidades básicas:

```bash
# 1. Clonar o descargar el repositorio
git clone https://github.com/triptalabs/TriptaFittings-FreeCAD.git
cd TriptaFittings-FreeCAD

# 2. Ejecutar pruebas básicas
python test_basic.py

# 3. Ejecutar demo interactivo
python demo_interactive.py
```

### Opción 2: Instalación Completa (Con FreeCAD)

#### Paso 1: Instalar FreeCAD

**Windows:**
1. Descargar desde: https://www.freecad.org/
2. Instalar la versión 0.20 o superior
3. Verificar que Python esté incluido en la instalación

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install freecad
```

**macOS:**
```bash
brew install freecad
```

#### Paso 2: Instalar el Plugin

**Método A: Addon Manager (Recomendado)**
1. Abrir FreeCAD
2. Ir a **Tools → Addon Manager**
3. Buscar "TriptaFittings"
4. Hacer clic en **Install**

**Método B: Instalación Manual**
1. Copiar la carpeta `TriptaFittings` a:
   - **Windows**: `%APPDATA%\FreeCAD\Mod\`
   - **macOS**: `~/Library/Application Support/FreeCAD/Mod/`
   - **Linux**: `~/.FreeCAD/Mod/`

2. Reiniciar FreeCAD

#### Paso 3: Verificar Instalación

```bash
# Ejecutar prueba de integración
python test_freecad_integration.py
```

## 🎮 Cómo Usar

### 1. Prueba Básica del Sistema

```bash
# Ejecutar pruebas básicas
python test_basic.py
```

**Resultado esperado:**
```
🚀 Iniciando pruebas básicas de TriptaFittings
==================================================
🔍 Probando importaciones básicas...
✅ DataManager importado correctamente
✅ Preset importado correctamente
✅ CSVLoader importado correctamente

🔍 Probando DataManager...
✅ DataManager creado exitosamente
📊 Cargando datos...
✅ Datos cargados exitosamente
📈 Resumen:
   - Ferrule presets: 9
   - Gasket presets: 9
   - Tamaños disponibles: [1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 8.0, 10.0, 12.0]

==================================================
📊 Resultados: 3/3 pruebas pasaron
🎉 ¡Todas las pruebas pasaron! El sistema está funcionando correctamente.
```

### 2. Demo Interactivo

```bash
# Ejecutar demo interactivo
python demo_interactive.py
```

**Funcionalidades disponibles:**
- 📊 Mostrar resumen de datos
- 📏 Ver tamaños disponibles
- 🔍 Ver detalles de Ferrule/Gasket
- 🔗 Verificar compatibilidad
- 🧪 Ejecutar validación completa

### 3. Uso en FreeCAD

#### Activar el Workbench
1. Abrir FreeCAD
2. Ir a **View → Workbenches → TriptaFittings**

#### Generar un Modelo
1. **Seleccionar Componente**: Ferrule o Gasket
2. **Elegir Tamaño**: 1.5", 2", 2.5", 3", 4", 6", 8", 10", 12"
3. **Hacer clic en "Generate Model"**

#### Parámetros Disponibles

**Ferrule (Férula):**
- `PassageDia`: Diámetro del paso
- `TubeID`: Diámetro interior del tubo
- `FlangeOD`: Diámetro exterior de la brida
- `C2`: Dimensión C2
- `SeatLipWidth`: Ancho del labio del asiento
- `HeightTube`: Altura del tubo
- `HeightProfile`: Altura del perfil

**Gasket (Junta):**
- `GasketOD`: Diámetro exterior de la junta
- `GasketID`: Diámetro interior de la junta
- `ProfileH`: Altura del perfil
- `C2`: Dimensión C2
- `SeatLipWidth`: Ancho del labio del asiento

## 🧪 Scripts de Prueba Disponibles

### 1. `test_basic.py`
Prueba básica del sistema de datos sin FreeCAD.

### 2. `demo_interactive.py`
Demo interactivo para explorar funcionalidades.

### 3. `test_freecad_integration.py`
Prueba de integración con FreeCAD.

### 4. `test_sprint1.py`
Prueba completa del Sprint 1 (sistema de datos).

## 📊 Datos y Estándares

### Estándares Soportados
- **DIN 32676 A**: Estándar alemán para conexiones de tubería
- **Tamaños**: 1.5" a 12" (DN40 a DN300)
- **Materiales**: Compatible con todos los materiales de FreeCAD

### Archivos de Datos
- `data/presets_ferrule_din32676A_1p5_to_12in.csv`: Presets de Ferrule
- `data/Presets_Gasket_DIN_32676_A__1_5_12_in_.csv`: Presets de Gasket

## 🔍 Solución de Problemas

### Error: "No module named 'FreeCAD'"
**Solución:** FreeCAD no está instalado o no está en el PATH.
```bash
# Instalar FreeCAD según tu sistema operativo
# Ver sección "Instalar FreeCAD" arriba
```

### Error: "ImportError: cannot import name 'DataManager'"
**Solución:** Verificar que estás en el directorio correcto.
```bash
# Asegúrate de estar en el directorio del proyecto
cd TriptaFittings-FreeCAD
python test_basic.py
```

### Error: "FileNotFoundError: data/*.csv"
**Solución:** Verificar que los archivos CSV están presentes.
```bash
# Verificar archivos de datos
ls data/*.csv
```

### Error en FreeCAD: "Workbench not found"
**Solución:** Verificar instalación del plugin.
```bash
# Verificar que la carpeta está en la ubicación correcta
# Reiniciar FreeCAD después de la instalación
```

## 📈 Estado del Proyecto

### ✅ Completado
- Sistema de datos robusto
- Validación de integridad
- Tests unitarios
- Documentación técnica

### ⏳ En Desarrollo
- Generadores de modelos 3D
- Interfaz de usuario completa
- Integración con FreeCAD
- Funcionalidades avanzadas

### 📋 Próximas Funcionalidades
- Exportación a formatos estándar
- Gestión de múltiples modelos
- Herramientas de debugging
- Documentación para más estándares

## 📖 Documentación

### Recursos
- **Documentación**: [README.md](README.md)
- **Roadmap**: [docs/roadmap.md](docs/roadmap.md)
- **Issues**: [GitHub Issues](https://github.com/triptalabs/TriptaFittings-FreeCAD/issues)

### Contacto
- **Email**: info@triptalabs.com
- **GitHub**: [triptalabs](https://github.com/triptalabs)

## 🎯 Próximos Pasos

1. **Instalar FreeCAD** (si quieres funcionalidades completas)
2. **Probar el sistema básico** con `test_basic.py`
3. **Explorar funcionalidades** con `demo_interactive.py`
4. **Instalar el plugin** en FreeCAD
5. **Generar modelos** usando el workbench

---

**¡Disfruta explorando TriptaFittings-FreeCAD! 🚀**
