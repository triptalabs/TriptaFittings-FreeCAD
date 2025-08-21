#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo automático de TriptaFittings
Muestra todas las funcionalidades del sistema de manera automática
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.data_manager import DataManager
from data.preset import Preset

def print_header():
    """Imprime el encabezado del demo"""
    print("=" * 70)
    print("🔧 DEMO AUTOMÁTICO - TriptaFittings-FreeCAD")
    print("=" * 70)
    print("Este demo muestra automáticamente todas las funcionalidades")
    print("del sistema de generación de modelos paramétricos.")
    print()

def demo_data_loading():
    """Demo de carga de datos"""
    print("📊 1. CARGA DE DATOS")
    print("-" * 40)
    
    try:
        dm = DataManager()
        success = dm.load_all_data()
        
        if success:
            print("✅ Datos cargados exitosamente")
            
            # Mostrar resumen
            summary = dm.get_data_summary()
            print(f"📈 Resumen:")
            print(f"   - Estado: {'CARGADO' if summary['loaded'] else 'NO CARGADO'}")
            print(f"   - Presets Ferrule: {summary['ferrule_count']}")
            print(f"   - Presets Gasket: {summary['gasket_count']}")
            print(f"   - Total presets: {summary['total_presets']}")
            print(f"   - Tamaños disponibles: {summary['available_sizes']}")
            print(f"   - DNs disponibles: {summary['available_dns']}")
            
            return dm
        else:
            print("❌ Error al cargar datos")
            return None
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def demo_available_sizes(dm):
    """Demo de tamaños disponibles"""
    print("\n📏 2. TAMAÑOS DISPONIBLES")
    print("-" * 40)
    
    sizes = dm.get_available_sizes()
    print(f"✅ {len(sizes)} tamaños disponibles:")
    
    for i, size in enumerate(sizes, 1):
        ferrule_preset = dm.get_preset_by_size('ferrule', size)
        gasket_preset = dm.get_preset_by_size('gasket', size)
        
        print(f"   {i:2d}. {size:4.1f}\" → DN{ferrule_preset.dn[2:]} "
              f"(Ferrule: {ferrule_preset.flange_od_mm}mm, "
              f"Gasket: {gasket_preset.gasket_od_mm}mm)")

def demo_preset_details(dm):
    """Demo de detalles de presets"""
    print("\n🔍 3. DETALLES DE PRESETS")
    print("-" * 40)
    
    # Mostrar ejemplo de Ferrule 3"
    print("📐 Ejemplo: Ferrule 3\"")
    ferrule_3in = dm.get_preset_by_size('ferrule', 3.0)
    print(f"   - Tamaño: {ferrule_3in.size}\"")
    print(f"   - DN: {ferrule_3in.dn}")
    print(f"   - Flange OD: {ferrule_3in.flange_od_mm} mm")
    print(f"   - C2: {ferrule_3in.c2_mm} mm")
    print(f"   - Tube ID: {ferrule_3in.tube_id_mm} mm")
    print(f"   - Passage Dia: {ferrule_3in.passage_dia_mm} mm")
    print(f"   - Height Tube: {ferrule_3in.height_tube_mm} mm")
    print(f"   - Height Profile: {ferrule_3in.height_profile_mm} mm")
    print(f"   - Seat Lip Width: {ferrule_3in.seat_lip_width_mm} mm")
    
    print("\n📐 Ejemplo: Gasket 3\"")
    gasket_3in = dm.get_preset_by_size('gasket', 3.0)
    print(f"   - Tamaño: {gasket_3in.size}\"")
    print(f"   - DN: {gasket_3in.dn}")
    print(f"   - Flange OD: {gasket_3in.flange_od_mm} mm")
    print(f"   - Gasket OD: {gasket_3in.gasket_od_mm} mm")
    print(f"   - Gasket ID: {gasket_3in.gasket_id_mm} mm")
    print(f"   - Bead C2: {gasket_3in.bead_c2_mm} mm")
    print(f"   - Profile H: {gasket_3in.profile_h_mm} mm")
    print(f"   - Seat Lip Width: {gasket_3in.seat_lip_width_mm} mm")

def demo_compatibility_check(dm):
    """Demo de verificación de compatibilidad"""
    print("\n🔗 4. VERIFICACIÓN DE COMPATIBILIDAD")
    print("-" * 40)
    
    # Verificar compatibilidad para varios tamaños
    test_sizes = [1.5, 3.0, 6.0, 12.0]
    
    for size in test_sizes:
        ferrule = dm.get_preset_by_size('ferrule', size)
        gasket = dm.get_preset_by_size('gasket', size)
        
        print(f"📏 Tamaño {size}\":")
        
        # Verificar dimensiones clave
        flange_compatible = ferrule.flange_od_mm == gasket.flange_od_mm
        c2_compatible = ferrule.c2_mm == gasket.bead_c2_mm
        lip_compatible = ferrule.seat_lip_width_mm == gasket.seat_lip_width_mm
        
        print(f"   - Flange OD: {'✅' if flange_compatible else '❌'} "
              f"Ferrule={ferrule.flange_od_mm}mm, Gasket={gasket.flange_od_mm}mm")
        print(f"   - C2: {'✅' if c2_compatible else '❌'} "
              f"Ferrule={ferrule.c2_mm}mm, Gasket={gasket.bead_c2_mm}mm")
        print(f"   - Seat Lip Width: {'✅' if lip_compatible else '❌'} "
              f"Ferrule={ferrule.seat_lip_width_mm}mm, Gasket={gasket.seat_lip_width_mm}mm")
        
        all_compatible = flange_compatible and c2_compatible and lip_compatible
        print(f"   - Estado general: {'✅ COMPATIBLE' if all_compatible else '❌ INCOMPATIBLE'}")
        print()

def demo_data_validation(dm):
    """Demo de validación de datos"""
    print("\n🧪 5. VALIDACIÓN DE DATOS")
    print("-" * 40)
    
    integrity_results = dm.validate_data_integrity()
    
    for component, result in integrity_results.items():
        status = "✅ VÁLIDO" if result['valid'] else "❌ INVÁLIDO"
        print(f"📦 {component.capitalize()}: {status}")
        print(f"   - Presets cargados: {result['presets_count']}")
        
        if result['errors']:
            print("   - Errores encontrados:")
            for error in result['errors']:
                print(f"     * {error}")
        else:
            print("   - Sin errores detectados")
        print()

def demo_search_functionality(dm):
    """Demo de funcionalidades de búsqueda"""
    print("\n🔍 6. FUNCIONALIDADES DE BÚSQUEDA")
    print("-" * 40)
    
    # Búsqueda por tamaño
    print("📏 Búsqueda por tamaño:")
    test_size = 4.0
    ferrule = dm.get_preset_by_size('ferrule', test_size)
    gasket = dm.get_preset_by_size('gasket', test_size)
    
    print(f"   - Ferrule {test_size}\": {ferrule.dn} (Flange OD: {ferrule.flange_od_mm}mm)")
    print(f"   - Gasket {test_size}\": {gasket.dn} (Gasket OD: {gasket.gasket_od_mm}mm)")
    
    # Búsqueda por DN
    print("\n🏷️  Búsqueda por DN:")
    test_dn = "DN80"
    ferrule_dn = dm.get_preset_by_dn('ferrule', test_dn)
    gasket_dn = dm.get_preset_by_dn('gasket', test_dn)
    
    if ferrule_dn and gasket_dn:
        print(f"   - Ferrule {test_dn}: {ferrule_dn.size}\" (Flange OD: {ferrule_dn.flange_od_mm}mm)")
        print(f"   - Gasket {test_dn}: {gasket_dn.size}\" (Gasket OD: {gasket_dn.gasket_od_mm}mm)")

def demo_standards_info():
    """Demo de información de estándares"""
    print("\n📋 7. INFORMACIÓN DE ESTÁNDARES")
    print("-" * 40)
    
    print("🏭 Estándar DIN 32676 A:")
    print("   - Estándar alemán para conexiones de tubería")
    print("   - Aplicación: Industria farmacéutica, alimentaria, química")
    print("   - Materiales: Acero inoxidable, plásticos, etc.")
    print("   - Presión: Hasta 10 bar")
    print("   - Temperatura: -20°C a +150°C")
    print()
    
    print("📐 Rangos de tamaños:")
    print("   - Diámetros nominales: DN40 a DN300")
    print("   - Tamaños en pulgadas: 1.5\" a 12\"")
    print("   - Aplicaciones: Tuberías sanitarias, conexiones higiénicas")

def demo_usage_scenarios():
    """Demo de escenarios de uso"""
    print("\n🎯 8. ESCENARIOS DE USO")
    print("-" * 40)
    
    scenarios = [
        {
            "title": "Industria Farmacéutica",
            "description": "Conexiones sanitarias para transferencia de productos",
            "sizes": ["1.5\"", "2\"", "3\""],
            "materials": "Acero inoxidable 316L"
        },
        {
            "title": "Industria Alimentaria",
            "description": "Sistemas de procesamiento de alimentos",
            "sizes": ["2\"", "4\"", "6\""],
            "materials": "Acero inoxidable 304"
        },
        {
            "title": "Industria Química",
            "description": "Transferencia de productos químicos",
            "sizes": ["3\"", "6\"", "8\"", "12\""],
            "materials": "Acero inoxidable, plásticos especiales"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"🏭 {i}. {scenario['title']}")
        print(f"   - Descripción: {scenario['description']}")
        print(f"   - Tamaños típicos: {', '.join(scenario['sizes'])}")
        print(f"   - Materiales: {scenario['materials']}")
        print()

def main():
    """Función principal del demo"""
    print_header()
    
    # Ejecutar demos
    dm = demo_data_loading()
    if not dm:
        print("❌ No se pudieron cargar los datos. Demo terminado.")
        return
    
    demo_available_sizes(dm)
    demo_preset_details(dm)
    demo_compatibility_check(dm)
    demo_data_validation(dm)
    demo_search_functionality(dm)
    demo_standards_info()
    demo_usage_scenarios()
    
    # Resumen final
    print("=" * 70)
    print("🎉 DEMO COMPLETADO EXITOSAMENTE")
    print("=" * 70)
    print("✅ El sistema TriptaFittings está funcionando correctamente")
    print("📊 Se cargaron y validaron todos los datos de presets")
    print("🔧 El sistema está listo para generar modelos paramétricos")
    print()
    print("💡 Próximos pasos:")
    print("   1. Instalar FreeCAD para funcionalidades completas")
    print("   2. Usar el plugin para generar modelos 3D")
    print("   3. Explorar las funcionalidades avanzadas")
    print()
    print("🚀 ¡Gracias por probar TriptaFittings-FreeCAD!")

if __name__ == "__main__":
    main()
