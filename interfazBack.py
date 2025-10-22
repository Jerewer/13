import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
import uuid

class SistemaEmpleados:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Registro de Empleados - MySQL")
        self.root.geometry("950x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variables de control
        self.nombre_var = tk.StringVar()
        self.sexo_var = tk.StringVar()
        self.correo_var = tk.StringVar()
        self.buscar_var = tk.StringVar()
        
        # Conectar a la base de datos
        self.connection = None
        self.conectar_bd()
        
        # Crear interfaz
        self.crear_interfaz()
        self.actualizar_lista_empleados()
    
    def conectar_bd(self):
        """Establece conexión con la base de datos MySQL"""
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',      # Usuario root
                password='toor',  # Contraseña toor
                database='registro_empleados'  # Base de datos que creamos
            )
            print("✅ Conexión a MySQL establecida correctamente")
            print("📊 Base de datos: registro_empleados")
            
        except Error as e:
            print(f"❌ Error al conectar a MySQL: {e}")
            messagebox.showerror("Error de Base de Datos", 
                               f"No se pudo conectar a la base de datos:\n{e}\n\n"
                               "Asegúrate de que:\n"
                               "1. MySQL esté ejecutándose\n"
                               "2. La base de datos 'registro_empleados' exista\n"
                               "3. Las credenciales sean usuario: root, contraseña: toor")
    
    def generar_id_unico(self):
        """Genera un ID único para el empleado usando UUID"""
        return str(uuid.uuid4())[:8].upper()
    
    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz gráfica"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid weights para responsividad
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título de la aplicación
        titulo = ttk.Label(main_frame, 
                          text="🏢 Sistema de Registro de Empleados - MySQL", 
                          font=('Arial', 16, 'bold'),
                          foreground='darkblue')
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 15))
        
        # Estado de conexión
        estado_texto = "✅ Conectado a MySQL - Base: registro_empleados" if self.connection else "❌ Sin conexión a la base de datos"
        estado_label = ttk.Label(main_frame, text=estado_texto, 
                                font=('Arial', 10),
                                foreground='green' if self.connection else 'red')
        estado_label.grid(row=1, column=0, columnspan=3, pady=(0, 15))
        
        # Sección de búsqueda
        self.crear_seccion_busqueda(main_frame, 2)
        
        # Sección de formulario
        self.crear_seccion_formulario(main_frame, 3)
        
        # Sección de lista de empleados
        self.crear_seccion_lista(main_frame, 4)
        
        # Sección de botones de control
        self.crear_seccion_controles(main_frame, 5)
    
    def crear_seccion_busqueda(self, parent, row):
        """Crea la sección de búsqueda de empleados"""
        search_frame = ttk.LabelFrame(parent, text="🔍 Búsqueda de Empleados", padding="10")
        search_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        search_frame.columnconfigure(1, weight=1)
        
        ttk.Label(search_frame, text="Buscar:", font=('Arial', 10, 'bold')).grid(
            row=0, column=0, padx=(0, 10))
        
        search_entry = ttk.Entry(search_frame, textvariable=self.buscar_var, 
                                width=50, font=('Arial', 10))
        search_entry.grid(row=0, column=1, padx=(0, 15), sticky=(tk.W, tk.E))
        search_entry.bind('<KeyRelease>', self.buscar_empleados)
        
        ttk.Button(search_frame, text="Limpiar Búsqueda", 
                  command=self.limpiar_busqueda).grid(row=0, column=2)
        
        # Información de búsqueda
        ttk.Label(search_frame, text="Puedes buscar por nombre, correo o ID", 
                 font=('Arial', 8), foreground='gray').grid(
                 row=1, column=0, columnspan=3, sticky=tk.W, pady=(5, 0))
    
    def crear_seccion_formulario(self, parent, row):
        """Crea la sección del formulario para agregar/editar empleados"""
        form_frame = ttk.LabelFrame(parent, text="📝 Datos del Empleado", padding="15")
        form_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        form_frame.columnconfigure(1, weight=1)
        
        # Campo Nombre
        ttk.Label(form_frame, text="Nombre completo:*", font=('Arial', 10, 'bold')).grid(
            row=0, column=0, sticky=tk.W, pady=8)
        nombre_entry = ttk.Entry(form_frame, textvariable=self.nombre_var, 
                                width=40, font=('Arial', 10))
        nombre_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=8, padx=(10, 0))
        nombre_entry.focus()
        
        # Campo Sexo
        ttk.Label(form_frame, text="Sexo:*", font=('Arial', 10, 'bold')).grid(
            row=1, column=0, sticky=tk.W, pady=8)
        sexo_combo = ttk.Combobox(form_frame, textvariable=self.sexo_var, 
                                 values=["Masculino", "Femenino", "Otro"], 
                                 state="readonly", font=('Arial', 10))
        sexo_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=8, padx=(10, 0))
        sexo_combo.set("Masculino")  # Valor por defecto
        
        # Campo Correo
        ttk.Label(form_frame, text="Correo electrónico:*", font=('Arial', 10, 'bold')).grid(
            row=2, column=0, sticky=tk.W, pady=8)
        correo_entry = ttk.Entry(form_frame, textvariable=self.correo_var, 
                                width=40, font=('Arial', 10))
        correo_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=8, padx=(10, 0))
        
        # Información de ID automático
        info_label = ttk.Label(form_frame, 
                              text="💡 El ID se generará automáticamente | * Campos obligatorios", 
                              font=('Arial', 9), foreground='blue')
        info_label.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=(10, 0))
    
    def crear_seccion_lista(self, parent, row):
        """Crea la sección que muestra la lista de empleados"""
        list_frame = ttk.LabelFrame(parent, text="👥 Lista de Empleados Registrados", padding="10")
        list_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        parent.rowconfigure(row, weight=1)
        
        # Crear Treeview con columnas
        columns = ('ID', 'Nombre', 'Sexo', 'Correo', 'Fecha Registro')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=16)
        
        # Configurar encabezados de columnas
        self.tree.heading('ID', text='ID Empleado')
        self.tree.heading('Nombre', text='Nombre Completo')
        self.tree.heading('Sexo', text='Sexo')
        self.tree.heading('Correo', text='Correo Electrónico')
        self.tree.heading('Fecha Registro', text='Fecha de Registro')
        
        # Configurar anchos de columnas
        self.tree.column('ID', width=120, anchor=tk.CENTER)
        self.tree.column('Nombre', width=250)
        self.tree.column('Sexo', width=120, anchor=tk.CENTER)
        self.tree.column('Correo', width=250)
        self.tree.column('Fecha Registro', width=150, anchor=tk.CENTER)
        
        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Grid del Treeview y scrollbar
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Bind evento de selección
        self.tree.bind('<<TreeviewSelect>>', self.seleccionar_empleado)
        
        # Etiqueta de contador
        self.contador_label = ttk.Label(list_frame, text="Total de empleados: 0", 
                                       font=('Arial', 9, 'bold'))
        self.contador_label.grid(row=1, column=0, sticky=tk.W, pady=(5, 0))
    
    def crear_seccion_controles(self, parent, row):
        """Crea la sección con los botones de control"""
        control_frame = ttk.Frame(parent)
        control_frame.grid(row=row, column=0, columnspan=3, pady=15)
        
        # Botones con estilos diferentes
        ttk.Button(control_frame, text="➕ Agregar Empleado", 
                  command=self.agregar_empleado, 
                  width=18).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(control_frame, text="🗑️ Eliminar Empleado", 
                  command=self.eliminar_empleado,
                  width=18).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(control_frame, text="🔄 Actualizar Lista", 
                  command=self.actualizar_lista_empleados,
                  width=15).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(control_frame, text="🧹 Limpiar Campos", 
                  command=self.limpiar_campos,
                  width=15).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(control_frame, text="📊 Estadísticas", 
                  command=self.mostrar_estadisticas,
                  width=12).pack(side=tk.LEFT, padx=8)
        
        ttk.Button(control_frame, text="❌ Salir", 
                  command=self.salir,
                  width=10).pack(side=tk.LEFT, padx=8)
    
    def agregar_empleado(self):
        """Agrega un nuevo empleado a la base de datos"""
        if not self.connection:
            messagebox.showerror("Error", "No hay conexión a la base de datos")
            return
        
        nombre = self.nombre_var.get().strip()
        sexo = self.sexo_var.get().strip()
        correo = self.correo_var.get().strip()
        
        # Validaciones
        if not nombre or not sexo or not correo:
            messagebox.showerror("Error", "❌ Todos los campos marcados con * son obligatorios")
            return
        
        if len(nombre) < 3:
            messagebox.showerror("Error", "❌ El nombre debe tener al menos 3 caracteres")
            return
        
        # Validación simple de correo
        if '@' not in correo or '.' not in correo:
            messagebox.showerror("Error", "❌ Por favor ingrese un correo electrónico válido")
            return
        
        try:
            cursor = self.connection.cursor()
            id_empleado = self.generar_id_unico()
            
            # Consulta segura con parámetros
            insert_query = "INSERT INTO empleados (id, nombre, sexo, correo) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (id_empleado, nombre, sexo, correo))
            self.connection.commit()
            cursor.close()
            
            messagebox.showinfo("✅ Éxito", 
                              f"Empleado agregado correctamente a la base de datos!\n\n"
                              f"📋 Detalles:\n"
                              f"• ID generado: {id_empleado}\n"
                              f"• Nombre: {nombre}\n"
                              f"• Sexo: {sexo}\n"
                              f"• Correo: {correo}")
            
            self.limpiar_campos()
            self.actualizar_lista_empleados()
            
        except Error as e:
            if "Duplicate entry" in str(e):
                messagebox.showerror("❌ Error", "El correo electrónico ya existe en la base de datos")
            else:
                messagebox.showerror("❌ Error", f"No se pudo agregar el empleado:\n{e}")
    
    def eliminar_empleado(self):
        """Elimina el empleado seleccionado de la base de datos"""
        if not self.connection:
            messagebox.showerror("Error", "No hay conexión a la base de datos")
            return
        
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "⚠️ Por favor seleccione un empleado de la lista")
            return
        
        item = seleccion[0]
        valores = self.tree.item(item, 'values')
        id_empleado = valores[0]
        nombre_empleado = valores[1]
        
        # Confirmación de eliminación
        confirmacion = messagebox.askyesno(
            "Confirmar Eliminación", 
            f"¿Está seguro de que desea ELIMINAR permanentemente al empleado?\n\n"
            f"🗄️  ID: {id_empleado}\n"
            f"👤 Nombre: {nombre_empleado}\n\n"
            "⚠️  Esta acción NO se puede deshacer y los datos se perderán permanentemente."
        )
        
        if confirmacion:
            try:
                cursor = self.connection.cursor()
                delete_query = "DELETE FROM empleados WHERE id = %s"
                cursor.execute(delete_query, (id_empleado,))
                self.connection.commit()
                affected_rows = cursor.rowcount
                cursor.close()
                
                if affected_rows > 0:
                    messagebox.showinfo("✅ Éxito", "Empleado eliminado correctamente de la base de datos")
                    self.actualizar_lista_empleados()
                    self.limpiar_campos()
                else:
                    messagebox.showerror("❌ Error", "No se encontró el empleado para eliminar")
                
            except Error as e:
                messagebox.showerror("❌ Error", f"No se pudo eliminar el empleado:\n{e}")
    
    def seleccionar_empleado(self, event):
        """Llena los campos del formulario con los datos del empleado seleccionado"""
        seleccion = self.tree.selection()
        if seleccion:
            item = seleccion[0]
            valores = self.tree.item(item, 'values')
            self.nombre_var.set(valores[1])
            self.sexo_var.set(valores[2])
            self.correo_var.set(valores[3])
    
    def actualizar_lista_empleados(self):
        """Actualiza la lista de empleados en el Treeview"""
        if not self.connection:
            return
            
        # Limpiar lista actual
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            cursor = self.connection.cursor(dictionary=True)
            # Consulta segura con formato de fecha
            select_query = """
            SELECT id, nombre, sexo, correo, 
                   DATE_FORMAT(fecha_creacion, '%d/%m/%Y %H:%i') as fecha 
            FROM empleados 
            ORDER BY fecha_creacion DESC
            """
            cursor.execute(select_query)
            empleados = cursor.fetchall()
            cursor.close()
            
            # Agregar empleados a la lista
            for empleado in empleados:
                self.tree.insert('', tk.END, values=(
                    empleado['id'],
                    empleado['nombre'],
                    empleado['sexo'],
                    empleado['correo'],
                    empleado['fecha']
                ))
            
            # Actualizar contador
            total_empleados = len(empleados)
            self.contador_label.config(text=f"Total de empleados registrados: {total_empleados}")
            
            if total_empleados == 0:
                self.tree.insert('', tk.END, values=(
                    "No hay empleados", "Registre el primer empleado", "", "", ""
                ))
                
        except Error as e:
            print(f"Error al obtener empleados: {e}")
            messagebox.showerror("Error", f"No se pudieron cargar los empleados:\n{e}")
    
    def buscar_empleados(self, event=None):
        """Busca empleados según el texto ingresado en la búsqueda"""
        if not self.connection:
            return
            
        criterio_busqueda = self.buscar_var.get().strip()
        
        if not criterio_busqueda:
            self.actualizar_lista_empleados()
            return
        
        # Limpiar lista actual
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            cursor = self.connection.cursor(dictionary=True)
            # Consulta segura con parámetros
            search_query = """
            SELECT id, nombre, sexo, correo, 
                   DATE_FORMAT(fecha_creacion, '%d/%m/%Y %H:%i') as fecha 
            FROM empleados 
            WHERE nombre LIKE %s OR correo LIKE %s OR id LIKE %s 
            ORDER BY nombre
            """
            parametro_busqueda = f"%{criterio_busqueda}%"
            cursor.execute(search_query, (parametro_busqueda, parametro_busqueda, parametro_busqueda))
            empleados = cursor.fetchall()
            cursor.close()
            
            # Agregar resultados a la lista
            for empleado in empleados:
                self.tree.insert('', tk.END, values=(
                    empleado['id'],
                    empleado['nombre'],
                    empleado['sexo'],
                    empleado['correo'],
                    empleado['fecha']
                ))
            
            # Actualizar contador de resultados
            total_resultados = len(empleados)
            self.contador_label.config(text=f"Resultados de búsqueda: {total_resultados}")
                
            # Mostrar mensaje si no hay resultados
            if not empleados:
                self.tree.insert('', tk.END, values=(
                    "No hay resultados", "Intente con otros términos de búsqueda", "", "", ""
                ))
                
        except Error as e:
            print(f"Error al buscar empleados: {e}")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas de los empleados"""
        if not self.connection:
            messagebox.showerror("Error", "No hay conexión a la base de datos")
            return
        
        try:
            cursor = self.connection.cursor()
            
            # Contar total de empleados
            cursor.execute("SELECT COUNT(*) as total FROM empleados")
            total = cursor.fetchone()[0]
            
            # Contar por sexo
            cursor.execute("SELECT sexo, COUNT(*) as cantidad FROM empleados GROUP BY sexo")
            por_sexo = cursor.fetchall()
            
            # Obtener fecha del primer registro
            cursor.execute("SELECT DATE_FORMAT(MIN(fecha_creacion), '%d/%m/%Y') as primera_fecha FROM empleados")
            primera_fecha = cursor.fetchone()[0] or "No hay registros"
            
            cursor.close()
            
            # Construir mensaje de estadísticas
            mensaje = f"📊 ESTADÍSTICAS DEL SISTEMA\n\n"
            mensaje += f"• Total de empleados registrados: {total}\n"
            mensaje += f"• Primer registro: {primera_fecha}\n\n"
            mensaje += "• Distribución por sexo:\n"
            
            for sexo, cantidad in por_sexo:
                porcentaje = (cantidad / total * 100) if total > 0 else 0
                mensaje += f"   - {sexo}: {cantidad} ({porcentaje:.1f}%)\n"
            
            messagebox.showinfo("Estadísticas del Sistema", mensaje)
            
        except Error as e:
            messagebox.showerror("Error", f"No se pudieron obtener las estadísticas:\n{e}")
    
    def limpiar_busqueda(self):
        """Limpia la búsqueda y muestra todos los empleados"""
        self.buscar_var.set("")
        self.actualizar_lista_empleados()
    
    def limpiar_campos(self):
        """Limpia los campos del formulario y deselecciona empleados"""
        self.nombre_var.set("")
        self.sexo_var.set("Masculino")  # Reset al valor por defecto
        self.correo_var.set("")
        # Deseleccionar cualquier empleado seleccionado
        seleccion = self.tree.selection()
        if seleccion:
            self.tree.selection_remove(seleccion)
    
    def salir(self):
        """Cierra la aplicación y la conexión a la base de datos"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("✅ Conexión a MySQL cerrada correctamente")
        self.root.quit()

def main():
    """Función principal que inicia la aplicación"""
    try:
        root = tk.Tk()
        app = SistemaEmpleados(root)
        root.mainloop()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        messagebox.showerror("Error Fatal", f"No se pudo iniciar la aplicación:\n{e}")

if __name__ == "__main__":
    main()