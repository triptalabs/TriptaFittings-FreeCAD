#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simplificado para verificar la instalacion de FreeCAD
"""

import sys
import os
import subprocess

def print_header():
    """Imprime el encabezado"""
    print("VERIFICACION DE INSTALACION DE FREECAD")
    print("=" * 50)

def check_freecad_command():
    """Verifica si el comando freecad esta disponible"""
    print("1. Verificando comando 'freecad'...")
    
    try:
        result = subprocess.run(['freecad', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("SUCCESS: Comando 'freecad' disponible")
            print(f"   Salida: {result.stdout.strip()}")
            return True
        else:
            print("ERROR: Comando 'freecad' no funciona correctamente")
            return False
    except FileNotFoundError:
        print("ERROR: Comando 'freecad' no encontrado en PATH")
        return False
    except subprocess.TimeoutExpired:
        print("WARNING: Timeout al ejecutar freecad")
        return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def check_freecad_installation_paths():
    """Verifica rutas de instalacion comunes"""
    print("\n2. Verificando rutas de instalacion...")
    
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
            print(f"SUCCESS: Encontrado: {path}")
    
    if not found_paths:
        print("ERROR: No se encontro FreeCAD en rutas comunes")
        print("INFO: FreeCAD no esta instalado o esta en una ubicacion diferente")
        return False
    
    return True

def check_python_import():
    """Verifica si Python puede importar FreeCAD"""
    print("\n3. Verificando importacion desde Python...")
    
    try:
        import FreeCAD
        print("SUCCESS: FreeCAD importado correctamente desde Python")
        print(f"   Version: {FreeCAD.Version()}")
        print(f"   Build: {FreeCAD.BuildVersionString()}")
        return True
    except ImportError as e:
        print(f"ERROR: Error al importar FreeCAD: {e}")
        print("INFO: FreeCAD no esta en el PATH de Python")
        return False
    except Exception as e:
        print(f"ERROR: Error inesperado: {e}")
        return False

def provide_installation_instructions():
    """Proporciona instrucciones de instalacion"""
    print("\nINSTRUCCIONES DE INSTALACION")
    print("-" * 40)
    
    print("Para instalar FreeCAD en Windows:")
    print()
    print("1. Descargar desde: https://www.freecad.org/downloads.php")
    print("2. Ejecutar instalador como administrador")
    print("3. Marcar 'Add FreeCAD to PATH'")
    print("4. Reiniciar Command Prompt")
    print("5. Ejecutar este script nuevamente")
    print()
    print("Alternativas:")
    print("   - Chocolatey: choco install freecad")
    print("   - Conda: conda install -c conda-forge freecad")

def main():
    """Funcion principal"""
    print_header()
    
    checks = [
        ("Comando freecad", check_freecad_command),
        ("Rutas de instalacion", check_freecad_installation_paths),
        ("Importacion Python", check_python_import)
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_func in checks:
        try:
            if check_func():
                passed += 1
        except Exception as e:
            print(f"ERROR en {check_name}: {e}")
    
    # Resumen
    print("\n" + "=" * 50)
    print(f"RESULTADOS: {passed}/{total} verificaciones pasaron")
    
    if passed == total:
        print("SUCCESS: FreeCAD esta correctamente instalado!")
        print("SUCCESS: Puedes usar TriptaFittings con todas las funcionalidades")
    elif passed >= 2:
        print("WARNING: FreeCAD esta parcialmente instalado")
        print("INFO: Algunas funcionalidades pueden no estar disponibles")
    else:
        print("ERROR: FreeCAD no esta correctamente instalado")
        provide_installation_instructions()
    
    # Recomendaciones
    print("\nRECOMENDACIONES:")
    if passed >= 2:
        print("   1. SUCCESS: FreeCAD esta listo para usar")
        print("   2. TEST: Ejecutar: python test_freecad_integration.py")
        print("   3. INSTALL: Instalar plugin TriptaFittings")
    else:
        print("   1. INSTALL: Instalar FreeCAD siguiendo las instrucciones")
        print("   2. RESTART: Reiniciar Command Prompt")
        print("   3. TEST: Ejecutar este script nuevamente")

if __name__ == "__main__":
    main()
