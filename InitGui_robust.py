# -*- coding: utf-8 -*-
"""
InitGui.py para TriptaFittings
Versión robusta con múltiples estrategias de registro
"""

def register_workbench():
    """Registra el workbench TriptaFittings con múltiples estrategias"""
    
    try:
        # Importar FreeCAD
        import FreeCADGui as Gui
        import FreeCAD as App
        
        # Agregar directorio actual al path
        import sys
        import os
        current_dir = os.path.dirname(__file__)
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        # ESTRATEGIA 1: Import directo
        try:
            from src.triptafittings.workbench.init_gui import TriptaFittingsWorkbench
            workbench = TriptaFittingsWorkbench()
            Gui.addWorkbench(workbench)
            App.Console.PrintMessage("✅ TriptaFittings registrado exitosamente (estrategia 1)\n")
            return True
        except Exception as e1:
            App.Console.PrintWarning(f"Estrategia 1 falló: {e1}\n")
        
        # ESTRATEGIA 2: Import con sys.path
        try:
            src_dir = os.path.join(current_dir, 'src')
            if src_dir not in sys.path:
                sys.path.insert(0, src_dir)
            
            from triptafittings.workbench.init_gui import TriptaFittingsWorkbench
            workbench = TriptaFittingsWorkbench()
            Gui.addWorkbench(workbench)
            App.Console.PrintMessage("✅ TriptaFittings registrado exitosamente (estrategia 2)\n")
            return True
        except Exception as e2:
            App.Console.PrintWarning(f"Estrategia 2 falló: {e2}\n")
        
        # ESTRATEGIA 3: Workbench minimalista
        try:
            class TriptaFittingsWorkbench(Gui.Workbench):
                MenuText = "TriptaFittings"
                ToolTip = "Generador de fittings sanitarios"
                
                def Initialize(self):
                    # Registrar comando simple
                    import FreeCADGui
                    
                    class SimpleCommand:
                        def GetResources(self):
                            return {
                                'MenuText': 'TriptaFittings Generator',
                                'ToolTip': 'Abre el generador TriptaFittings'
                            }
                        
                        def Activated(self):
                            import FreeCAD
                            FreeCAD.Console.PrintMessage("TriptaFittings activado!\n")
                    
                    FreeCADGui.addCommand('TriptaSimple', SimpleCommand())
                    self.list = ['TriptaSimple']
                
                def GetClassName(self):
                    return "Gui::PythonWorkbench"
            
            workbench = TriptaFittingsWorkbench()
            Gui.addWorkbench(workbench)
            App.Console.PrintMessage("✅ TriptaFittings registrado exitosamente (estrategia 3 - básico)\n")
            return True
            
        except Exception as e3:
            App.Console.PrintError(f"Todas las estrategias fallaron. Último error: {e3}\n")
            return False
            
    except ImportError:
        # FreeCAD no disponible (testing mode)
        print("FreeCAD no disponible - modo testing")
        return False
    except Exception as e:
        print(f"Error general: {e}")
        return False

# Ejecutar registro
register_workbench()


