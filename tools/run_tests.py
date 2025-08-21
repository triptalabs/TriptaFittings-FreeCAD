#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script unificado para ejecutar todas las pruebas del proyecto TriptaFittings.

Este script ejecuta todos los tests unitarios y de integración,
proporcionando un resumen completo del estado del proyecto.
"""

import os
import sys
import unittest
import time
from pathlib import Path

# Añadir src al path para imports
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

def discover_tests(test_dir: str, pattern: str = "test_*.py") -> unittest.TestSuite:
    """Descubre tests en un directorio específico."""
    loader = unittest.TestLoader()
    start_dir = PROJECT_ROOT / "tests" / test_dir
    return loader.discover(str(start_dir), pattern=pattern)

def run_test_suite(suite: unittest.TestSuite, suite_name: str) -> tuple:
    """Ejecuta una suite de tests y retorna resultados."""
    print(f"\n{'='*60}")
    print(f"🧪 Ejecutando {suite_name}")
    print(f"{'='*60}")
    
    runner = unittest.TextTestRunner(verbosity=2)
    start_time = time.time()
    result = runner.run(suite)
    duration = time.time() - start_time
    
    print(f"\n⏱️  Tiempo: {duration:.2f}s")
    return result, duration

def print_summary(results: list):
    """Imprime resumen final de todos los tests."""
    print(f"\n{'='*60}")
    print("📊 RESUMEN FINAL")
    print(f"{'='*60}")
    
    total_tests = 0
    total_failures = 0
    total_errors = 0
    total_time = 0
    
    for name, result, duration in results:
        total_tests += result.testsRun
        total_failures += len(result.failures)
        total_errors += len(result.errors)
        total_time += duration
        
        status = "✅ PASS" if (len(result.failures) + len(result.errors)) == 0 else "❌ FAIL"
        print(f"{status} {name}: {result.testsRun} tests, {len(result.failures)} failures, {len(result.errors)} errors ({duration:.2f}s)")
    
    print(f"\n📈 TOTAL: {total_tests} tests, {total_failures} failures, {total_errors} errors")
    print(f"⏱️  Tiempo total: {total_time:.2f}s")
    
    if total_failures + total_errors == 0:
        print("🎉 ¡Todos los tests pasaron!")
        return True
    else:
        print("⚠️  Algunos tests fallaron")
        return False

def main():
    """Función principal."""
    print("🚀 TriptaFittings - Test Runner")
    print(f"📁 Directorio del proyecto: {PROJECT_ROOT}")
    
    results = []
    
    # Tests unitarios
    unit_suite = discover_tests("unit")
    unit_result, unit_duration = run_test_suite(unit_suite, "Tests Unitarios")
    results.append(("Tests Unitarios", unit_result, unit_duration))
    
    # Tests de integración
    integration_suite = discover_tests("integration") 
    integration_result, integration_duration = run_test_suite(integration_suite, "Tests de Integración")
    results.append(("Tests de Integración", integration_result, integration_duration))
    
    # Resumen final
    success = print_summary(results)
    
    # Exit code para CI/CD
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()