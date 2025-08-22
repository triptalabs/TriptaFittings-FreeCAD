# -*- coding: utf-8 -*-
"""
InitGui.py SIMPLE Y FUNCIONAL para TriptaFittings
==================================================
Este archivo registra el workbench TriptaFittings en FreeCAD
"""

import os
import sys

# Agregar el directorio actual al path
current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

def register_workbench():
    """Registra el workbench TriptaFittings"""
    
    try:
        import FreeCADGui as Gui
        import FreeCAD as App
        
        # Definir el workbench directamente aquí para evitar problemas de import
        class TriptaFittingsWorkbench(Gui.Workbench):
            MenuText = "TriptaFittings"
            ToolTip = "Generador de fittings sanitarios DIN 32676 A"
            Icon = os.path.join(current_dir, "resources", "icons", "triptafittings.svg")
            
            def Initialize(self):
                """Inicializa el workbench"""
                try:
                    # Comando simple para probar
                    class TriptaFittingsCommand:
                        def GetResources(self):
                            return {
                                'MenuText': 'TriptaFittings Generator',
                                'ToolTip': 'Abre el generador de fittings TriptaFittings',
                                'Pixmap': os.path.join(current_dir, "resources", "icons", "triptafittings.svg")
                            }
                        
                        def Activated(self):
                            import FreeCAD
                            FreeCAD.Console.PrintMessage("🎉 ¡TriptaFittings activado!\n")
                            FreeCAD.Console.PrintMessage("Workbench funcionando correctamente\n")
                        
                        def IsActive(self):
                            return True
                    
                    # Registrar el comando
                    Gui.addCommand('TriptaFittings_Generator', TriptaFittingsCommand())
                    
                    # Configurar toolbar y menú
                    self.list = ['TriptaFittings_Generator']
                    self.appendToolbar('TriptaFittings', self.list)
                    self.appendMenu('TriptaFittings', self.list)
                    
                    App.Console.PrintMessage("✅ TriptaFittings workbench inicializado correctamente\n")
                    
                except Exception as e:
                    App.Console.PrintError(f"Error al inicializar workbench: {e}\n")
            
            def GetClassName(self):
                return "Gui::PythonWorkbench"
        
        # Crear y registrar el workbench
        workbench = TriptaFittingsWorkbench()
        Gui.addWorkbench(workbench)
        
        App.Console.PrintMessage("🎉 TriptaFittings workbench registrado exitosamente\n")
        App.Console.PrintMessage("Ve a: View > Workbenches > TriptaFittings\n")
        
        return True
        
    except ImportError:
        # FreeCAD no disponible (modo testing)
        print("FreeCAD no disponible - modo testing")
        return False
    except Exception as e:
        print(f"Error al registrar workbench: {e}")
        return False

# Ejecutar registro automáticamente
if __name__ == "__main__":
    register_workbench()
else:
    # Cuando FreeCAD importa este módulo
    register_workbench()

