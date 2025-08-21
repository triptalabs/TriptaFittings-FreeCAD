#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de diagnóstico para TriptaFittings-FreeCAD
Verifica por qué el plugin no aparece en FreeCAD
"""

import os
import sys
import traceback
from pathlib import Path

def print_header(title):
    print("=" * 60)
    print(f"🔍 {title}")
    print("=" * 60)

def check_freecad_installation():
    """Verifica si FreeCAD está instalado y accesible"""
    print_header("VERIFICACIÓN DE INSTALACIÓN DE FREECAD")
    
    try:
        import FreeCAD
        print("✅ FreeCAD importado correctamente")
        print(f"   Versión: {FreeCAD.Version()}")
        print(f"   Build: {FreeCAD.BuildVersionString()}")
        return True
    except ImportError as e:
        print(f"❌ Error al importar FreeCAD: {e}")
        print("   FreeCAD no está instalado o no está en el PATH")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def check_plugin_structure():
    """Verifica la estructura del plugin"""
    print_header("VERIFICACIÓN DE ESTRUCTURA DEL PLUGIN")
    
    current_dir = Path(__file__).parent
    required_files = [
        "__init__.py",
        "InitGui.py", 
        "TriptaFittingsGui.py",
        "TriptaFittingsCmd.py",
        "package.xml"
    ]
    
    missing_files = []
    for file in required_files:
        file_path = current_dir / file
        if file_path.exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - FALTANTE")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Archivos faltantes: {missing_files}")
        return False
    else:
        print("\n✅ Todos los archivos requeridos están presentes")
        return True

def check_plugin_imports():
    """Verifica que el plugin se pueda importar correctamente"""
    print_header("VERIFICACIÓN DE IMPORTS DEL PLUGIN")
    
    try:
        # Agregar el directorio actual al path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, current_dir)
        
        # Intentar importar módulos del plugin
        import __init__
        print("✅ __init__.py importado correctamente")
        
        import InitGui
        print("✅ InitGui.py importado correctamente")
        
        import TriptaFittingsGui
        print("✅ TriptaFittingsGui.py importado correctamente")
        
        import TriptaFittingsCmd
        print("✅ TriptaFittingsCmd.py importado correctamente")
        
        # Verificar que la clase workbench existe
        workbench = InitGui.TriptaFittingsWorkbench()
        print("✅ TriptaFittingsWorkbench creado correctamente")
        print(f"   MenuText: {workbench.MenuText}")
        print(f"   ToolTip: {workbench.ToolTip}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al importar plugin: {e}")
        print("   Traceback:")
        traceback.print_exc()
        return False

def check_freecad_paths():
    """Verifica las rutas de instalación de FreeCAD"""
    print_header("VERIFICACIÓN DE RUTAS DE FREECAD")
    
    # Rutas comunes de FreeCAD en Windows
    common_paths = [
        r"C:\Program Files\FreeCAD\bin",
        r"C:\Program Files (x86)\FreeCAD\bin",
        r"C:\FreeCAD\bin",
        os.path.expanduser(r"~\AppData\Local\Programs\FreeCAD\bin")
    ]
    
    found_paths = []
    for path in common_paths:
        if os.path.exists(path):
            found_paths.append(path)
            print(f"✅ Encontrado: {path}")
        else:
            print(f"❌ No encontrado: {path}")
    
    if not found_paths:
        print("\n⚠️  No se encontró FreeCAD en rutas comunes")
        print("   Instala FreeCAD desde: https://www.freecad.org/downloads.php")
        return False
    
    return True

def check_mod_directory():
    """Verifica si el plugin está en el directorio Mod correcto"""
    print_header("VERIFICACIÓN DE DIRECTORIO MOD")
    
    current_dir = Path(__file__).parent.absolute()
    print(f"Directorio actual: {current_dir}")
    
    # Verificar si estamos en un directorio Mod
    mod_paths = [
        os.path.expanduser(r"~\AppData\Roaming\FreeCAD\Mod"),
        os.path.expanduser(r"~\AppData\Local\FreeCAD\Mod"),
        r"C:\Program Files\FreeCAD\Mod",
        r"C:\Program Files (x86)\FreeCAD\Mod"
    ]
    
    in_mod_directory = False
    for mod_path in mod_paths:
        if current_dir == Path(mod_path) / "TriptaFittings":
            print(f"✅ Plugin está en directorio Mod correcto: {mod_path}")
            in_mod_directory = True
            break
    
    if not in_mod_directory:
        print("❌ Plugin NO está en el directorio Mod correcto")
        print("\n📋 INSTRUCCIONES DE INSTALACIÓN:")
        print("1. Copia toda la carpeta del plugin a:")
        print("   %APPDATA%\\FreeCAD\\Mod\\TriptaFittings")
        print("2. Reinicia FreeCAD")
        print("3. Ve a View → Workbenches → TriptaFittings")
        return False
    
    return True

def check_package_xml():
    """Verifica el archivo package.xml"""
    print_header("VERIFICACIÓN DE PACKAGE.XML")
    
    try:
        import xml.etree.ElementTree as ET
        tree = ET.parse('package.xml')
        root = tree.getroot()
        
        # Verificar elementos importantes
        name = root.find('name')
        if name is not None:
            print(f"✅ Nombre del plugin: {name.text}")
        
        classname = root.find('classname')
        if classname is not None:
            print(f"✅ Clase workbench: {classname.text}")
        
        version = root.find('version')
        if version is not None:
            print(f"✅ Versión: {version.text}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al leer package.xml: {e}")
        return False

def check_workbench_registration():
    """Verifica si el workbench se puede registrar correctamente"""
    print_header("VERIFICACIÓN DE REGISTRO DE WORKBENCH")
    
    try:
        import InitGui
        workbench = InitGui.TriptaFittingsWorkbench()
        
        # Verificar métodos requeridos
        methods = ['Initialize', 'GetClassName', 'Activated', 'Deactivated']
        for method in methods:
            if hasattr(workbench, method):
                print(f"✅ Método {method} presente")
            else:
                print(f"❌ Método {method} faltante")
                return False
        
        # Verificar atributos requeridos
        attributes = ['MenuText', 'ToolTip', 'Icon']
        for attr in attributes:
            if hasattr(workbench, attr):
                print(f"✅ Atributo {attr} presente: {getattr(workbench, attr)}")
            else:
                print(f"❌ Atributo {attr} faltante")
                return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error al verificar workbench: {e}")
        return False

def main():
    """Función principal de diagnóstico"""
    print("🔧 DIAGNÓSTICO COMPLETO - TriptaFittings-FreeCAD")
    print("=" * 60)
    
    checks = [
        ("FreeCAD Installation", check_freecad_installation),
        ("Plugin Structure", check_plugin_structure),
        ("Plugin Imports", check_plugin_imports),
        ("FreeCAD Paths", check_freecad_paths),
        ("Mod Directory", check_mod_directory),
        ("Package XML", check_package_xml),
        ("Workbench Registration", check_workbench_registration)
    ]
    
    results = []
    for check_name, check_func in checks:
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"❌ Error en {check_name}: {e}")
            results.append((check_name, False))
        print()
    
    # Resumen final
    print_header("RESUMEN DE DIAGNÓSTICO")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for check_name, result in results:
        status = "✅ PASÓ" if result else "❌ FALLÓ"
        print(f"{status} {check_name}")
    
    print(f"\n📊 Resultado: {passed}/{total} verificaciones pasaron")
    
    if passed == total:
        print("\n🎉 ¡El plugin debería funcionar correctamente!")
        print("   Si aún no aparece en FreeCAD:")
        print("   1. Reinicia FreeCAD completamente")
        print("   2. Ve a View → Workbenches → TriptaFittings")
        print("   3. Verifica que no hay errores en la consola de FreeCAD")
    else:
        print("\n⚠️  Se encontraron problemas:")
        print("   1. Revisa los errores arriba")
        print("   2. Sigue las instrucciones de corrección")
        print("   3. Ejecuta este diagnóstico nuevamente")

if __name__ == "__main__":
    main()
