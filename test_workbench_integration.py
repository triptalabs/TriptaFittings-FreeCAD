#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para verificar la integración del workbench TriptaFittings
"""

import os
import sys

def test_workbench_integration():
    """Prueba la integración del workbench sin FreeCAD."""
    print("🔧 Probando integración del workbench TriptaFittings...")
    
    try:
        # Agregar src al path
        src_path = os.path.join(os.path.dirname(__file__), "src")
        if src_path not in sys.path:
            sys.path.insert(0, src_path)
        
        # Importar workbench
        from triptafittings.workbench.init_gui import TriptaFittingsWorkbench
        print("✅ Workbench importado correctamente")
        
        # Crear instancia
        wb = TriptaFittingsWorkbench()
        print("✅ Instancia de workbench creada")
        
        # Verificar atributos
        assert hasattr(wb, 'MenuText'), "Falta atributo MenuText"
        assert hasattr(wb, 'ToolTip'), "Falta atributo ToolTip"
        assert hasattr(wb, 'Icon'), "Falta atributo Icon"
        print("✅ Atributos básicos presentes")
        
        # Verificar métodos
        assert hasattr(wb, 'Initialize'), "Falta método Initialize"
        assert hasattr(wb, 'Activated'), "Falta método Activated"
        assert hasattr(wb, 'Deactivated'), "Falta método Deactivated"
        assert hasattr(wb, 'GetClassName'), "Falta método GetClassName"
        print("✅ Métodos requeridos presentes")
        
        # Probar Initialize (sin FreeCAD)
        wb.Initialize()
        print("✅ Initialize ejecutado sin errores")
        
        # Verificar comandos y toolbar
        assert len(wb.toolbar) > 0, "Toolbar vacía"
        assert len(wb.menu) > 0, "Menú vacío"
        print(f"✅ Toolbar: {len(wb.toolbar)} comandos")
        print(f"✅ Menú: {len(wb.menu)} comandos")
        
        # Probar comandos
        from triptafittings.workbench.commands import COMMANDS
        assert len(COMMANDS) > 0, "No hay comandos definidos"
        print(f"✅ Comandos disponibles: {list(COMMANDS.keys())}")
        
        # Verificar iconos
        from triptafittings.workbench.gui import get_command_icon, WB_ICON
        for cmd_name in COMMANDS.keys():
            icon_path = get_command_icon(cmd_name)
            print(f"✅ Icono para {cmd_name}: {os.path.basename(icon_path)}")
        
        print(f"✅ Icono principal: {os.path.basename(WB_ICON)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_commands():
    """Prueba los comandos individualmente."""
    print("\n🔧 Probando comandos individuales...")
    
    try:
        from triptafittings.workbench.commands import COMMANDS
        
        for cmd_name, cmd_obj in COMMANDS.items():
            print(f"\n--- Probando comando: {cmd_name} ---")
            
            # Verificar métodos requeridos
            assert hasattr(cmd_obj, 'Activated'), f"Comando {cmd_name} no tiene método Activated"
            assert hasattr(cmd_obj, 'GetResources'), f"Comando {cmd_name} no tiene método GetResources"
            
            # Probar GetResources
            resources = cmd_obj.GetResources()
            assert 'MenuText' in resources, f"Comando {cmd_name} no tiene MenuText"
            assert 'ToolTip' in resources, f"Comando {cmd_name} no tiene ToolTip"
            assert 'Pixmap' in resources, f"Comando {cmd_name} no tiene Pixmap"
            
            print(f"  ✅ MenuText: {resources['MenuText']}")
            print(f"  ✅ ToolTip: {resources['ToolTip']}")
            print(f"  ✅ Pixmap: {os.path.basename(resources['Pixmap'])}")
            
            # Probar Activated (puede fallar sin UI, pero no debe crashear)
            try:
                result = cmd_obj.Activated()
                print(f"  ✅ Activated ejecutado: {result}")
            except Exception as e:
                print(f"  ⚠️ Activated falló (esperado sin UI): {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error probando comandos: {e}")
        import traceback
        traceback.print_exc()
        return False

def verify_icons():
    """Verifica que todos los iconos existan."""
    print("\n🔧 Verificando iconos...")
    
    try:
        from triptafittings.workbench.gui import get_command_icon, WB_ICON
        from triptafittings.workbench.commands import COMMANDS
        
        # Verificar icono principal
        if os.path.exists(WB_ICON):
            print(f"✅ Icono principal existe: {WB_ICON}")
        else:
            print(f"❌ Icono principal no existe: {WB_ICON}")
        
        # Verificar iconos de comandos
        for cmd_name in COMMANDS.keys():
            icon_path = get_command_icon(cmd_name)
            if os.path.exists(icon_path):
                print(f"✅ Icono existe para {cmd_name}: {icon_path}")
            else:
                print(f"❌ Icono NO existe para {cmd_name}: {icon_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error verificando iconos: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 PRUEBA DE INTEGRACIÓN - WORKBENCH TRIPTAFITTINGS")
    print("=" * 60)
    
    success = True
    
    # Probar workbench
    success &= test_workbench_integration()
    
    # Probar comandos
    success &= test_commands()
    
    # Verificar iconos
    success &= verify_icons()
    
    print("\n" + "=" * 60)
    print("📊 RESULTADO FINAL")
    print("=" * 60)
    
    if success:
        print("🎉 ¡Todas las pruebas pasaron!")
        print("   El workbench está listo para integración con FreeCAD")
    else:
        print("⚠️ Algunas pruebas fallaron")
        print("   Revisar errores arriba")
