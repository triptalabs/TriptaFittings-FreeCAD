#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para activar manualmente el workbench TriptaFittings en FreeCAD.
Ejecutar en la consola de Python de FreeCAD.
"""

def activate_triptafittings_workbench():
    """Activa manualmente el workbench TriptaFittings."""
    print("🔧 Activando TriptaFittings workbench manualmente...")
    
    try:
        import sys
        import os
        
        # Agregar el directorio del plugin al path
        plugin_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if plugin_dir not in sys.path:
            sys.path.insert(0, plugin_dir)
            print(f"✅ Directorio del plugin agregado al path: {plugin_dir}")
        
        # Importar el workbench
        from src.triptafittings.workbench.init_gui import TriptaFittingsWorkbench
        print("✅ Workbench importado correctamente")
        
        # Registrar con FreeCAD
        import FreeCADGui as Gui
        
        # Verificar si ya está registrado
        workbenches = Gui.listWorkbenches()
        if "TriptaFittingsWorkbench" in workbenches:
            print("ℹ️ Workbench ya está registrado")
        else:
            # Crear y registrar workbench
            workbench = TriptaFittingsWorkbench()
            Gui.addWorkbench(workbench)
            print("✅ Workbench registrado exitosamente")
        
        # Activar el workbench
        Gui.activateWorkbench("TriptaFittingsWorkbench")
        print("✅ Workbench activado")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        return False
    except Exception as e:
        print(f"❌ Error general: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_workbench_status():
    """Verifica el estado del workbench."""
    print("🔍 Verificando estado del workbench...")
    
    try:
        import FreeCADGui as Gui
        
        workbenches = Gui.listWorkbenches()
        print(f"📋 Workbenches disponibles: {list(workbenches.keys())}")
        
        if "TriptaFittingsWorkbench" in workbenches:
            print("✅ TriptaFittings workbench está registrado")
            
            # Verificar workbench activo
            active_wb = Gui.activeWorkbench()
            if hasattr(active_wb, 'MenuText') and active_wb.MenuText == "TriptaFittings":
                print("✅ TriptaFittings workbench está activo")
            else:
                print("ℹ️ TriptaFittings workbench no está activo")
                print(f"   Workbench activo: {active_wb}")
        else:
            print("❌ TriptaFittings workbench NO está registrado")
            
    except Exception as e:
        print(f"❌ Error al verificar estado: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 SCRIPT DE ACTIVACIÓN MANUAL - TriptaFittings")
    print("=" * 60)
    
    # Verificar estado actual
    check_workbench_status()
    
    print("\n" + "=" * 60)
    print("🔧 INTENTANDO ACTIVACIÓN MANUAL")
    print("=" * 60)
    
    # Intentar activación
    success = activate_triptafittings_workbench()
    
    print("\n" + "=" * 60)
    print("📊 ESTADO FINAL")
    print("=" * 60)
    
    # Verificar estado final
    check_workbench_status()
    
    if success:
        print("\n🎉 ¡Activación exitosa!")
        print("   El workbench TriptaFittings debería aparecer en View → Workbenches")
    else:
        print("\n⚠️ Activación falló")
        print("   Revisar errores arriba para más información")
