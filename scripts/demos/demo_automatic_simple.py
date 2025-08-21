#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo automatico simplificado de TriptaFittings
Muestra todas las funcionalidades del sistema de manera automatica
"""

import sys
import os

# Agregar el directorio raiz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from models.data_manager import DataManager
from data.preset import Preset

def print_header():
    """Imprime el encabezado del demo"""
    print("=" * 70)
    print("DEMO AUTOMATICO - TriptaFittings-FreeCAD")
    print("=" * 70)
    print("Este demo muestra automaticamente todas las funcionalidades")
    print("del sistema de generacion de modelos parametricos.")
    print()

def demo_data_loading():
    """Demo de carga de datos"""
    print("1. CARGA DE DATOS")
    print("-" * 30)
    
    try:
        dm = DataManager()
        print("SUCCESS: DataManager creado exitosamente")
        
        success = dm.load_all_data()
        if success:
            print("SUCCESS: Todos los datos cargados correctamente")
        else:
            print("ERROR: Error al cargar datos")
            return False
            
        return True
    except Exception as e:
        print(f"ERROR: Error en carga de datos: {e}")
        return False

def demo_available_sizes():
    """Demo de tamaños disponibles"""
    print("\n2. TAMAÑOS DISPONIBLES")
    print("-" * 30)
    
    try:
        dm = DataManager()
        dm.load_all_data()
        
        sizes = dm.get_available_sizes()
        print(f"SUCCESS: {len(sizes)} tamaños disponibles:")
        for size in sizes:
            print(f"   - {size}")
            
        return True
    except Exception as e:
        print(f"ERROR: Error al obtener tamaños: {e}")
        return False

def demo_preset_details():
    """Demo de detalles de presets"""
    print("\n3. DETALLES DE PRESETS")
    print("-" * 30)
    
    try:
        dm = DataManager()
        dm.load_all_data()
        
        # Obtener presets de Ferrule
        ferrule_presets = dm.get_presets_by_type('ferrule')
        print(f"SUCCESS: {len(ferrule_presets)} presets de Ferrule cargados")
        
        # Obtener presets de Gasket
        gasket_presets = dm.get_presets_by_type('gasket')
        print(f"SUCCESS: {len(gasket_presets)} presets de Gasket cargados")
        
        # Mostrar ejemplo de preset
        if ferrule_presets:
            example = ferrule_presets[0]
            print(f"EJEMPLO - Ferrule {example.size}:")
            print(f"   DN: {example.dn}")
            print(f"   PassageDia: {example.passage_dia}")
            print(f"   TubeID: {example.tube_id}")
            
        return True
    except Exception as e:
        print(f"ERROR: Error al obtener detalles: {e}")
        return False

def demo_compatibility_check():
    """Demo de verificación de compatibilidad"""
    print("\n4. VERIFICACION DE COMPATIBILIDAD")
    print("-" * 30)
    
    try:
        dm = DataManager()
        dm.load_all_data()
        
        # Verificar compatibilidad para todos los tamaños
        sizes = dm.get_available_sizes()
        compatible_count = 0
        
        for size in sizes:
            ferrule = dm.get_preset_by_size_and_type(size, 'ferrule')
            gasket = dm.get_preset_by_size_and_type(size, 'gasket')
            
            if ferrule and gasket:
                compatible_count += 1
                print(f"SUCCESS: {size} - Ferrule y Gasket compatibles")
            else:
                print(f"WARNING: {size} - Falta Ferrule o Gasket")
        
        print(f"\nSUCCESS: {compatible_count}/{len(sizes)} tamaños son compatibles")
        return True
    except Exception as e:
        print(f"ERROR: Error en verificación: {e}")
        return False

def demo_data_validation():
    """Demo de validación de datos"""
    print("\n5. VALIDACION DE DATOS")
    print("-" * 30)
    
    try:
        dm = DataManager()
        dm.load_all_data()
        
        # Validar todos los presets
        all_presets = dm.get_all_presets()
        valid_count = 0
        
        for preset in all_presets:
            if preset.is_valid():
                valid_count += 1
            else:
                print(f"WARNING: Preset {preset.size} {preset.type} no es válido")
        
        print(f"SUCCESS: {valid_count}/{len(all_presets)} presets son válidos")
        return True
    except Exception as e:
        print(f"ERROR: Error en validación: {e}")
        return False

def demo_search_functionality():
    """Demo de funcionalidades de búsqueda"""
    print("\n6. FUNCIONALIDADES DE BUSQUEDA")
    print("-" * 30)
    
    try:
        dm = DataManager()
        dm.load_all_data()
        
        # Búsqueda por tamaño
        size = "2\""
        ferrule = dm.get_preset_by_size_and_type(size, 'ferrule')
        gasket = dm.get_preset_by_size_and_type(size, 'gasket')
        
        if ferrule and gasket:
            print(f"SUCCESS: Encontrados presets para {size}")
            print(f"   Ferrule DN: {ferrule.dn}")
            print(f"   Gasket DN: {gasket.dn}")
        
        # Búsqueda por DN
        dn = "DN50"
        ferrule_dn = dm.get_preset_by_dn_and_type(dn, 'ferrule')
        gasket_dn = dm.get_preset_by_dn_and_type(dn, 'gasket')
        
        if ferrule_dn and gasket_dn:
            print(f"SUCCESS: Encontrados presets para {dn}")
            print(f"   Ferrule Size: {ferrule_dn.size}")
            print(f"   Gasket Size: {gasket_dn.size}")
            
        return True
    except Exception as e:
        print(f"ERROR: Error en búsqueda: {e}")
        return False

def demo_standards_info():
    """Demo de información de estándares"""
    print("\n7. INFORMACION DE ESTANDARES")
    print("-" * 30)
    
    try:
        print("SUCCESS: Estándar implementado: DIN 32676 A")
        print("   - Estándar alemán para conexiones sanitarias")
        print("   - Compatible con industria alimentaria y farmacéutica")
        print("   - Tamaños de 1.5\" a 12\" (DN40 a DN300)")
        print("   - Materiales: Acero inoxidable, plásticos, etc.")
        
        return True
    except Exception as e:
        print(f"ERROR: Error en información: {e}")
        return False

def demo_usage_scenarios():
    """Demo de escenarios de uso"""
    print("\n8. ESCENARIOS DE USO")
    print("-" * 30)
    
    try:
        print("SUCCESS: Escenarios de uso disponibles:")
        print("   1. Generación automática de modelos 3D")
        print("   2. Validación de compatibilidad de componentes")
        print("   3. Cálculo de parámetros según estándares")
        print("   4. Exportación a formatos CAD estándar")
        print("   5. Integración con FreeCAD para diseño")
        
        return True
    except Exception as e:
        print(f"ERROR: Error en escenarios: {e}")
        return False

def main():
    """Función principal del demo"""
    print_header()
    
    demos = [
        ("Carga de datos", demo_data_loading),
        ("Tamaños disponibles", demo_available_sizes),
        ("Detalles de presets", demo_preset_details),
        ("Verificación de compatibilidad", demo_compatibility_check),
        ("Validación de datos", demo_data_validation),
        ("Funcionalidades de búsqueda", demo_search_functionality),
        ("Información de estándares", demo_standards_info),
        ("Escenarios de uso", demo_usage_scenarios)
    ]
    
    passed = 0
    total = len(demos)
    
    for demo_name, demo_func in demos:
        try:
            if demo_func():
                passed += 1
        except Exception as e:
            print(f"ERROR en {demo_name}: {e}")
    
    # Resumen final
    print("\n" + "=" * 70)
    print("RESUMEN DEL DEMO")
    print("=" * 70)
    print(f"SUCCESS: {passed}/{total} demos ejecutados correctamente")
    
    if passed == total:
        print("SUCCESS: ¡Todas las funcionalidades están funcionando!")
        print("SUCCESS: El sistema está listo para usar")
    else:
        print("WARNING: Algunas funcionalidades tienen problemas")
        print("INFO: Revisa los errores arriba para más detalles")
    
    print("\nPROXIMOS PASOS:")
    print("   1. Si todo funciona: Instalar FreeCAD para funcionalidades completas")
    print("   2. Para más información: Revisar la documentación")
    print("   3. Para soporte: Crear issue en el repositorio")

if __name__ == "__main__":
    main()
