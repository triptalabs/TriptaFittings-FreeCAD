# Script para ejecutar en la consola de Python de FreeCAD
# Copia y pega este código en: View > Panels > Python Console

print("🔍 DIAGNÓSTICO TRIPTAFITTINGS")
print("=" * 50)

# 1. Verificar paths
import sys
import os

print("📁 Paths relevantes:")
for path in sys.path:
    if 'freecad' in path.lower() or 'mod' in path.lower():
        print(f"  ✅ {path}")

# 2. Verificar directorio Mod
mod_path = os.path.expanduser("~/AppData/Roaming/FreeCAD/Mod/TriptaFittings")
print(f"\n📂 Verificando: {mod_path}")
if os.path.exists(mod_path):
    print("  ✅ Directorio TriptaFittings existe")
    initgui = os.path.join(mod_path, "InitGui.py")
    if os.path.exists(initgui):
        print("  ✅ InitGui.py encontrado")
    else:
        print("  ❌ InitGui.py NO encontrado")
else:
    print("  ❌ Directorio TriptaFittings NO existe")

# 3. Intentar import del workbench
print("\n🔧 Probando imports:")
try:
    import FreeCAD
    print("  ✅ FreeCAD importado")
    
    import FreeCADGui as Gui
    print("  ✅ FreeCADGui importado")
    
    # Agregar path del plugin
    if mod_path not in sys.path:
        sys.path.insert(0, mod_path)
        print("  ✅ Path del plugin agregado")
    
    from src.triptafittings.workbench.init_gui import TriptaFittingsWorkbench
    print("  ✅ TriptaFittingsWorkbench importado")
    
    wb = TriptaFittingsWorkbench()
    print("  ✅ Instancia creada")
    
    wb.Initialize()
    print("  ✅ Initialize ejecutado")
    
    print(f"  📊 Comandos: {len(wb.commands)}")
    print(f"  📊 Toolbar: {len(wb.toolbar)}")
    print(f"  📊 Menu: {len(wb.menu)}")
    
except Exception as e:
    print(f"  ❌ Error: {e}")
    import traceback
    traceback.print_exc()

# 4. Verificar workbenches registrados
print("\n📋 Workbenches disponibles:")
try:
    workbenches = Gui.listWorkbenches()
    print(f"  Total workbenches: {len(workbenches)}")
    for name in sorted(workbenches.keys()):
        if 'tripta' in name.lower():
            print(f"  ✅ ENCONTRADO: {name}")
except Exception as e:
    print(f"  ❌ Error listando workbenches: {e}")

print("\n🎯 INSTRUCCIONES:")
print("1. Ve a View > Workbenches")
print("2. Busca 'TriptaFittings' en la lista")
print("3. Si no aparece, ejecuta este diagnóstico")



