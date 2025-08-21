# 📖 Guías de Uso - TriptaFittings-FreeCAD

Esta carpeta contendrá todas las guías de uso del sistema TriptaFittings-FreeCAD.

## 📂 Estructura Planificada

```
usage/
├── README.md                    # Este archivo (índice)
├── getting_started.md          # Guía de inicio rápido
├── basic_usage.md              # Uso básico del sistema
├── model_generation.md         # Generación de modelos 3D
├── advanced_features.md        # Características avanzadas
├── troubleshooting.md          # Solución de problemas
└── examples/                   # Ejemplos prácticos
    ├── ferrule_examples.md     # Ejemplos de Ferrule
    ├── gasket_examples.md      # Ejemplos de Gasket
    └── integration_examples.md # Ejemplos de integración
```

## 🚀 Estado Actual

### ✅ Disponible
- **Sistema básico**: Funcionando y probado
- **Scripts de demo**: `scripts/demos/` carpeta
- **Pruebas**: `scripts/testing/` carpeta

### 🚧 En Desarrollo
- **Interfaz gráfica**: En desarrollo
- **Generación de modelos**: Próximamente
- **Guías detalladas**: En preparación

### 📋 Planificado
- **Guías de uso**: Documentación completa
- **Ejemplos prácticos**: Casos de uso reales
- **Tutoriales**: Videos y guías paso a paso

## 🎯 Funcionalidades Actuales

### Sistema de Datos
- ✅ Carga de presets desde archivos CSV
- ✅ Validación automática de datos
- ✅ Verificación de compatibilidad
- ✅ Búsqueda por tamaño y DN

### Componentes Soportados
- ✅ **Ferrule (Férula)**: 9 tamaños (1.5" a 12")
- ✅ **Gasket (Junta)**: 9 tamaños (1.5" a 12")
- ✅ **Estándar**: DIN 32676 A

### Scripts de Demostración
- ✅ **Demo automático**: `scripts/demos/demo_automatic.py`
- ✅ **Demo interactivo**: `scripts/demos/demo_interactive.py`
- ✅ **Pruebas básicas**: `scripts/testing/test_basic.py`

## 🔧 Uso Actual

### Ejecutar Demos
```bash
# Demo automático (recomendado para empezar)
python scripts/demos/demo_automatic.py

# Demo interactivo (exploración manual)
python scripts/demos/demo_interactive.py
```

### Verificar Sistema
```bash
# Ejecutar todas las pruebas
python scripts/run_all_tests.py

# Pruebas individuales
python scripts/testing/test_basic.py
python scripts/testing/check_freecad.py
```

### Explorar Datos
```python
from models.data_manager import DataManager

# Crear instancia del gestor de datos
dm = DataManager()

# Cargar todos los datos
dm.load_all_data()

# Obtener tamaños disponibles
sizes = dm.get_available_sizes()
print(f"Tamaños disponibles: {sizes}")

# Obtener presets de Ferrule
ferrule_presets = dm.get_presets_by_type('ferrule')
print(f"Presets de Ferrule: {len(ferrule_presets)}")

# Obtener presets de Gasket
gasket_presets = dm.get_presets_by_type('gasket')
print(f"Presets de Gasket: {len(gasket_presets)}")
```

## 📊 Datos Disponibles

### Tamaños Soportados
| Tamaño | DN | Descripción |
|--------|----|-------------|
| 1.5" | DN40 | Pequeño |
| 2" | DN50 | Pequeño |
| 2.5" | DN65 | Mediano |
| 3" | DN80 | Mediano |
| 4" | DN100 | Mediano |
| 6" | DN150 | Grande |
| 8" | DN200 | Grande |
| 10" | DN250 | Extra grande |
| 12" | DN300 | Extra grande |

### Estándares Implementados
- **DIN 32676 A**: Estándar alemán para conexiones sanitarias
- **Compatibilidad**: Ferrule y Gasket 100% compatibles
- **Validación**: Verificación automática de datos

## 🔮 Próximas Funcionalidades

### Interfaz Gráfica
- [ ] Panel de control en FreeCAD
- [ ] Selector de tamaños visual
- [ ] Vista previa de modelos
- [ ] Configuración de parámetros

### Generación de Modelos
- [ ] Creación automática de Ferrule 3D
- [ ] Creación automática de Gasket 3D
- [ ] Exportación a formatos estándar
- [ ] Parametrización completa

### Características Avanzadas
- [ ] Documentación para múltiples estándares
- [ ] Integración con bases de datos
- [ ] API para desarrolladores
- [ ] Plugins adicionales

## 🛠️ Desarrollo

### Para Contribuir
1. **Fork** el repositorio
2. **Crear** rama para nueva funcionalidad
3. **Desarrollar** siguiendo las guías
4. **Probar** con los scripts disponibles
5. **Pull Request** con documentación

### Estándares de Código
- **Python**: PEP 8
- **Documentación**: Docstrings completos
- **Pruebas**: Cobertura mínima 80%
- **Commits**: Mensajes descriptivos

## 📖 Documentación

### Recursos Disponibles
- **Documentación**: `docs/` carpeta
- **Scripts de prueba**: `scripts/testing/` carpeta
- **Demos**: `scripts/demos/` carpeta
- **Issues**: Repositorio de GitHub

### Comunidad
- **Discusiones**: Sección de GitHub
- **Contribuciones**: Pull requests bienvenidos
- **Reportes**: Issues para bugs y mejoras

---

**¡Las guías de uso estarán disponibles próximamente! 🚀**

*Mientras tanto, usa los scripts de demo para explorar las funcionalidades actuales.*
