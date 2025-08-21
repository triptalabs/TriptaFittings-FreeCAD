# -*- coding: utf-8 -*-
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
