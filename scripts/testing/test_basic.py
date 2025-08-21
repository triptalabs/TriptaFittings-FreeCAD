#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba básico para TriptaFittings
"""

import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_basic_imports():
    """Prueba las importaciones básicas"""
    print("🔍 Probando importaciones básicas...")
    
    try:
        from models.data_manager import DataManager
        print("✅ DataManager importado correctamente")
        
        from data.preset import Preset
        print("✅ Preset importado correctamente")
        
        from data.csv_loader import CSVLoader
        print("✅ CSVLoader importado correctamente")
        
        return True
    except Exception as e:
        print(f"❌ Error en importaciones: {e}")
        return False

def test_data_manager():
    """Prueba la creación del DataManager"""
    print("\n🔍 Probando DataManager...")
    
    try:
        from models.data_manager import DataManager
        
        # Crear instancia
        dm = DataManager()
        print("✅ DataManager creado exitosamente")
        
        # Cargar datos
        print("📊 Cargando datos...")
        success = dm.load_all_data()
        
        if success:
            print("✅ Datos cargados exitosamente")
            
            # Obtener resumen
            summary = dm.get_data_summary()
            print(f"📈 Resumen:")
            print(f"   - Ferrule presets: {summary['ferrule_count']}")
            print(f"   - Gasket presets: {summary['gasket_count']}")
            print(f"   - Tamaños disponibles: {summary['available_sizes']}")
            
            return True
        else:
            print("❌ Error al cargar datos")
            return False
            
    except Exception as e:
        print(f"❌ Error en DataManager: {e}")
        return False

def test_preset_creation():
    """Prueba la creación de presets"""
    print("\n🔍 Probando creación de presets...")
    
    try:
        from data.preset import Preset
        
        # Datos de ejemplo para Ferrule
        ferrule_data = {
            'Size': '3"',
            'DN': 'DN80',
            'FlangeOD_mm': 106.0,
            'C2_mm': 97.0,
            'TubeID_mm': 81.2,
            'PassageDia_mm': 81.0,
            'HeightTube_mm': 24.0,
            'HeightProfile_mm': 4.3,
            'SeatLipWidth_mm': 1.0,
            'Standard': 'DIN 32676 A'
        }
        
        # Crear preset de Ferrule
        ferrule_preset = Preset('ferrule', ferrule_data)
        print("✅ Preset de Ferrule creado exitosamente")
        print(f"   - Tamaño: {ferrule_preset.size}")
        print(f"   - DN: {ferrule_preset.dn}")
        print(f"   - Flange OD: {ferrule_preset.flange_od_mm} mm")
        
        # Datos de ejemplo para Gasket
        gasket_data = {
            'Size': '3"',
            'DN': 'DN80',
            'FlangeOD_mm': 106.0,
            'GasketOD_mm': 106.0,
            'GasketID_mm': 81.2,
            'BeadC2_mm': 97.0,
            'ProfileH_mm': 4.3,
            'SeatLipWidth_mm': 1.0,
            'Standard': 'DIN 32676 A'
        }
        
        # Crear preset de Gasket
        gasket_preset = Preset('gasket', gasket_data)
        print("✅ Preset de Gasket creado exitosamente")
        print(f"   - Tamaño: {gasket_preset.size}")
        print(f"   - DN: {gasket_preset.dn}")
        print(f"   - Gasket OD: {gasket_preset.gasket_od_mm} mm")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en creación de presets: {e}")
        return False

def main():
    """Función principal de pruebas"""
    print("Iniciando pruebas basicas de TriptaFittings")
    print("=" * 50)
    
    # Ejecutar pruebas
    tests = [
        test_basic_imports,
        test_data_manager,
        test_preset_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    # Resumen
    print("=" * 50)
    print(f"📊 Resultados: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron! El sistema está funcionando correctamente.")
        return True
    else:
        print("⚠️  Algunas pruebas fallaron. Revisa los errores arriba.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
