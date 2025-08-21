# -*- coding: utf-8 -*-
"""Punto de entrada para FreeCAD - InitGui.py

Este archivo es requerido por FreeCAD para registrar el workbench.
"""

# Import del workbench desde la nueva estructura
try:
    from src.triptafittings.workbench.init_gui import TriptaFittingsWorkbench
    
    # Registrar el workbench con FreeCAD
    try:
        import FreeCADGui as Gui
        
        # Crear instancia del workbench
        workbench = TriptaFittingsWorkbench()
        
        # Registrar con FreeCAD
        Gui.addWorkbench(workbench)
        print("✅ TriptaFittings workbench registrado exitosamente")
        
    except ImportError:
        # FreeCAD no está disponible (modo testing)
        print("⚠️ FreeCAD no disponible - workbench no registrado")
    except Exception as e:
        print(f"❌ Error al registrar workbench TriptaFittings: {e}")
        import traceback
        traceback.print_exc()

except ImportError as e:
    print(f"❌ Error al importar TriptaFittings workbench: {e}")
    import traceback
    traceback.print_exc()
