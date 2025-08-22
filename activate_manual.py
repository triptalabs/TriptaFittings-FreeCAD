#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ACTIVADOR MANUAL DE TRIPTAFITTINGS WORKBENCH
=============================================

INSTRUCCIONES:
1. Abre FreeCAD
2. Ve a: View > Panels > Python Console  
3. Copia y pega TODO este código en la consola
4. Presiona Enter

Si aparecen errores, copia el mensaje completo.
"""

print("🚀 ACTIVADOR MANUAL TRIPTAFITTINGS")
print("=" * 50)

# Paso 1: Verificar que FreeCAD está disponible
try:
    import FreeCADGui as Gui
    import FreeCAD as App
    print("✅ FreeCAD detectado correctamente")
except ImportError as e:
    print(f"❌ Error: FreeCAD no disponible - {e}")
    print("   Este script debe ejecutarse DENTRO de FreeCAD")
    exit()

# Paso 2: Agregar el directorio del plugin al path
import sys
import os

# Directorio donde está instalado TriptaFittings
plugin_dir = os.path.expanduser("~/AppData/Roaming/FreeCAD/Mod/TriptaFittings")
print(f"📁 Buscando plugin en: {plugin_dir}")

if not os.path.exists(plugin_dir):
    print(f"❌ ERROR: Directorio del plugin no encontrado")
    print(f"   Esperado: {plugin_dir}")
    print("   Verifica que el plugin esté instalado correctamente")
    exit()

print("✅ Directorio del plugin encontrado")

# Agregar al Python path
if plugin_dir not in sys.path:
    sys.path.insert(0, plugin_dir)
    print("✅ Plugin agregado al Python path")

# Paso 3: Importar el workbench
print("\n🔧 Importando workbench...")
try:
    from src.triptafittings.workbench.init_gui import TriptaFittingsWorkbench
    print("✅ Workbench importado exitosamente")
except ImportError as e:
    print(f"❌ Error al importar workbench: {e}")
    print("   Verificando estructura de archivos...")
    
    # Verificar archivos críticos
    critical_files = [
        "InitGui.py",
        "src/triptafittings/__init__.py", 
        "src/triptafittings/workbench/init_gui.py",
        "src/triptafittings/workbench/commands.py",
        "src/triptafittings/workbench/gui.py"
    ]
    
    for file_path in critical_files:
        full_path = os.path.join(plugin_dir, file_path)
        if os.path.exists(full_path):
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - FALTA")
    exit()

# Paso 4: Crear y registrar el workbench
print("\n🔨 Registrando workbench con FreeCAD...")
try:
    # Crear instancia del workbench
    workbench = TriptaFittingsWorkbench()
    print("✅ Instancia de workbench creada")
    
    # Registrar con FreeCAD
    Gui.addWorkbench(workbench)
    print("✅ Workbench registrado con FreeCAD")
    
    # Verificar que se agregó
    workbenches = Gui.listWorkbenches()
    if 'TriptaFittingsWorkbench' in workbenches:
        print("🎉 ¡ÉXITO! TriptaFittings apareció en la lista de workbenches")
        print("   Ve a: View > Workbenches > TriptaFittings")
    else:
        print("⚠️  Workbench registrado pero no aparece en la lista")
        print("   Workbenches disponibles:")
        for wb_name in sorted(workbenches.keys()):
            print(f"     - {wb_name}")
            
except Exception as e:
    print(f"❌ Error al registrar workbench: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 50)
print("ACTIVACIÓN MANUAL COMPLETADA")
print("Si hay errores, copia el mensaje completo y compártelo")


