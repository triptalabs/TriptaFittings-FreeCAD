#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para validar el Sprint 1: Core del Sistema de Datos
Ejecuta tests con los datos reales de los archivos CSV
"""

import sys
import os
import logging
from pathlib import Path

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.data_manager import DataManager
from data.preset import Preset


class Sprint1TestError(Exception):
    """Errores específicos de las pruebas del Sprint 1"""
    pass


def test_sprint1_complete():
    """Test completo del Sprint 1 con datos reales"""
    print("🚀 Iniciando validación del Sprint 1: Core del Sistema de Datos")
    print("=" * 60)
    
    # 1. Test inicialización del DataManager
    print("\n📋 1. Inicializando DataManager...")
    try:
        data_manager = DataManager()
        print("✅ DataManager inicializado correctamente")
    except Exception as e:
        raise Sprint1TestError(f"Error al inicializar DataManager: {e}")
    
    # 2. Test validación de integridad de datos
    print("\n🔍 2. Validando integridad de datos CSV...")
    try:
        integrity_results = data_manager.validate_data_integrity()
        
        print(f"📊 Resultados de validación:")
        for component, result in integrity_results.items():
            status = "✅ VÁLIDO" if result['valid'] else "❌ INVÁLIDO"
            print(f"   {component.capitalize()}: {status}")
            if result['errors']:
                for error in result['errors']:
                    print(f"      Error: {error}")
            print(f"   Presets cargados: {result['presets_count']}")
        
        # Verificar que ambos componentes son válidos
        assert (
            integrity_results['ferrule']['valid']
            and integrity_results['gasket']['valid']
        ), "Algunos archivos CSV tienen errores"
        
        print("✅ Validación de integridad completada")
        
    except Exception as e:
        raise Sprint1TestError(f"Error en validación de integridad: {e}")
    
    # 3. Test carga de todos los datos
    print("\n📥 3. Cargando todos los datos...")
    try:
        success = data_manager.load_all_data()
        assert success, "Error al cargar datos"
        
        print("✅ Datos cargados exitosamente")
        
    except Exception as e:
        raise Sprint1TestError(f"Error al cargar datos: {e}")
    
    # 4. Test resumen de datos
    print("\n📊 4. Obteniendo resumen de datos...")
    try:
        summary = data_manager.get_data_summary()
        
        print(f"📈 Resumen de datos:")
        print(f"   Estado: {'✅ CARGADO' if summary['loaded'] else '❌ NO CARGADO'}")
        print(f"   Presets Ferrule: {summary['ferrule_count']}")
        print(f"   Presets Gasket: {summary['gasket_count']}")
        print(f"   Total presets: {summary['total_presets']}")
        print(f"   Tamaños disponibles: {summary['available_sizes']}")
        print(f"   DNs disponibles: {summary['available_dns']}")
        
        if summary['errors']:
            print("⚠️  Errores encontrados:")
            for error in summary['errors']:
                print(f"      {error}")
        
        print("✅ Resumen obtenido correctamente")
        
    except Exception as e:
        raise Sprint1TestError(f"Error al obtener resumen: {e}")
    
    # 5. Test búsquedas por tamaño
    print("\n🔍 5. Probando búsquedas por tamaño...")
    try:
        available_sizes = data_manager.get_available_sizes()
        
        for size in available_sizes[:3]:  # Probar los primeros 3 tamaños
            print(f"\n   Probando tamaño: {size}\"")
            
            # Buscar Ferrule
            ferrule = data_manager.get_preset_by_size('ferrule', size)
            if ferrule:
                print(f"      ✅ Ferrule encontrado: {ferrule.get_name()}")
                print(f"         DN: {ferrule.dn}, FlangeOD: {ferrule.flange_od_mm}mm")
            else:
                raise AssertionError(
                    f"Ferrule no encontrado para tamaño {size}\""
                )
            
            # Buscar Gasket
            gasket = data_manager.get_preset_by_size('gasket', size)
            if gasket:
                print(f"      ✅ Gasket encontrado: {gasket.get_name()}")
                print(f"         DN: {gasket.dn}, GasketOD: {gasket.gasket_od_mm}mm")
            else:
                raise AssertionError(
                    f"Gasket no encontrado para tamaño {size}\""
                )
        
        print("✅ Búsquedas por tamaño completadas")
        
    except Exception as e:
        raise Sprint1TestError(f"Error en búsquedas por tamaño: {e}")
    
    # 6. Test búsquedas por DN
    print("\n🔍 6. Probando búsquedas por DN...")
    try:
        available_dns = data_manager.get_available_dns()
        
        for dn in available_dns[:3]:  # Probar los primeros 3 DNs
            print(f"\n   Probando DN: {dn}")
            
            # Buscar Ferrule
            ferrule = data_manager.get_preset_by_dn('ferrule', dn)
            if ferrule:
                print(f"      ✅ Ferrule encontrado: {ferrule.get_name()}")
            else:
                raise AssertionError(f"Ferrule no encontrado para DN {dn}")
            
            # Buscar Gasket
            gasket = data_manager.get_preset_by_dn('gasket', dn)
            if gasket:
                print(f"      ✅ Gasket encontrado: {gasket.get_name()}")
            else:
                raise AssertionError(f"Gasket no encontrado para DN {dn}")
        
        print("✅ Búsquedas por DN completadas")
        
    except Exception as e:
        raise Sprint1TestError(f"Error en búsquedas por DN: {e}")
    
    # 7. Test presets compatibles
    print("\n🔗 7. Probando presets compatibles...")
    try:
        test_size = available_sizes[0] if available_sizes else 3.0
        ferrule, gasket = data_manager.get_compatible_presets(test_size)
        
        if ferrule and gasket:
            print(f"   ✅ Presets compatibles encontrados para {test_size}\":")
            print(f"      Ferrule: {ferrule.get_name()}")
            print(f"      Gasket: {gasket.get_name()}")
            
            # Verificar compatibilidad
            if ferrule.is_compatible_with(gasket):
                print(f"      ✅ Compatibilidad verificada")
            else:
                raise AssertionError("Los presets no son compatibles")
        else:
            raise AssertionError(
                f"No se encontraron presets compatibles para {test_size}\""
            )
        
        print("✅ Test de compatibilidad completado")
        
    except Exception as e:
        raise Sprint1TestError(f"Error en test de compatibilidad: {e}")
    
    # 8. Test parámetros de presets
    print("\n📋 8. Probando parámetros de presets...")
    try:
        # Obtener un preset de ejemplo
        ferrule = data_manager.get_preset_by_size('ferrule', available_sizes[0])
        if ferrule:
            params = ferrule.get_parameters_dict()
            print(f"   📊 Parámetros de {ferrule.get_name()}:")
            for key, value in params.items():
                print(f"      {key}: {value}")
            assert params, "No se obtuvieron parámetros del preset"

        print("✅ Parámetros obtenidos correctamente")

    except Exception as e:
        raise Sprint1TestError(f"Error al obtener parámetros: {e}")
    
    # 9. Test recarga de datos
    print("\n🔄 9. Probando recarga de datos...")
    try:
        success = data_manager.reload_data()
        assert success, "Error en recarga de datos"
        print("✅ Recarga de datos exitosa")
        
    except Exception as e:
        raise Sprint1TestError(f"Error en recarga: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 ¡Sprint 1 completado exitosamente!")
    print("✅ Todas las funcionalidades del sistema de datos funcionan correctamente")
    print("✅ Los archivos CSV se cargan y validan correctamente")
    print("✅ Las búsquedas por tamaño y DN funcionan")
    print("✅ Los presets son compatibles entre sí")
    print("✅ El sistema está listo para el Sprint 2")


def main():
    """Función principal"""
    print("TriptaFittings - Validación Sprint 1")
    print("Core del Sistema de Datos")
    print("=" * 60)

    try:
        test_sprint1_complete()
    except (Sprint1TestError, AssertionError) as e:
        print(f"\n❌ Validación fallida. {e}")
        sys.exit(1)

    print("\n🎯 Próximos pasos:")
    print("   - Sprint 2: Generadores de Modelos")
    print("   - Sprint 3: Interfaz de Usuario")
    print("   - Sprint 4: Integración con FreeCAD")
    sys.exit(0)


if __name__ == "__main__":
    main()
