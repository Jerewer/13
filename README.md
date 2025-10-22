
# 🏢 Sistema de Registro de Empleados con Python + MySQL

Un sistema de escritorio desarrollado en **Python (Tkinter)** con conexión a **MySQL**, que permite **registrar, buscar, eliminar y visualizar empleados** de manera sencilla e interactiva.  
Ideal para proyectos CRUD, prácticas universitarias o aprendizaje de bases de datos con interfaces gráficas.

---

## 🚀 Características Principales

- ✅ **Conexión directa con MySQL**
- 🧾 **Registro automático** con ID único (UUID)
- 🔍 **Búsqueda dinámica** (nombre, correo o ID)
- 📋 **Visualización profesional** con Treeview
- 🧮 **Estadísticas detalladas** del sistema
- ⚙️ **Validaciones y manejo de errores**
- 🎨 **Interfaz moderna con Tkinter y ttk**

---

## 🗂️ Estructura del Proyecto

```

📦 Sistema_Registro_Empleados
├── sistema_empleados.py     # Código principal de la aplicación
├── README.md                # Documento descriptivo (este archivo)
└── registro_empleados.sql   # Script SQL para crear la base de datos

```

---

## 🧠 Requisitos Previos

Antes de ejecutar el programa, asegúrate de tener instalado lo siguiente:

- 🐍 **Python 3.10 o superior**
- 🗄️ **MySQL Server** (con acceso local)
- 📦 Librería necesaria:
```bash
  pip install mysql-connector-python
```

## 🧱 Configuración de la Base de Datos

Puedes crear la base de datos manualmente o ejecutar directamente el script incluido (`registro_empleados.sql`).

### 💾 Script SQL completo

```sql
CREATE DATABASE IF NOT EXISTS registro_empleados;
USE registro_empleados;

CREATE TABLE IF NOT EXISTS empleados (
    id VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    sexo VARCHAR(10) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO empleados (id, nombre, sexo, correo) VALUES
('EMP001', 'María González López', 'Femenino', 'maria.gonzalez@empresa.com'),
('EMP002', 'Carlos Rodríguez Pérez', 'Masculino', 'carlos.rodriguez@empresa.com');

-- Ver tablas creadas
SHOW TABLES;

-- Ver datos de empleados
SELECT * FROM empleados;

-- Ver estructura de la tabla
DESCRIBE empleados;
```

---

## ⚙️ Configuración del Código

Dentro del archivo `sistema_empleados.py`, asegúrate de que los datos de conexión coincidan con tu entorno MySQL:

```python
self.connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='toor',
    database='registro_empleados'
)
```

> 💡 Cambia el usuario o contraseña según tu instalación de MySQL.

---

## ▶️ Ejecución del Programa

Ejecuta el archivo desde tu terminal o IDE preferido:

```bash
python sistema_empleados.py
```

> Se abrirá una interfaz gráfica donde podrás registrar y gestionar empleados fácilmente.

---

## 🖥️ Interfaz de Usuario

**Componentes principales:**

* 🧍 Formulario para registro de empleados
* 🔍 Campo de búsqueda dinámica
* 📄 Lista interactiva de empleados (Treeview)
* ⚙️ Panel de control con botones:

  * ➕ Agregar Empleado
  * 🗑️ Eliminar Empleado
  * 🔄 Actualizar Lista
  * 🧹 Limpiar Campos
  * 📊 Ver Estadísticas
  * ❌ Salir

---

## 📊 Estadísticas del Sistema

Al presionar **📊 Estadísticas**, el sistema muestra:

```
📊 ESTADÍSTICAS DEL SISTEMA

• Total de empleados registrados: 8
• Primer registro: 22/10/2025

• Distribución por sexo:
   - Masculino: 5 (62.5%)
   - Femenino: 3 (37.5%)
```

---

## 🧩 Funciones Destacadas

| Función                        | Descripción                        |
| ------------------------------ | ---------------------------------- |
| `conectar_bd()`                | Establece la conexión con MySQL    |
| `agregar_empleado()`           | Inserta un nuevo registro en la BD |
| `eliminar_empleado()`          | Borra el empleado seleccionado     |
| `buscar_empleados()`           | Filtra resultados en tiempo real   |
| `actualizar_lista_empleados()` | Refresca la vista del Treeview     |
| `mostrar_estadisticas()`       | Calcula totales y porcentajes      |
| `generar_id_unico()`           | Crea un ID único con UUID          |

---

## 🧠 Conceptos Aplicados

* CRUD completo (Create, Read, Update, Delete)
* Uso de **MySQL Connector** con parámetros seguros
* Diseño modular con **Tkinter y ttk**
* Manejo de excepciones
* Buenas prácticas en interfaz y lógica de negocio

