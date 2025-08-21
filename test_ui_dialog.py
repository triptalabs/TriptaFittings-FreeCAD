#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script de testing para el diálogo TriptaFittings (Issue #10).

Este script prueba la nueva interfaz gráfica sin requerir FreeCAD,
validando toda la funcionalidad implementada.
"""

import sys
import os
from pathlib import Path

# Agregar el directorio src al path para imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_dialog_import():
    """Prueba que el diálogo se puede importar correctamente."""
    print("🔍 Testing: Importación del diálogo...")
    
    try:
        from src.triptafittings.ui.dialog import TriptaFittingsDialog, show_triptafittings_dialog
        print("✅ Diálogo importado correctamente")
        return True
    except Exception as e:
        print(f"❌ Error al importar diálogo: {e}")
        return False

def test_data_manager_integration():
    """Prueba que el diálogo integra correctamente con DataManager."""
    print("\n🔍 Testing: Integración con DataManager...")
    
    try:
        from src.triptafittings.ui.dialog import TriptaFittingsDialog
        
        # Crear diálogo de prueba
        dialog = TriptaFittingsDialog()
        
        # Verificar que el data manager está inicializado
        assert hasattr(dialog, 'data_manager'), "DataManager no inicializado"
        
        # Verificar que se cargaron datos
        summary = dialog.data_manager.get_data_summary()
        assert summary['loaded'], "Datos no cargados"
        assert summary['ferrule_count'] > 0, "No se cargaron presets de Ferrule"
        assert summary['gasket_count'] > 0, "No se cargaron presets de Gasket"
        
        print(f"✅ DataManager integrado - {summary['ferrule_count']} Ferrule, {summary['gasket_count']} Gasket")
        return True
        
    except Exception as e:
        print(f"❌ Error en integración DataManager: {e}")
        return False

def test_ui_components():
    """Prueba que los componentes de UI están presentes."""
    print("\n🔍 Testing: Componentes de UI...")
    
    try:
        from src.triptafittings.ui.dialog import TriptaFittingsDialog
        
        dialog = TriptaFittingsDialog()
        
        # Verificar componentes principales
        components = [
            'component_combo', 'size_combo', 'dn_label',
            'params_table', 'generate_btn', 'preview_btn',
            'validate_btn', 'progress_bar', 'status_text'
        ]
        
        missing = []
        for component in components:
            if not hasattr(dialog, component):
                missing.append(component)
        
        if missing:
            print(f"❌ Componentes faltantes: {missing}")
            return False
        
        print("✅ Todos los componentes de UI presentes")
        return True
        
    except Exception as e:
        print(f"❌ Error al verificar componentes UI: {e}")
        return False

def test_dropdown_population():
    """Prueba que los dropdowns se llenan con datos."""
    print("\n🔍 Testing: Población de dropdowns...")
    
    try:
        from src.triptafittings.ui.dialog import TriptaFittingsDialog
        
        dialog = TriptaFittingsDialog()
        
        # Verificar dropdown de componentes
        component_count = dialog.component_combo.count()
        assert component_count == 2, f"Expected 2 components, got {component_count}"
        
        # Verificar dropdown de tamaños
        size_count = dialog.size_combo.count()
        assert size_count > 0, "No hay tamaños en el dropdown"
        
        print(f"✅ Dropdowns poblados - {component_count} componentes, {size_count} tamaños")
        return True
        
    except Exception as e:
        print(f"❌ Error al verificar dropdowns: {e}")
        return False

def test_preset_loading():
    """Prueba que se puede cargar un preset y actualizar parámetros."""
    print("\n🔍 Testing: Carga de presets...")
    
    try:
        from src.triptafittings.ui.dialog import TriptaFittingsDialog
        
        dialog = TriptaFittingsDialog()
        
        # Simular selección de tamaño
        if dialog.size_combo.count() > 0:
            dialog.size_combo.setCurrentIndex(0)
            dialog._on_size_changed()
            
            # Verificar que se cargó un preset
            assert dialog.current_preset is not None, "No se cargó preset"
            
            # Verificar que la tabla tiene parámetros
            row_count = dialog.params_table.rowCount()
            assert row_count > 0, "La tabla de parámetros está vacía"
            
            print(f"✅ Preset cargado con {row_count} parámetros")
            return True
        else:
            print("⚠️ No hay tamaños disponibles para probar")
            return True
            
    except Exception as e:
        print(f"❌ Error al cargar preset: {e}")
        return False

def test_validation():
    """Prueba el sistema de validación."""
    print("\n🔍 Testing: Sistema de validación...")
    
    try:
        from src.triptafittings.ui.dialog import TriptaFittingsDialog
        
        dialog = TriptaFittingsDialog()
        
        # Probar validación sin selección
        dialog._validate_selection()
        assert not dialog.generate_btn.isEnabled(), "Botón debería estar deshabilitado sin selección"
        
        # Simular selección válida
        if dialog.size_combo.count() > 0:
            dialog.size_combo.setCurrentIndex(0)
            dialog._on_size_changed()
            
            # Probar validación con selección
            dialog._validate_selection()
            # El botón debería estar habilitado si hay preset válido
            
        print("✅ Sistema de validación funcionando")
        return True
        
    except Exception as e:
        print(f"❌ Error en validación: {e}")
        return False

def test_commands_integration():
    """Prueba que los comandos pueden crear el diálogo."""
    print("\n🔍 Testing: Integración con comandos...")
    
    try:
        from src.triptafittings.workbench.commands import COMMANDS
        
        # Verificar que los comandos existen
        expected_commands = ["Tripta_OpenDialog", "Tripta_CreateFerrule", "Tripta_CreateGasket"]
        
        for cmd_name in expected_commands:
            assert cmd_name in COMMANDS, f"Comando {cmd_name} no encontrado"
            
            # Verificar que el comando tiene los métodos necesarios
            cmd = COMMANDS[cmd_name]
            assert hasattr(cmd, 'Activated'), f"Comando {cmd_name} no tiene método Activated"
            assert hasattr(cmd, 'GetResources'), f"Comando {cmd_name} no tiene método GetResources"
        
        print(f"✅ {len(expected_commands)} comandos integrados correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error en integración de comandos: {e}")
        return False

def test_generation_flow():
    """Prueba el flujo completo de generación de modelos."""
    print("\n🔍 Testing: Flujo de generación...")
    
    try:
        from src.triptafittings.ui.dialog import TriptaFittingsDialog
        
        dialog = TriptaFittingsDialog()
        
        # Configurar selección
        if dialog.size_combo.count() > 0:
            dialog.size_combo.setCurrentIndex(0)
            dialog._on_size_changed()
            
            if dialog.current_preset:
                # Simular generación
                initial_models = len(dialog.generated_models)
                dialog._generate_model()
                final_models = len(dialog.generated_models)
                
                assert final_models > initial_models, "No se generó modelo"
                
                print(f"✅ Modelo generado exitosamente")
                return True
            else:
                print("⚠️ No hay preset válido para generar")
                return True
        else:
            print("⚠️ No hay tamaños disponibles para generar")
            return True
            
    except Exception as e:
        print(f"❌ Error en generación: {e}")
        return False

def main():
    """Ejecuta todos los tests."""
    print("🚀 Iniciando tests del diálogo TriptaFittings (Issue #10)")
    print("=" * 60)
    
    tests = [
        test_dialog_import,
        test_data_manager_integration,
        test_ui_components,
        test_dropdown_population,
        test_preset_loading,
        test_validation,
        test_commands_integration,
        test_generation_flow,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 60)
    print(f"📊 Resumen: {passed}/{total} tests pasados")
    
    if passed == total:
        print("🎉 ¡Todos los tests pasaron! Issue #10 implementado correctamente.")
        return True
    else:
        print(f"⚠️ {total - passed} tests fallaron. Revisar implementación.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
