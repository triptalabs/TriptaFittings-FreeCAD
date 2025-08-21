#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script principal para ejecutar todas las pruebas y demos de TriptaFittings
"""

import sys
import os
import subprocess

# Agregar el directorio raíz al path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.insert(0, root_dir)

def print_header():
    """Imprime el encabezado del script"""
    print("=" * 70)
    print("SISTEMA DE PRUEBAS Y DEMOS - TriptaFittings-FreeCAD")
    print("=" * 70)
    print("Este script ejecuta todas las pruebas y demos disponibles")
    print()

def run_script(script_path, description):
    """Ejecuta un script y muestra el resultado"""
    print(f"EJECUTANDO: {description}")
    print("-" * 50)
    
    try:
        # Configurar el entorno para el subproceso
        env = os.environ.copy()
        env['PYTHONPATH'] = root_dir + os.pathsep + env.get('PYTHONPATH', '')
        
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, timeout=60,
                              env=env, cwd=root_dir)
        
        if result.returncode == 0:
            print("SUCCESS: Ejecutado exitosamente")
            print(result.stdout)
        else:
            print("ERROR: Error en la ejecucion")
            print(f"Error: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("WARNING: Timeout en la ejecucion")
    except Exception as e:
        print(f"ERROR: {e}")
    
    print()

def main():
    """Función principal"""
    print_header()
    
    # Lista de scripts a ejecutar
    scripts = [
        {
            "path": os.path.join(current_dir, "testing", "test_basic.py"),
            "description": "PRUEBAS BASICAS DEL SISTEMA"
        },
        {
            "path": os.path.join(current_dir, "testing", "check_freecad_simple.py"),
            "description": "VERIFICACION DE INSTALACION DE FREECAD"
        },
        {
            "path": os.path.join(current_dir, "demos", "demo_automatic_simple.py"),
            "description": "DEMO AUTOMATICO DE FUNCIONALIDADES"
        }
    ]
    
    # Ejecutar cada script
    for script in scripts:
        if os.path.exists(script["path"]):
            run_script(script["path"], script["description"])
        else:
            print(f"ERROR: Script no encontrado: {script['path']}")
            print()
    
    # Resumen final
    print("=" * 70)
    print("RESUMEN DE EJECUCION")
    print("=" * 70)
    print("Todas las pruebas han sido ejecutadas")
    print("Revisa los resultados arriba para verificar el estado del sistema")
    print()
    print("PROXIMOS PASOS:")
    print("   1. Si todas las pruebas pasan: El sistema esta listo")
    print("   2. Si hay errores: Revisa la documentacion de instalacion")
    print("   3. Para mas demos: Ejecuta scripts/demos/demo_interactive.py")
    print("   4. Para integracion con FreeCAD: Instala FreeCAD y ejecuta test_freecad_integration.py")

if __name__ == "__main__":
    main()
