# 🚀 Guía de Instalación de FreeCAD en Windows

## 📋 Requisitos Previos

### Sistema Operativo
- **Windows 10/11** (64-bit)
- **Mínimo 4GB RAM** (recomendado 8GB+)
- **2GB espacio libre** en disco

### Python
- **Python 3.8+** (ya tienes Python 3.13.5 ✅)

## 🔧 Métodos de Instalación

### Método 1: Instalador Oficial (Recomendado)

#### Paso 1: Descargar FreeCAD
1. **Ir a la página oficial**: https://www.freecad.org/downloads.php
2. **Seleccionar Windows**
3. **Descargar la versión estable** (0.20.x o superior)
4. **Elegir la versión correcta**:
   - **64-bit**: Para sistemas modernos
   - **Con Python**: Incluye Python integrado

#### Paso 2: Instalar FreeCAD
1. **Ejecutar el instalador** como administrador
2. **Seguir el asistente de instalación**
3. **Marcar opciones importantes**:
   - ✅ Add FreeCAD to PATH
   - ✅ Associate .FCStd files
   - ✅ Create desktop shortcut
4. **Completar la instalación**

#### Paso 3: Verificar Instalación
```cmd
# Abrir Command Prompt y verificar
freecad --version

# O buscar en el menú de inicio
# FreeCAD debería aparecer en "Programs"
```

### Método 2: Chocolatey (Si tienes Chocolatey instalado)

```cmd
# Instalar Chocolatey primero (si no lo tienes)
# https://chocolatey.org/install

# Instalar FreeCAD
choco install freecad
```

### Método 3: Conda (Si usas Anaconda/Miniconda)

```cmd
# Crear entorno conda para FreeCAD
conda create -n freecad python=3.9
conda activate freecad

# Instalar FreeCAD
conda install -c conda-forge freecad
```

## 🔍 Verificación de la Instalación

### 1. Verificar desde Python
```python
# Crear archivo: test_freecad.py
import sys
import os

def test_freecad():
    try:
        import FreeCAD
        print("✅ FreeCAD importado correctamente")
        print(f"Versión: {FreeCAD.Version()}")
        print(f"Build: {FreeCAD.BuildVersionString()}")
        return True
    except ImportError as e:
        print(f"❌ Error al importar FreeCAD: {e}")
        return False

if __name__ == "__main__":
    test_freecad()
```

### 2. Verificar desde Línea de Comandos
```cmd
# Verificar que FreeCAD está en PATH
where freecad

# Verificar versión
freecad --version

# Verificar módulos Python
python -c "import FreeCAD; print('FreeCAD OK')"
```

## 🛠️ Configuración Post-Instalación

### 1. Configurar PATH (si es necesario)
Si FreeCAD no está en PATH:
1. **Buscar la instalación**: `C:\Program Files\FreeCAD\bin`
2. **Agregar al PATH**:
   - Panel de Control → Sistema → Variables de Entorno
   - Editar PATH → Agregar ruta de FreeCAD

### 2. Configurar Python
```cmd
# Verificar que Python puede encontrar FreeCAD
python -c "import sys; print('\\n'.join(sys.path))"

# Si es necesario, agregar manualmente
python -c "import sys; sys.path.append('C:/Program Files/FreeCAD/lib')"
```

### 3. Instalar Dependencias Adicionales
```cmd
# Instalar paquetes útiles
pip install numpy scipy matplotlib
```

## 🧪 Pruebas de Funcionalidad

### 1. Prueba Básica de FreeCAD
```python
# Crear archivo: test_freecad_basic.py
import FreeCAD
import Part
import Spreadsheet

def test_basic_functionality():
    print("🔧 Probando funcionalidades básicas de FreeCAD...")
    
    # Crear documento
    doc = FreeCAD.newDocument("Test")
    print("✅ Documento creado")
    
    # Crear objeto básico
    box = Part.makeBox(10, 10, 10)
    print("✅ Objeto 3D creado")
    
    # Crear spreadsheet
    sheet = doc.addObject('Spreadsheet::Sheet', 'TestSheet')
    print("✅ Spreadsheet creado")
    
    print("🎉 Todas las pruebas básicas pasaron!")
    return True

if __name__ == "__main__":
    test_basic_functionality()
```

### 2. Prueba de Integración con TriptaFittings
```cmd
# Ejecutar prueba de integración
python test_freecad_integration.py
```

## 🔧 Solución de Problemas

### Error: "No module named 'FreeCAD'"
**Soluciones:**
1. **Verificar instalación**: `freecad --version`
2. **Agregar al PATH**: Ruta de instalación de FreeCAD
3. **Usar Python de FreeCAD**: `C:\Program Files\FreeCAD\bin\python.exe`

### Error: "ImportError: DLL load failed"
**Soluciones:**
1. **Reinstalar Visual C++ Redistributable**
2. **Verificar arquitectura**: 64-bit vs 32-bit
3. **Actualizar drivers de gráficos**

### Error: "FreeCAD not found in PATH"
**Soluciones:**
1. **Agregar manualmente al PATH**
2. **Usar ruta completa**: `"C:\Program Files\FreeCAD\bin\freecad.exe"`
3. **Crear alias**: `doskey freecad="C:\Program Files\FreeCAD\bin\freecad.exe"`

## 📁 Ubicaciones Importantes

### Archivos de Instalación
- **Ejecutable**: `C:\Program Files\FreeCAD\bin\freecad.exe`
- **Python**: `C:\Program Files\FreeCAD\bin\python.exe`
- **Librerías**: `C:\Program Files\FreeCAD\lib`
- **Módulos**: `C:\Program Files\FreeCAD\Mod`

### Archivos de Usuario
- **Configuración**: `%APPDATA%\FreeCAD`
- **Macros**: `%APPDATA%\FreeCAD\Macro`
- **Workbenches**: `%APPDATA%\FreeCAD\Mod`

## 🎯 Próximos Pasos

### 1. Instalar TriptaFittings Plugin
```cmd
# Copiar plugin a la carpeta de FreeCAD
xcopy /E /I "TriptaFittings" "%APPDATA%\FreeCAD\Mod\TriptaFittings"
```

### 2. Verificar Plugin
```cmd
# Ejecutar pruebas de integración
python test_freecad_integration.py
```

### 3. Usar FreeCAD con TriptaFittings
1. **Abrir FreeCAD**
2. **Activar workbench**: View → Workbenches → TriptaFittings
3. **Generar modelos**: Usar los comandos del plugin

## 📖 Documentación

### Recursos Oficiales
- **Documentación**: https://wiki.freecad.org/
- **Foros**: https://forum.freecad.org/
- **GitHub**: https://github.com/FreeCAD/FreeCAD

### Comandos Útiles
```cmd
# Verificar instalación
freecad --version

# Ejecutar FreeCAD
freecad

# Ejecutar con archivo específico
freecad mi_archivo.FCStd

# Ejecutar macro
freecad -M mi_macro.FCMacro
```

---
