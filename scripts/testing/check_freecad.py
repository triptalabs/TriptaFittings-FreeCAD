#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar la instalación de FreeCAD
"""

import sys
import os
import subprocess

def print_header():
    """Imprime el encabezado"""
    print("🔍 VERIFICACIÓN DE INSTALACIÓN DE FREECAD")
    print("=" * 50)

def check_freecad_command():
    """Verifica si el comando freecad está disponible"""
    print("📋 1. Verificando comando 'freecad'...")
    
    try:
        result = subprocess.run(['freecad', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Comando 'freecad' disponible")
            print(f"   Salida: {result.stdout.strip()}")
            return True
        else:
            print("❌ Comando 'freecad' no funciona correctamente")
            return False
    except FileNotFoundError:
        print("❌ Comando 'freecad' no encontrado en PATH")
        return False
    except subprocess.TimeoutExpired:
        print("⚠️  Timeout al ejecutar freecad")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def check_freecad_installation_paths():
    """Verifica rutas de instalación comunes"""
    print("\n📁 2. Verificando rutas de instalación...")
    
    common_paths = [
        r"C:\Program Files\FreeCAD\bin\freecad.exe",
        r"C:\Program Files (x86)\FreeCAD\bin\freecad.exe",
        r"C:\FreeCAD\bin\freecad.exe",
        os.path.expanduser(r"~\AppData\Local\Programs\FreeCAD\bin\freecad.exe")
    ]
    
    found_paths = []
    for path in common_paths:
        if os.path.exists(path):
            found_paths.append(path)
            print(f"✅ Encontrado: {path}")
    
    if not found_paths:
        print("❌ No se encontró FreeCAD en rutas comunes")
        print("💡 FreeCAD no está instalado o está en una ubicación diferente")
        return False
    
    return True

def check_python_import():
    """Verifica si Python puede importar FreeCAD"""
    print("\n🐍 3. Verificando importación desde Python...")
    
    try:
        import FreeCAD
        print("✅ FreeCAD importado correctamente desde Python")
        print(f"   Versión: {FreeCAD.Version()}")
        print(f"   Build: {FreeCAD.BuildVersionString()}")
        return True
    except ImportError as e:
        print(f"❌ Error al importar FreeCAD: {e}")
        print("💡 FreeCAD no está en el PATH de Python")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def check_freecad_modules():
    """Verifica módulos importantes de FreeCAD"""
    print("\n🔧 4. Verificando módulos de FreeCAD...")
    
    try:
        import FreeCAD
        import Part
        import Spreadsheet
        
        print("✅ Módulos básicos importados correctamente")
        
        # Verificar funcionalidad básica
        doc = FreeCAD.newDocument("Test")
        print("✅ Creación de documento exitosa")
        
        box = Part.makeBox(10, 10, 10)
        print("✅ Creación de objeto 3D exitosa")
        
        sheet = doc.addObject('Spreadsheet::Sheet', 'TestSheet')
        print("✅ Creación de spreadsheet exitosa")
        
        FreeCAD.closeDocument("Test")
        print("✅ Cierre de documento exitoso")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en módulos: {e}")
        return False

def check_freecad_python_path():
    """Verifica el PATH de Python de FreeCAD"""
    print("\n🔍 5. Verificando PATH de Python...")
    
    try:
        import sys
        print(f"Python ejecutable: {sys.executable}")
        print(f"Python version: {sys.version}")
        
        # Buscar rutas relacionadas con FreeCAD
        freecad_paths = [path for path in sys.path if 'freecad' in path.lower()]
        
        if freecad_paths:
            print("✅ Rutas de FreeCAD encontradas en sys.path:")
            for path in freecad_paths:
                print(f"   - {path}")
        else:
            print("⚠️  No se encontraron rutas de FreeCAD en sys.path")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al verificar PATH: {e}")
        return False

def provide_installation_instructions():
    """Proporciona instrucciones de instalación"""
    print("\n📋 INSTRUCCIONES DE INSTALACIÓN")
    print("-" * 40)
    
    print("🔧 Para instalar FreeCAD en Windows:")
    print()
    print("1. 📥 Descargar desde: https://www.freecad.org/downloads.php")
    print("2. 🖥️  Ejecutar instalador como administrador")
    print("3. ✅ Marcar 'Add FreeCAD to PATH'")
    print("4. 🔄 Reiniciar Command Prompt")
    print("5. 🧪 Ejecutar este script nuevamente")
    print()
    print("💡 Alternativas:")
    print("   - Chocolatey: choco install freecad")
    print("   - Conda: conda install -c conda-forge freecad")

def main():
    """Función principal"""
    print_header()
    
    checks = [
        ("Comando freecad", check_freecad_command),
        ("Rutas de instalación", check_freecad_installation_paths),
        ("Importación Python", check_python_import),
        ("Módulos de FreeCAD", check_freecad_modules),
        ("PATH de Python", check_freecad_python_path)
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_func in checks:
        try:
            if check_func():
                passed += 1
        except Exception as e:
            print(f"❌ Error en {check_name}: {e}")
    
    # Resumen
    print("\n" + "=" * 50)
    print(f"📊 RESULTADOS: {passed}/{total} verificaciones pasaron")
    
    if passed == total:
        print("🎉 ¡FreeCAD está correctamente instalado!")
        print("✅ Puedes usar TriptaFittings con todas las funcionalidades")
    elif passed >= 3:
        print("⚠️  FreeCAD está parcialmente instalado")
        print("💡 Algunas funcionalidades pueden no estar disponibles")
    else:
        print("❌ FreeCAD no está correctamente instalado")
        provide_installation_instructions()
    
    # Recomendaciones
    print("\n💡 RECOMENDACIONES:")
    if passed >= 3:
        print("   1. ✅ FreeCAD está listo para usar")
        print("   2. 🧪 Ejecutar: python test_freecad_integration.py")
        print("   3. 🚀 Instalar plugin TriptaFittings")
    else:
        print("   1. 📥 Instalar FreeCAD siguiendo las instrucciones")
        print("   2. 🔄 Reiniciar Command Prompt")
        print("   3. 🧪 Ejecutar este script nuevamente")

if __name__ == "__main__":
    main()
