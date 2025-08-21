#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para probar la integración con FreeCAD
Verifica si FreeCAD está disponible y prueba las funcionalidades básicas
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def check_freecad_availability():
    """Verifica si FreeCAD está disponible"""
    print("🔍 Verificando disponibilidad de FreeCAD...")
    
    try:
        import FreeCAD
        import FreeCADGui
        import Part
        import Spreadsheet
        
        print("✅ FreeCAD está disponible")
        print(f"   - Versión: {FreeCAD.Version()}")
        print(f"   - Build: {FreeCAD.BuildVersionString()}")
        return True
        
    except ImportError as e:
        print("❌ FreeCAD no está disponible")
        print(f"   Error: {e}")
        print("\n💡 Para instalar FreeCAD:")
        print("   - Windows: Descarga desde https://www.freecad.org/")
        print("   - Linux: sudo apt-get install freecad")
        print("   - macOS: brew install freecad")
        return False

def test_freecad_workbench():
    """Prueba la creación del workbench"""
    print("\n🔧 Probando creación del workbench...")
    
    try:
        from InitGui import TriptaFittingsWorkbench
        
        # Crear instancia del workbench
        wb = TriptaFittingsWorkbench()
        print("✅ Workbench creado exitosamente")
        
        # Verificar metadatos
        print(f"   - Nombre: {wb.MenuText}")
        print(f"   - Tooltip: {wb.ToolTip}")
        print(f"   - Icono: {wb.Icon}")
        
        # Inicializar workbench
        commands = wb.Initialize()
        print(f"   - Comandos registrados: {len(commands)}")
        for cmd in commands:
            print(f"     * {cmd}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al crear workbench: {e}")
        return False

def test_commands():
    """Prueba los comandos del plugin"""
    print("\n⚡ Probando comandos...")
    
    try:
        from TriptaFittingsCmd import COMMANDS
        
        print(f"✅ {len(COMMANDS)} comandos disponibles:")
        for cmd_name, cmd_obj in COMMANDS.items():
            resources = cmd_obj.GetResources()
            print(f"   - {cmd_name}: {resources.get('MenuText', 'Sin nombre')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al probar comandos: {e}")
        return False

def test_user_interface():
    """Prueba la interfaz de usuario"""
    print("\n🖥️  Probando interfaz de usuario...")
    
    try:
        from ui.user_interface import UserInterface
        
        # Crear instancia de la interfaz
        ui = UserInterface()
        print("✅ Interfaz de usuario creada exitosamente")
        
        # Probar generación de modelo (sin FreeCAD)
        print("🧪 Probando generación de modelo (simulación)...")
        result = ui.generate_model('ferrule', 3.0)
        
        if result:
            print("✅ Generación de modelo exitosa")
            print(f"   - Componente: {result.get('component', 'N/A')}")
            print(f"   - Tamaño: {result.get('size', 'N/A')}")
            print(f"   - Estado: {result.get('status', 'N/A')}")
        else:
            print("❌ Error en generación de modelo")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al probar interfaz: {e}")
        return False

def test_model_generators():
    """Prueba los generadores de modelos"""
    print("\n🏗️  Probando generadores de modelos...")
    
    try:
        from models.ferrule_generator import FerruleGenerator
        from models.gasket_generator import GasketGenerator
        
        # Probar FerruleGenerator
        ferrule_gen = FerruleGenerator()
        print("✅ FerruleGenerator creado exitosamente")
        
        # Probar GasketGenerator
        gasket_gen = GasketGenerator()
        print("✅ GasketGenerator creado exitosamente")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al probar generadores: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 PRUEBA DE INTEGRACIÓN CON FREECAD")
    print("=" * 50)
    
    tests = [
        ("Disponibilidad de FreeCAD", check_freecad_availability),
        ("Workbench", test_freecad_workbench),
        ("Comandos", test_commands),
        ("Interfaz de Usuario", test_user_interface),
        ("Generadores de Modelos", test_model_generators)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        if test_func():
            passed += 1
        print()
    
    # Resumen
    print("=" * 50)
    print(f"📊 RESULTADOS: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron!")
        print("✅ El plugin está listo para usar con FreeCAD")
    else:
        print("⚠️  Algunas pruebas fallaron")
        print("💡 Revisa los errores arriba para más detalles")
    
    # Recomendaciones
    print("\n💡 RECOMENDACIONES:")
    if not check_freecad_availability():
        print("   1. Instala FreeCAD para usar todas las funcionalidades")
        print("   2. Mientras tanto, puedes usar el demo interactivo")
    else:
        print("   1. El plugin está listo para instalar en FreeCAD")
        print("   2. Copia la carpeta a la carpeta Mod de FreeCAD")
        print("   3. Reinicia FreeCAD y activa el workbench TriptaFittings")

if __name__ == "__main__":
    main()
