#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de instalación automática para TriptaFittings-FreeCAD
Instala el plugin en el directorio Mod correcto de FreeCAD
"""

import os
import shutil
import sys
from pathlib import Path

def print_header(title):
    print("=" * 60)
    print(f"🔧 {title}")
    print("=" * 60)

def find_freecad_mod_directory():
    """Encuentra el directorio Mod de FreeCAD"""
    print_header("BUSCANDO DIRECTORIO MOD DE FREECAD")
    
    # Rutas posibles para el directorio Mod
    possible_paths = [
        os.path.expanduser(r"~\AppData\Roaming\FreeCAD\Mod"),
        os.path.expanduser(r"~\AppData\Local\FreeCAD\Mod"),
        r"C:\Program Files\FreeCAD\Mod",
        r"C:\Program Files (x86)\FreeCAD\Mod",
        os.path.expanduser(r"~\AppData\Local\Programs\FreeCAD\Mod")
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            print(f"✅ Encontrado directorio Mod: {path}")
            return path
    
    print("❌ No se encontró ningún directorio Mod de FreeCAD")
    print("\n📋 SOLUCIONES:")
    print("1. Instala FreeCAD desde: https://www.freecad.org/downloads.php")
    print("2. O crea manualmente el directorio:")
    print("   %APPDATA%\\FreeCAD\\Mod")
    return None

def create_mod_directory():
    """Crea el directorio Mod si no existe"""
    mod_path = os.path.expanduser(r"~\AppData\Roaming\FreeCAD\Mod")
    
    if not os.path.exists(mod_path):
        print(f"📁 Creando directorio Mod: {mod_path}")
        os.makedirs(mod_path, exist_ok=True)
        return mod_path
    
    return mod_path

def install_plugin():
    """Instala el plugin en el directorio Mod"""
    print_header("INSTALACIÓN DEL PLUGIN")
    
    # Obtener directorio actual (donde está el plugin)
    current_dir = Path(__file__).parent.absolute()
    print(f"Directorio del plugin: {current_dir}")
    
    # Encontrar o crear directorio Mod
    mod_dir = find_freecad_mod_directory()
    if not mod_dir:
        mod_dir = create_mod_directory()
    
    # Directorio destino para el plugin
    plugin_dest = Path(mod_dir) / "TriptaFittings"
    print(f"Directorio destino: {plugin_dest}")
    
    # Verificar si ya existe
    if plugin_dest.exists():
        print("⚠️  El plugin ya existe en el directorio Mod")
        response = input("¿Deseas sobrescribir? (s/n): ").lower()
        if response != 's':
            print("❌ Instalación cancelada")
            return False
        
        # Eliminar instalación anterior
        shutil.rmtree(plugin_dest)
        print("🗑️  Instalación anterior eliminada")
    
    try:
        # Copiar plugin al directorio Mod
        print("📋 Copiando archivos...")
        shutil.copytree(current_dir, plugin_dest)
        print("✅ Plugin copiado correctamente")
        
        # Verificar archivos importantes
        required_files = [
            "__init__.py",
            "InitGui.py",
            "TriptaFittingsGui.py", 
            "TriptaFittingsCmd.py",
            "package.xml"
        ]
        
        missing_files = []
        for file in required_files:
            if not (plugin_dest / file).exists():
                missing_files.append(file)
        
        if missing_files:
            print(f"❌ Archivos faltantes: {missing_files}")
            return False
        
        print("✅ Todos los archivos requeridos están presentes")
        return True
        
    except Exception as e:
        print(f"❌ Error durante la instalación: {e}")
        return False

def create_activation_script():
    """Crea un script para activar el plugin en FreeCAD"""
    print_header("CREANDO SCRIPT DE ACTIVACIÓN")
    
    script_content = '''# -*- coding: utf-8 -*-
"""
Script para activar TriptaFittings en FreeCAD
Ejecuta este script en la consola de Python de FreeCAD
"""

try:
    # Importar el workbench
    import TriptaFittings.InitGui
    
    # Registrar el workbench
    Gui.addWorkbench(TriptaFittings.InitGui.TriptaFittingsWorkbench())
    
    print("✅ TriptaFittings activado correctamente")
    print("   Ve a View → Workbenches → TriptaFittings")
    
except Exception as e:
    print(f"❌ Error al activar TriptaFittings: {e}")
    print("   Verifica que el plugin esté instalado correctamente")
'''
    
    script_path = Path(__file__).parent / "activate_triptafittings.py"
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print(f"✅ Script de activación creado: {script_path}")
    return script_path

def main():
    """Función principal de instalación"""
    print("🚀 INSTALADOR AUTOMÁTICO - TriptaFittings-FreeCAD")
    print("=" * 60)
    
    # Instalar plugin
    if not install_plugin():
        print("\n❌ La instalación falló")
        return
    
    # Crear script de activación
    script_path = create_activation_script()
    
    # Instrucciones finales
    print_header("INSTALACIÓN COMPLETADA")
    print("✅ El plugin ha sido instalado correctamente")
    print("\n📋 PRÓXIMOS PASOS:")
    print("1. Reinicia FreeCAD completamente")
    print("2. Ve a View → Workbenches → TriptaFittings")
    print("3. Si no aparece, ejecuta en la consola de Python de FreeCAD:")
    print(f"   exec(open(r'{script_path}').read())")
    print("\n🔧 SOLUCIÓN DE PROBLEMAS:")
    print("- Si el plugin no aparece, verifica que FreeCAD esté en el PATH")
    print("- Si hay errores, revisa la consola de Python de FreeCAD")
    print("- Para más ayuda, ejecuta: python diagnose_plugin.py")

if __name__ == "__main__":
    main()
