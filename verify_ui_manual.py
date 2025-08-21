#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script para verificación manual de la UI de TriptaFittings.

Este script permite verificar la UI de diferentes maneras:
1. Modo consola (sin GUI, solo lógica)
2. Modo GUI standalone (si PySide2/PyQt5 disponible)
3. Modo simulación (con GUI mock)
"""

import sys
import os
from pathlib import Path

# Agregar el directorio src al path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def check_pyside2():
    """Verifica disponibilidad de PySide2/PyQt5."""
    try:
        from PySide2 import QtWidgets
        return "PySide2"
    except ImportError:
        try:
            from PyQt5 import QtWidgets
            return "PyQt5"
        except ImportError:
            return None

def test_console_mode():
    """Prueba el diálogo en modo consola (sin GUI)."""
    print("🖥️  MODO CONSOLA - Testing lógica de UI sin GUI")
    print("-" * 50)
    
    try:
        from src.triptafittings.ui.dialog import TriptaFittingsDialog
        
        # Crear diálogo (se ejecutará con mock objects)
        print("1. Creando diálogo...")
        dialog = TriptaFittingsDialog()
        
        # Verificar inicialización
        print("2. Verificando inicialización...")
        assert hasattr(dialog, 'data_manager'), "DataManager no inicializado"
        
        # Verificar datos
        print("3. Verificando datos...")
        summary = dialog.data_manager.get_data_summary()
        print(f"   - Ferrule presets: {summary['ferrule_count']}")
        print(f"   - Gasket presets: {summary['gasket_count']}")
        print(f"   - Tamaños disponibles: {len(summary['available_sizes'])}")
        
        # Simular interacción
        print("4. Simulando interacción...")
        if dialog.size_combo.count() > 0:
            dialog.size_combo.setCurrentIndex(0)
            dialog._on_size_changed()
            
            if dialog.current_preset:
                print(f"   - Preset cargado: {dialog.current_preset.get_name()}")
                print(f"   - DN: {dialog.current_preset.dn}")
                print(f"   - Parámetros: {len(dialog.current_preset.get_parameters_dict())}")
                
                # Simular generación
                print("5. Simulando generación de modelo...")
                initial_count = len(dialog.generated_models)
                dialog._generate_model()
                final_count = len(dialog.generated_models)
                print(f"   - Modelos generados: {final_count - initial_count}")
        
        print("✅ MODO CONSOLA - Todo funcionando correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error en modo consola: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_gui_mode():
    """Prueba el diálogo en modo GUI real."""
    gui_lib = check_pyside2()
    
    if not gui_lib:
        print("⚠️  GUI no disponible - PySide2/PyQt5 no instalados")
        return False
    
    print(f"🖼️  MODO GUI - Testing con {gui_lib}")
    print("-" * 50)
    
    try:
        # Importar Qt
        if gui_lib == "PySide2":
            from PySide2 import QtWidgets
        else:
            from PyQt5 import QtWidgets
        
        # Crear aplicación
        app = QtWidgets.QApplication.instance()
        if app is None:
            app = QtWidgets.QApplication(sys.argv)
        
        # Crear diálogo
        from src.triptafittings.ui.dialog import TriptaFittingsDialog
        dialog = TriptaFittingsDialog()
        
        print("✅ Diálogo creado exitosamente")
        print(f"   - Título: {dialog.windowTitle()}")
        print(f"   - Componentes: {dialog.component_combo.count()}")
        print(f"   - Tamaños: {dialog.size_combo.count()}")
        
        # Mostrar información
        print("\n📋 Para probar manualmente:")
        print("   1. Ejecuta: python verify_ui_manual.py --show")
        print("   2. Se abrirá el diálogo gráfico")
        print("   3. Prueba seleccionar componentes y tamaños")
        print("   4. Verifica la tabla de parámetros")
        print("   5. Prueba el botón Generate Model")
        
        # Si se pasa --show, mostrar el diálogo
        if "--show" in sys.argv:
            print("\n🚀 Mostrando diálogo...")
            dialog.show()
            return app.exec_() == 0
        
        return True
        
    except Exception as e:
        print(f"❌ Error en modo GUI: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_freecad_integration():
    """Verifica integración con comandos de FreeCAD."""
    print("🔧 INTEGRACIÓN FREECAD - Testing comandos")
    print("-" * 50)
    
    try:
        from src.triptafittings.workbench.commands import COMMANDS
        
        print(f"✅ {len(COMMANDS)} comandos disponibles:")
        for cmd_name, cmd_obj in COMMANDS.items():
            resources = cmd_obj.GetResources()
            print(f"   - {cmd_name}: {resources['MenuText']}")
        
        # Probar comando principal
        main_cmd = COMMANDS.get("Tripta_OpenDialog")
        if main_cmd:
            print(f"\n🧪 Probando comando principal...")
            # No ejecutar Activated() aquí porque abriría el diálogo
            resources = main_cmd.GetResources()
            print(f"   - Menú: {resources['MenuText']}")
            print(f"   - Tooltip: {resources['ToolTip']}")
            print("   ✅ Comando configurado correctamente")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en integración FreeCAD: {e}")
        return False

def show_usage():
    """Muestra instrucciones de uso."""
    gui_lib = check_pyside2()
    
    print("=" * 60)
    print("🎯 VERIFICACIÓN MANUAL - TriptaFittings UI (Issue #10)")
    print("=" * 60)
    
    print(f"\n📦 Estado del sistema:")
    print(f"   - GUI disponible: {'✅ ' + gui_lib if gui_lib else '❌ No'}")
    print(f"   - Python: {sys.version.split()[0]}")
    
    print(f"\n🚀 Opciones de verificación:")
    print(f"   1. Modo consola: python verify_ui_manual.py --console")
    print(f"   2. Modo GUI: python verify_ui_manual.py --gui")
    if gui_lib:
        print(f"   3. Mostrar UI: python verify_ui_manual.py --show")
    print(f"   4. Integración: python verify_ui_manual.py --freecad")
    print(f"   5. Todo: python verify_ui_manual.py --all")
    
    print(f"\n📋 Verificación en FreeCAD:")
    print(f"   1. Copiar plugin a: %APPDATA%\\FreeCAD\\Mod\\TriptaFittings")
    print(f"   2. Reiniciar FreeCAD")
    print(f"   3. Ir a View → Workbenches → TriptaFittings")
    print(f"   4. Usar comandos de la toolbar")

def main():
    """Función principal."""
    if len(sys.argv) == 1:
        show_usage()
        return
    
    mode = sys.argv[1]
    success = True
    
    if mode == "--console":
        success = test_console_mode()
    elif mode == "--gui":
        success = test_gui_mode()
    elif mode == "--show":
        success = test_gui_mode()
    elif mode == "--freecad":
        success = test_freecad_integration()
    elif mode == "--all":
        print("🔄 Ejecutando todas las verificaciones...\n")
        success = (test_console_mode() and 
                  test_gui_mode() and 
                  test_freecad_integration())
        print(f"\n📊 Resultado general: {'✅ ÉXITO' if success else '❌ FALLÓ'}")
    else:
        show_usage()
        return
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
