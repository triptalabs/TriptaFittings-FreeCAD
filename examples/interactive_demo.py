#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo interactivo de TriptaFittings
Permite explorar las funcionalidades del sistema de manera interactiva
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.data_manager import DataManager
from data.preset import Preset

def print_header():
    """Imprime el encabezado del demo"""
    print("=" * 60)
    print("🔧 DEMO INTERACTIVO - TriptaFittings-FreeCAD")
    print("=" * 60)
    print("Este demo te permite explorar las funcionalidades del sistema")
    print("de generación de modelos paramétricos de Ferrule y Gasket.")
    print()

def load_data():
    """Carga los datos del sistema"""
    print("📊 Cargando datos del sistema...")
    try:
        dm = DataManager()
        success = dm.load_all_data()
        
        if success:
            print("✅ Datos cargados exitosamente")
            return dm
        else:
            print("❌ Error al cargar datos")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def show_summary(dm):
    """Muestra un resumen de los datos cargados"""
    print("\n📈 RESUMEN DE DATOS")
    print("-" * 30)
    
    summary = dm.get_data_summary()
    print(f"✅ Estado: {'CARGADO' if summary['loaded'] else 'NO CARGADO'}")
    print(f"📦 Presets Ferrule: {summary['ferrule_count']}")
    print(f"📦 Presets Gasket: {summary['gasket_count']}")
    print(f"📏 Tamaños disponibles: {summary['available_sizes']}")
    print(f"🏷️  DNs disponibles: {summary['available_dns']}")
    
    if summary['errors']:
        print("⚠️  Errores encontrados:")
        for error in summary['errors']:
            print(f"   - {error}")

def show_available_sizes(dm):
    """Muestra los tamaños disponibles"""
    print("\n📏 TAMAÑOS DISPONIBLES")
    print("-" * 30)
    
    sizes = dm.get_available_sizes()
    for i, size in enumerate(sizes, 1):
        ferrule_preset = dm.get_preset_by_size('ferrule', size)
        gasket_preset = dm.get_preset_by_size('gasket', size)
        
        print(f"{i:2d}. {size:4.1f}\" → DN{ferrule_preset.dn[2:]} "
              f"(Ferrule: {ferrule_preset.flange_od_mm}mm, "
              f"Gasket: {gasket_preset.gasket_od_mm}mm)")

def show_preset_details(dm, component, size):
    """Muestra los detalles de un preset específico"""
    print(f"\n🔍 DETALLES DEL PRESET: {component.upper()} {size}\"")
    print("-" * 50)
    
    preset = dm.get_preset_by_size(component, size)
    if not preset:
        print(f"❌ No se encontró preset para {component} {size}\"")
        return
    
    print(f"📏 Tamaño: {preset.size}\"")
    print(f"🏷️  DN: {preset.dn}")
    print(f"📋 Estándar: {preset.standard}")
    print()
    
    if component == 'ferrule':
        print("📐 PARÁMETROS DE FERRULE:")
        print(f"   - Flange OD: {preset.flange_od_mm} mm")
        print(f"   - C2: {preset.c2_mm} mm")
        print(f"   - Tube ID: {preset.tube_id_mm} mm")
        print(f"   - Passage Dia: {preset.passage_dia_mm} mm")
        print(f"   - Height Tube: {preset.height_tube_mm} mm")
        print(f"   - Height Profile: {preset.height_profile_mm} mm")
        print(f"   - Seat Lip Width: {preset.seat_lip_width_mm} mm")
    
    elif component == 'gasket':
        print("📐 PARÁMETROS DE GASKET:")
        print(f"   - Flange OD: {preset.flange_od_mm} mm")
        print(f"   - Gasket OD: {preset.gasket_od_mm} mm")
        print(f"   - Gasket ID: {preset.gasket_id_mm} mm")
        print(f"   - Bead C2: {preset.bead_c2_mm} mm")
        print(f"   - Profile H: {preset.profile_h_mm} mm")
        print(f"   - Seat Lip Width: {preset.seat_lip_width_mm} mm")

def show_compatibility_check(dm, size):
    """Verifica la compatibilidad entre Ferrule y Gasket"""
    print(f"\n🔗 VERIFICACIÓN DE COMPATIBILIDAD: {size}\"")
    print("-" * 50)
    
    ferrule = dm.get_preset_by_size('ferrule', size)
    gasket = dm.get_preset_by_size('gasket', size)
    
    if not ferrule or not gasket:
        print("❌ No se pueden verificar los presets")
        return
    
    print("✅ Presets encontrados para ambos componentes")
    print()
    
    # Verificar dimensiones clave
    print("📐 COMPARACIÓN DE DIMENSIONES:")
    print(f"   Flange OD: Ferrule={ferrule.flange_od_mm}mm, Gasket={gasket.flange_od_mm}mm")
    print(f"   {'✅' if ferrule.flange_od_mm == gasket.flange_od_mm else '❌'} Compatibles")
    
    print(f"   C2: Ferrule={ferrule.c2_mm}mm, Gasket={gasket.bead_c2_mm}mm")
    print(f"   {'✅' if ferrule.c2_mm == gasket.bead_c2_mm else '❌'} Compatibles")
    
    print(f"   Seat Lip Width: Ferrule={ferrule.seat_lip_width_mm}mm, Gasket={gasket.seat_lip_width_mm}mm")
    print(f"   {'✅' if ferrule.seat_lip_width_mm == gasket.seat_lip_width_mm else '❌'} Compatibles")

def interactive_menu(dm):
    """Menú interactivo principal"""
    while True:
        print("\n" + "=" * 60)
        print("🎮 MENÚ INTERACTIVO")
        print("=" * 60)
        print("1. 📊 Mostrar resumen de datos")
        print("2. 📏 Ver tamaños disponibles")
        print("3. 🔍 Ver detalles de Ferrule")
        print("4. 🔍 Ver detalles de Gasket")
        print("5. 🔗 Verificar compatibilidad")
        print("6. 🧪 Ejecutar validación completa")
        print("0. 🚪 Salir")
        print("-" * 60)
        
        try:
            choice = input("Selecciona una opción (0-6): ").strip()
            
            if choice == '0':
                print("👋 ¡Hasta luego!")
                break
            elif choice == '1':
                show_summary(dm)
            elif choice == '2':
                show_available_sizes(dm)
            elif choice == '3':
                size = input("Ingresa el tamaño (ej: 3.0): ").strip()
                try:
                    size_float = float(size)
                    show_preset_details(dm, 'ferrule', size_float)
                except ValueError:
                    print("❌ Tamaño inválido")
            elif choice == '4':
                size = input("Ingresa el tamaño (ej: 3.0): ").strip()
                try:
                    size_float = float(size)
                    show_preset_details(dm, 'gasket', size_float)
                except ValueError:
                    print("❌ Tamaño inválido")
            elif choice == '5':
                size = input("Ingresa el tamaño (ej: 3.0): ").strip()
                try:
                    size_float = float(size)
                    show_compatibility_check(dm, size_float)
                except ValueError:
                    print("❌ Tamaño inválido")
            elif choice == '6':
                print("\n🧪 EJECUTANDO VALIDACIÓN COMPLETA...")
                integrity_results = dm.validate_data_integrity()
                for component, result in integrity_results.items():
                    status = "✅ VÁLIDO" if result['valid'] else "❌ INVÁLIDO"
                    print(f"   {component.capitalize()}: {status}")
                    if result['errors']:
                        for error in result['errors']:
                            print(f"      Error: {error}")
            else:
                print("❌ Opción inválida")
                
        except KeyboardInterrupt:
            print("\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Función principal"""
    print_header()
    
    # Cargar datos
    dm = load_data()
    if not dm:
        print("❌ No se pudieron cargar los datos. Saliendo...")
        return
    
    # Mostrar resumen inicial
    show_summary(dm)
    
    # Iniciar menú interactivo
    interactive_menu(dm)

if __name__ == "__main__":
    main()
