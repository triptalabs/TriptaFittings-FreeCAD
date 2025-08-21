# -*- coding: utf-8 -*-
"""Diálogo principal de TriptaFittings para FreeCAD.

Este módulo implementa la interfaz gráfica completa para el issue #10,
incluyendo diálogo principal, dropdowns dinámicos, tabla de parámetros
y validación visual.
"""
from __future__ import annotations

import sys
from typing import Dict, Any, List, Optional
from pathlib import Path

try:
    from PySide2 import QtWidgets, QtCore, QtGui
    from PySide2.QtCore import Signal
    PYSIDE2_AVAILABLE = True
except ImportError:
    try:
        # Intentar PyQt5 como fallback
        from PyQt5 import QtWidgets, QtCore, QtGui
        from PyQt5.QtCore import pyqtSignal as Signal
        PYSIDE2_AVAILABLE = True
    except ImportError:
        # Fallback para entornos sin Qt
        PYSIDE2_AVAILABLE = False
        
        class QtWidgets:
            class QDialog:
                def __init__(self, parent=None):
                    self.parent = parent
                def exec_(self):
                    return True
                def setWindowTitle(self, title):
                    pass
                def setModal(self, modal):
                    pass
                def resize(self, w, h):
                    pass
                def reject(self):
                    pass
            
            class QVBoxLayout:
                def __init__(self, parent=None):
                    pass
                def addWidget(self, widget):
                    pass
            
            class QHBoxLayout:
                def __init__(self, parent=None):
                    pass
                def addWidget(self, widget):
                    pass
                def addStretch(self):
                    pass
            
            class QGridLayout:
                def __init__(self, parent=None):
                    pass
                def addWidget(self, widget, row, col):
                    pass
            
            class QComboBox:
                def __init__(self):
                    self._items = []
                    self._current = 0
                def addItems(self, items):
                    self._items.extend(items)
                def addItem(self, text, data=None):
                    self._items.append((text, data))
                def currentText(self):
                    return self._items[self._current][0] if self._items else ""
                def currentData(self):
                    return self._items[self._current][1] if self._items else None
                def setCurrentIndex(self, index):
                    self._current = index
                def findText(self, text):
                    for i, (t, d) in enumerate(self._items):
                        if t == text:
                            return i
                    return -1
                def count(self):
                    return len(self._items)
                def clear(self):
                    self._items = []
                def setToolTip(self, tooltip):
                    pass
                @property
                def currentTextChanged(self):
                    return MockSignal()
            
            class QPushButton:
                def __init__(self, text=""):
                    self.text = text
                    self._enabled = True
                def setStyleSheet(self, style):
                    pass
                def setEnabled(self, enabled):
                    self._enabled = enabled
                def isEnabled(self):
                    return self._enabled
                @property
                def clicked(self):
                    return MockSignal()
            
            class QTableWidget:
                def __init__(self):
                    self._rows = 0
                    self._cols = 0
                def setColumnCount(self, count):
                    self._cols = count
                def setRowCount(self, count):
                    self._rows = count
                def rowCount(self):
                    return self._rows
                def setHorizontalHeaderLabels(self, labels):
                    pass
                def horizontalHeader(self):
                    return MockHeader()
                def setAlternatingRowColors(self, alt):
                    pass
                def setSelectionBehavior(self, behavior):
                    pass
                def setMaximumHeight(self, height):
                    pass
                def setItem(self, row, col, item):
                    pass
            
            class QTableWidgetItem:
                def __init__(self, text=""):
                    self.text = text
                    self._flags = 0xFF
                def flags(self):
                    return self._flags
                def setFlags(self, flags):
                    self._flags = flags
            
            class QLabel:
                def __init__(self, text=""):
                    self.text = text
                def setFont(self, font):
                    pass
                def setAlignment(self, align):
                    pass
                def setStyleSheet(self, style):
                    pass
                def setText(self, text):
                    self.text = text
            
            class QTextEdit:
                def __init__(self):
                    self.text = ""
                def setMaximumHeight(self, height):
                    pass
                def setReadOnly(self, readonly):
                    pass
                def setPlainText(self, text):
                    self.text = text
                def append(self, text):
                    self.text += "\n" + text
                def textCursor(self):
                    return MockCursor()
                def setTextCursor(self, cursor):
                    pass
            
            class QProgressBar:
                def __init__(self):
                    pass
                def setVisible(self, visible):
                    pass
                def setRange(self, min_val, max_val):
                    pass
                def setValue(self, value):
                    pass
            
            class QGroupBox:
                def __init__(self, title=""):
                    self.title = title
            
            class QMessageBox:
                @staticmethod
                def critical(parent, title, message):
                    print(f"ERROR: {message}")
                @staticmethod
                def warning(parent, title, message):
                    print(f"WARNING: {message}")
                @staticmethod
                def information(parent, title, message):
                    print(f"INFO: {message}")
            
            class QWidget:
                def __init__(self):
                    pass
            
            class QHeaderView:
                Stretch = 1
                ResizeToContents = 2
                def setStretchLastSection(self, stretch):
                    pass
                def setSectionResizeMode(self, section, mode):
                    pass
            
            class QAbstractItemView:
                SelectRows = 1
        
        class QtCore:
            class Qt:
                AlignCenter = 1
                ItemIsEditable = 1
            
            class QDateTime:
                @staticmethod
                def currentDateTime():
                    return MockDateTime()
        
        class QtGui:
            class QFont:
                def __init__(self):
                    pass
                def setBold(self, bold):
                    pass
                def setPointSize(self, size):
                    pass
            
            class QTextCursor:
                End = 1
                def movePosition(self, pos):
                    pass

        class MockSignal:
            def __init__(self, *args):
                pass
            def connect(self, func):
                pass
            def emit(self, *args):
                pass

        class MockHeader:
            def setStretchLastSection(self, stretch):
                pass
            def setSectionResizeMode(self, section, mode):
                pass

        class MockCursor:
            def movePosition(self, pos):
                pass

        class MockDateTime:
            def toString(self, format_str):
                return "12:00:00"

        Signal = MockSignal

from ..core.data_manager import DataManager
from ..generators.ferrule import FerruleGenerator
from ..generators.gasket import GasketGenerator


class TriptaFittingsDialog(QtWidgets.QDialog):
    """Diálogo principal para generar modelos de Ferrule y Gasket.
    
    Implementa la interfaz gráfica completa según las especificaciones
    del issue #10 (XL-002).
    """
    
    # Señales para comunicación con FreeCAD
    model_generated = Signal(dict)
    error_occurred = Signal(str)
    
    def __init__(self, parent=None, data_directory: Optional[str] = None):
        """Inicializa el diálogo principal.
        
        Args:
            parent: Widget padre (usualmente FreeCAD main window)
            data_directory: Directorio personalizado para datos CSV
        """
        super().__init__(parent)
        
        # Inicializar gestor de datos
        self.data_manager = DataManager(data_directory)
        self.current_preset = None
        self.generated_models = []
        
        # Configurar ventana
        self.setWindowTitle("TriptaFittings Generator")
        self.setModal(True)
        self.resize(600, 500)
        
        # Cargar datos y configurar interfaz
        self._load_data()
        self._setup_ui()
        self._connect_signals()
        self._update_size_dropdown()
    
    def _load_data(self):
        """Carga los datos de presets desde CSV."""
        try:
            success = self.data_manager.load_all_data()
            if not success:
                self._show_error("Error al cargar datos de presets")
        except Exception as e:
            self._show_error(f"Error crítico al cargar datos: {str(e)}")
    
    def _setup_ui(self):
        """Configura la interfaz de usuario completa."""
        # Layout principal
        main_layout = QtWidgets.QVBoxLayout(self)
        
        # Título del diálogo
        title_label = QtWidgets.QLabel("TriptaFittings - Generador de Modelos")
        title_font = QtGui.QFont()
        title_font.setBold(True)
        title_font.setPointSize(14)
        title_label.setFont(title_font)
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Grupo de selección
        selection_group = self._create_selection_group()
        main_layout.addWidget(selection_group)
        
        # Grupo de parámetros
        params_group = self._create_parameters_group()
        main_layout.addWidget(params_group)
        
        # Grupo de acciones
        actions_group = self._create_actions_group()
        main_layout.addWidget(actions_group)
        
        # Área de estado
        status_group = self._create_status_group()
        main_layout.addWidget(status_group)
        
        # Botones de diálogo
        dialog_buttons = self._create_dialog_buttons()
        main_layout.addWidget(dialog_buttons)
    
    def _create_selection_group(self) -> QtWidgets.QGroupBox:
        """Crea el grupo de selección de componente y tamaño."""
        group = QtWidgets.QGroupBox("Selección de Componente")
        layout = QtWidgets.QGridLayout(group)
        
        # Selector de componente
        layout.addWidget(QtWidgets.QLabel("Tipo de Componente:"), 0, 0)
        self.component_combo = QtWidgets.QComboBox()
        self.component_combo.addItems(["Ferrule", "Gasket"])
        self.component_combo.setToolTip("Selecciona el tipo de componente a generar")
        layout.addWidget(self.component_combo, 0, 1)
        
        # Selector de tamaño
        layout.addWidget(QtWidgets.QLabel("Tamaño:"), 1, 0)
        self.size_combo = QtWidgets.QComboBox()
        self.size_combo.setToolTip("Selecciona el tamaño del componente")
        layout.addWidget(self.size_combo, 1, 1)
        
        # DN correspondiente (solo lectura)
        layout.addWidget(QtWidgets.QLabel("DN Equivalente:"), 2, 0)
        self.dn_label = QtWidgets.QLabel("--")
        self.dn_label.setStyleSheet("font-weight: bold; color: #2e7d32;")
        layout.addWidget(self.dn_label, 2, 1)
        
        return group
    
    def _create_parameters_group(self) -> QtWidgets.QGroupBox:
        """Crea el grupo de visualización/edición de parámetros."""
        group = QtWidgets.QGroupBox("Parámetros del Modelo")
        layout = QtWidgets.QVBoxLayout(group)
        
        # Tabla de parámetros
        self.params_table = QtWidgets.QTableWidget()
        self.params_table.setColumnCount(3)
        self.params_table.setHorizontalHeaderLabels(["Parámetro", "Valor", "Unidad"])
        
        # Configurar tabla
        header = self.params_table.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        
        self.params_table.setAlternatingRowColors(True)
        self.params_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.params_table.setMaximumHeight(200)
        
        layout.addWidget(self.params_table)
        
        return group
    
    def _create_actions_group(self) -> QtWidgets.QGroupBox:
        """Crea el grupo de acciones principales."""
        group = QtWidgets.QGroupBox("Acciones")
        layout = QtWidgets.QHBoxLayout(group)
        
        # Botón principal de generación
        self.generate_btn = QtWidgets.QPushButton("Generate Model")
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #4caf50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        self.generate_btn.setEnabled(False)
        
        # Botón de preview
        self.preview_btn = QtWidgets.QPushButton("Preview Parameters")
        self.preview_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196f3;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #1976d2;
            }
            QPushButton:pressed {
                background-color: #0d47a1;
            }
        """)
        
        # Botón de validación
        self.validate_btn = QtWidgets.QPushButton("Validate")
        self.validate_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff9800;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #f57c00;
            }
            QPushButton:pressed {
                background-color: #e65100;
            }
        """)
        
        layout.addWidget(self.preview_btn)
        layout.addWidget(self.validate_btn)
        layout.addStretch()
        layout.addWidget(self.generate_btn)
        
        return group
    
    def _create_status_group(self) -> QtWidgets.QGroupBox:
        """Crea el grupo de estado y feedback."""
        group = QtWidgets.QGroupBox("Estado")
        layout = QtWidgets.QVBoxLayout(group)
        
        # Barra de progreso
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Área de mensajes
        self.status_text = QtWidgets.QTextEdit()
        self.status_text.setMaximumHeight(80)
        self.status_text.setReadOnly(True)
        self.status_text.setPlainText("Listo. Selecciona un componente y tamaño para comenzar.")
        layout.addWidget(self.status_text)
        
        return group
    
    def _create_dialog_buttons(self) -> QtWidgets.QWidget:
        """Crea los botones estándar del diálogo."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout(widget)
        
        # Botón de ayuda
        help_btn = QtWidgets.QPushButton("Help")
        help_btn.clicked.connect(self._show_help)
        
        # Botón cerrar
        close_btn = QtWidgets.QPushButton("Close")
        close_btn.clicked.connect(self.reject)
        
        layout.addWidget(help_btn)
        layout.addStretch()
        layout.addWidget(close_btn)
        
        return widget
    
    def _connect_signals(self):
        """Conecta las señales de los componentes."""
        self.component_combo.currentTextChanged.connect(self._on_component_changed)
        self.size_combo.currentTextChanged.connect(self._on_size_changed)
        self.generate_btn.clicked.connect(self._generate_model)
        self.preview_btn.clicked.connect(self._preview_parameters)
        self.validate_btn.clicked.connect(self._validate_selection)
    
    def _update_size_dropdown(self):
        """Actualiza el dropdown de tamaños según el componente seleccionado."""
        component = self.component_combo.currentText().lower()
        sizes = self.data_manager.get_available_sizes(component)
        
        # Limpiar y llenar dropdown
        self.size_combo.clear()
        for size in sizes:
            display_text = f'{size}"'
            self.size_combo.addItem(display_text, size)
        
        self._log_status(f"Tamaños disponibles para {component}: {len(sizes)}")
    
    def _on_component_changed(self):
        """Maneja el cambio de tipo de componente."""
        self._update_size_dropdown()
        self._clear_parameters()
        self.generate_btn.setEnabled(False)
        self._log_status(f"Componente cambiado a: {self.component_combo.currentText()}")
    
    def _on_size_changed(self):
        """Maneja el cambio de tamaño."""
        if self.size_combo.currentData() is not None:
            self._load_preset()
            self._update_parameters_table()
            self._validate_selection()
    
    def _load_preset(self):
        """Carga el preset correspondiente a la selección actual."""
        component = self.component_combo.currentText().lower()
        size = self.size_combo.currentData()
        
        if size is not None:
            self.current_preset = self.data_manager.get_preset_by_size(component, size)
            if self.current_preset:
                self.dn_label.setText(self.current_preset.dn)
                self._log_status(f"Preset cargado: {component} {size}\" ({self.current_preset.dn})")
            else:
                self.dn_label.setText("--")
                self._log_status(f"⚠️ No se encontró preset para {component} {size}\"", "warning")
    
    def _update_parameters_table(self):
        """Actualiza la tabla de parámetros con el preset actual."""
        if not self.current_preset:
            self._clear_parameters()
            return
        
        params = self.current_preset.get_parameters_dict()
        self.params_table.setRowCount(len(params))
        
        for row, (param, value) in enumerate(params.items()):
            # Nombre del parámetro
            param_item = QtWidgets.QTableWidgetItem(param)
            param_item.setFlags(param_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.params_table.setItem(row, 0, param_item)
            
            # Valor (editable)
            value_item = QtWidgets.QTableWidgetItem(str(value))
            self.params_table.setItem(row, 1, value_item)
            
            # Unidad
            unit = "mm" if "mm" in param or "dia" in param.lower() else ""
            unit_item = QtWidgets.QTableWidgetItem(unit)
            unit_item.setFlags(unit_item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.params_table.setItem(row, 2, unit_item)
    
    def _clear_parameters(self):
        """Limpia la tabla de parámetros."""
        self.params_table.setRowCount(0)
        self.dn_label.setText("--")
    
    def _preview_parameters(self):
        """Muestra un preview de los parámetros actuales."""
        if not self.current_preset:
            self._show_warning("Selecciona un componente y tamaño primero")
            return
        
        component = self.component_combo.currentText()
        size = self.size_combo.currentData()
        
        preview_text = f"""
Componente: {component}
Tamaño: {size}"
DN: {self.current_preset.dn}

Parámetros principales:
"""
        params = self.current_preset.get_parameters_dict()
        for param, value in list(params.items())[:5]:  # Mostrar solo los primeros 5
            preview_text += f"  • {param}: {value}\n"
        
        if len(params) > 5:
            preview_text += f"  ... y {len(params) - 5} parámetros más"
        
        self._log_status(preview_text.strip())
    
    def _validate_selection(self):
        """Valida la selección actual."""
        if not self.current_preset:
            self.generate_btn.setEnabled(False)
            self._log_status("❌ Selección inválida", "error")
            return
        
        # Validaciones básicas
        errors = []
        
        # Verificar que el preset tenga datos válidos
        params = self.current_preset.get_parameters_dict()
        if not params:
            errors.append("El preset no tiene parámetros válidos")
        
        # Verificar valores numéricos
        for param, value in params.items():
            try:
                float(value)
            except (ValueError, TypeError):
                if param not in ['component_type', 'size_display', 'dn']:
                    errors.append(f"Valor inválido en {param}: {value}")
        
        if errors:
            self.generate_btn.setEnabled(False)
            self._log_status(f"❌ Errores de validación:\n" + "\n".join(errors), "error")
        else:
            self.generate_btn.setEnabled(True)
            self._log_status("✅ Selección válida. Listo para generar.", "success")
    
    def _generate_model(self):
        """Genera el modelo 3D."""
        if not self.current_preset:
            self._show_error("No hay preset seleccionado")
            return
        
        try:
            self._set_progress(True)
            component = self.component_combo.currentText().lower()
            
            # Generar usando el generador correspondiente
            if component == "ferrule":
                generator = FerruleGenerator(self.current_preset)
            else:
                generator = GasketGenerator(self.current_preset)
            
            # Generar geometría
            model = generator.generate_geometry()
            
            # Registrar modelo generado
            self.generated_models.append(model)
            
            # Emitir señal para FreeCAD
            self.model_generated.emit(model)
            
            self._log_status(f"✅ Modelo generado exitosamente: {model['name']}", "success")
            
        except Exception as e:
            error_msg = f"Error al generar modelo: {str(e)}"
            self._log_status(f"❌ {error_msg}", "error")
            self.error_occurred.emit(error_msg)
        finally:
            self._set_progress(False)
    
    def _set_progress(self, active: bool):
        """Controla la visualización del progreso."""
        self.progress_bar.setVisible(active)
        if active:
            self.progress_bar.setRange(0, 0)  # Progreso indefinido
        else:
            self.progress_bar.setRange(0, 1)
            self.progress_bar.setValue(1)
    
    def _log_status(self, message: str, level: str = "info"):
        """Registra un mensaje en el área de estado."""
        timestamp = QtCore.QDateTime.currentDateTime().toString("hh:mm:ss")
        
        if level == "error":
            styled_message = f"[{timestamp}] ❌ {message}"
        elif level == "warning":
            styled_message = f"[{timestamp}] ⚠️ {message}"
        elif level == "success":
            styled_message = f"[{timestamp}] ✅ {message}"
        else:
            styled_message = f"[{timestamp}] {message}"
        
        self.status_text.append(styled_message)
        # Auto-scroll al final
        cursor = self.status_text.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        self.status_text.setTextCursor(cursor)
    
    def _show_error(self, message: str):
        """Muestra un diálogo de error."""
        QtWidgets.QMessageBox.critical(self, "Error", message)
    
    def _show_warning(self, message: str):
        """Muestra un diálogo de advertencia."""
        QtWidgets.QMessageBox.warning(self, "Advertencia", message)
    
    def _show_help(self):
        """Muestra la ayuda del diálogo."""
        help_text = """
<h3>TriptaFittings Generator - Ayuda</h3>

<p><b>Paso 1:</b> Selecciona el tipo de componente (Ferrule o Gasket)</p>
<p><b>Paso 2:</b> Elige el tamaño deseado de la lista</p>
<p><b>Paso 3:</b> Revisa los parámetros en la tabla</p>
<p><b>Paso 4:</b> Haz clic en "Generate Model"</p>

<h4>Funciones adicionales:</h4>
<ul>
<li><b>Preview Parameters:</b> Muestra un resumen de los parámetros</li>
<li><b>Validate:</b> Verifica que la selección sea válida</li>
<li><b>Tabla de Parámetros:</b> Puedes editar valores antes de generar</li>
</ul>

<h4>Estándares soportados:</h4>
<p>DIN 32676 A - Tamaños de 1.5" a 12"</p>
        """
        
        QtWidgets.QMessageBox.information(self, "Ayuda", help_text)
    
    def get_generated_models(self) -> List[Dict[str, Any]]:
        """Retorna la lista de modelos generados en esta sesión."""
        return self.generated_models.copy()
    
    def clear_generated_models(self):
        """Limpia la lista de modelos generados."""
        self.generated_models.clear()
        self._log_status("Lista de modelos generados limpiada")


def show_triptafittings_dialog(parent=None) -> TriptaFittingsDialog:
    """Función de conveniencia para mostrar el diálogo.
    
    Args:
        parent: Widget padre (usualmente FreeCAD main window)
    
    Returns:
        Instancia del diálogo creado
    """
    dialog = TriptaFittingsDialog(parent)
    return dialog


# Función para testing sin FreeCAD
def main():
    """Función principal para testing standalone."""
    app = QtWidgets.QApplication(sys.argv)
    
    dialog = TriptaFittingsDialog()
    dialog.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
