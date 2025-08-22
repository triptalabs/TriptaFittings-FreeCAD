#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para diagnosticar y arreglar el problema de registro del workbench TriptaFittings
"""

import sys
import os
import traceback

def test_freecad_gui():
    """Prueba la disponibilidad de FreeCADGui"""
    print("🔍 Probando FreeCADGui...")
    
    try:
        import FreeCADGui as Gui
        print("✅ FreeCADGui importado correctamente")
        
        # Verificar si Workbench está disponible
        if hasattr(Gui, 'Workbench'):
            print("✅ FreeCADGui.Workbench disponible")
            return True
        else:
            print("❌ FreeCADGui.Workbench NO disponible")
            print("   Esto es normal en modo consola")
            return False
            
    except ImportError as e:
        print(f"❌ Error al importar FreeCADGui: {e}")
        return False

def test_workbench_import():
    """Prueba la importación del workbench"""
    print("\n🔍 Probando importación del workbench...")
    
    try:
        # Agregar el directorio del plugin al path
        plugin_dir = os.path.join(os.environ['APPDATA'], 'FreeCAD', 'Mod', 'TriptaFittings')
        sys.path.insert(0, plugin_dir)
        
        # Intentar importar el workbench
        from src.triptafittings.workbench.init_gui import TriptaFittingsWorkbench
        print("✅ TriptaFittingsWorkbench importado correctamente")
        
        # Crear instancia
        wb = TriptaFittingsWorkbench()
        print("✅ Instancia del workbench creada correctamente")
        print(f"   MenuText: {wb.MenuText}")
        print(f"   ToolTip: {wb.ToolTip}")
        print(f"   Icon: {wb.Icon}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al importar workbench: {e}")
        traceback.print_exc()
        return False

def test_commands_import():
    """Prueba la importación de comandos"""
    print("\n🔍 Probando importación de comandos...")
    
    try:
        plugin_dir = os.path.join(os.environ['APPDATA'], 'FreeCAD', 'Mod', 'TriptaFittings')
        sys.path.insert(0, plugin_dir)
        
        from src.triptafittings.workbench.commands import COMMANDS
        print(f"✅ Comandos importados: {len(COMMANDS)} comandos disponibles")
        
        for cmd_name in COMMANDS.keys():
            print(f"   - {cmd_name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al importar comandos: {e}")
        traceback.print_exc()
        return False

def test_icons():
    """Prueba la disponibilidad de iconos"""
    print("\n🔍 Probando iconos...")
    
    try:
        plugin_dir = os.path.join(os.environ['APPDATA'], 'FreeCAD', 'Mod', 'TriptaFittings')
        icons_dir = os.path.join(plugin_dir, 'resources', 'icons')
        
        required_icons = [
            'triptafittings.svg',
            'create_ferrule.svg',
            'create_gasket.svg',
            'open_dialog.svg'
        ]
        
        missing_icons = []
        for icon in required_icons:
            icon_path = os.path.join(icons_dir, icon)
            if os.path.exists(icon_path):
                print(f"✅ {icon} - OK")
            else:
                print(f"❌ {icon} - FALTANTE")
                missing_icons.append(icon)
        
        if not missing_icons:
            print("✅ Todos los iconos están disponibles")
            return True
        else:
            print(f"❌ Faltan {len(missing_icons)} iconos")
            return False
            
    except Exception as e:
        print(f"❌ Error al verificar iconos: {e}")
        return False

def create_fixed_initgui():
    """Crea una versión corregida de InitGui.py"""
    print("\n🔧 Creando InitGui.py corregido...")
    
    fixed_content = '''# -*- coding: utf-8 -*-
"""Punto de entrada para FreeCAD - InitGui.py (VERSIÓN CORREGIDA)

Este archivo es requerido por FreeCAD para registrar el workbench.
Versión corregida para FreeCAD 1.0+
"""

import sys
import os

def register_workbench():
    """Registra el workbench con FreeCAD"""
    try:
        # Importar FreeCADGui
        import FreeCADGui as Gui
        
        # Verificar que Workbench esté disponible
        if not hasattr(Gui, 'Workbench'):
            print("⚠️ FreeCADGui.Workbench no disponible - intentando inicializar GUI")
            try:
                # Intentar inicializar la GUI
                Gui.showMainWindow()
                # Reimportar para obtener Workbench
                import FreeCADGui as Gui
            except Exception as e:
                print(f"❌ No se pudo inicializar GUI: {e}")
                return False
        
        # Importar el workbench
        from src.triptafittings.workbench.init_gui import TriptaFittingsWorkbench
        
        # Crear instancia del workbench
        workbench = TriptaFittingsWorkbench()
        
        # Registrar con FreeCAD
        Gui.addWorkbench(workbench)
        print("✅ TriptaFittings workbench registrado exitosamente")
        return True
        
    except ImportError as e:
        print(f"❌ Error al importar módulos: {e}")
        return False
    except Exception as e:
        print(f"❌ Error al registrar workbench: {e}")
        import traceback
        traceback.print_exc()
        return False

# Registrar automáticamente al importar
if __name__ == "__main__":
    register_workbench()
else:
    # Cuando se importa desde FreeCAD
    register_workbench()
'''
    
    # Escribir el archivo corregido
    plugin_dir = os.path.join(os.environ['APPDATA'], 'FreeCAD', 'Mod', 'TriptaFittings')
    initgui_path = os.path.join(plugin_dir, 'InitGui_fixed.py')
    
    with open(initgui_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"✅ Archivo corregido creado: {initgui_path}")
    return initgui_path

def backup_and_replace_initgui():
    """Hace backup del InitGui.py original y lo reemplaza con la versión corregida"""
    print("\n🔧 Haciendo backup y reemplazando InitGui.py...")
    
    plugin_dir = os.path.join(os.environ['APPDATA'], 'FreeCAD', 'Mod', 'TriptaFittings')
    original_path = os.path.join(plugin_dir, 'InitGui.py')
    backup_path = os.path.join(plugin_dir, 'InitGui_backup.py')
    
    try:
        # Hacer backup del original
        if os.path.exists(original_path):
            import shutil
            shutil.copy2(original_path, backup_path)
            print(f"✅ Backup creado: {backup_path}")
        
        # Crear versión corregida
        fixed_path = create_fixed_initgui()
        
        # Reemplazar el original
        import shutil
        shutil.copy2(fixed_path, original_path)
        print(f"✅ InitGui.py reemplazado con versión corregida")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al hacer backup/reemplazo: {e}")
        return False

def main():
    """Función principal de diagnóstico"""
    print("🔧 DIAGNÓSTICO Y REPARACIÓN - TriptaFittings Workbench")
    print("=" * 60)
    
    # Ejecutar pruebas
    tests = [
        ("FreeCADGui", test_freecad_gui),
        ("Workbench Import", test_workbench_import),
        ("Commands Import", test_commands_import),
        ("Icons", test_icons),
    ]
    
    results = {}
    for test_name, test_func in tests:
        print(f"\n📋 Ejecutando: {test_name}")
        results[test_name] = test_func()
    
    # Resumen
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE DIAGNÓSTICO")
    print("=" * 60)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASÓ" if result else "❌ FALLÓ"
        print(f"{test_name}: {status}")
    
    print(f"\nProgreso: {passed}/{total} pruebas pasaron")
    
    # Recomendaciones
    print("\n💡 RECOMENDACIONES:")
    
    if not results["FreeCADGui"]:
        print("1. FreeCADGui no está disponible - esto es normal en modo consola")
        print("2. El workbench se registrará cuando abras FreeCAD")
    
    if not results["Workbench Import"]:
        print("3. Problema con la importación del workbench")
        print("4. Verificar estructura de archivos")
    
    if not results["Commands Import"]:
        print("5. Problema con la importación de comandos")
        print("6. Verificar archivo commands.py")
    
    if not results["Icons"]:
        print("7. Faltan iconos - copiar desde el directorio original")
    
    # Intentar reparación automática
    if passed < total:
        print("\n🔧 INTENTANDO REPARACIÓN AUTOMÁTICA...")
        if backup_and_replace_initgui():
            print("✅ Reparación completada")
            print("🔄 Reinicia FreeCAD para aplicar los cambios")
        else:
            print("❌ No se pudo completar la reparación automática")
    
    print("\n🎯 PRÓXIMOS PASOS:")
    print("1. Reinicia FreeCAD completamente")
    print("2. Ve a View → Workbenches")
    print("3. Busca 'TriptaFittings' en la lista")
    print("4. Si no aparece, ejecuta este script nuevamente")

if __name__ == "__main__":
    main()
