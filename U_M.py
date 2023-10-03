import tkinter as tk
from tkinter import ttk
import sqlite3
import subprocess

# Crear la ventana principal
app = tk.Tk()
app.title("Billetera Virtual")
app.geometry("360x540")  # Tamaño de pantalla de un celular estándar (360x800)

# Fondo azul claro
background_color = "#ADD8E6"
app.configure(bg=background_color)

# Contenedor principal (frame)
frame = ttk.Frame(app)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# Crear una función para cargar los datos desde la base de datos y mostrarlos en una tabla
def cargar_datos():
    # Conectar a la base de datos "movimientos.db"
    conexion = sqlite3.connect("movimientos.db")
    cursor = conexion.cursor()

    # Obtener los últimos 4 registros
    cursor.execute("SELECT * FROM movimientos ORDER BY id DESC LIMIT 4")
    datos = cursor.fetchall()

    # Cerrar la conexión
    conexion.close()

    # Crear una tabla para mostrar los datos
    tabla = ttk.Treeview(frame, columns=("ID", "Acción", "Monto", "Moneda"))
    tabla.heading("#1", text="ID")
    tabla.heading("#2", text="Acción")
    tabla.heading("#3", text="Monto")
    tabla.heading("#4", text="Moneda")

    # Insertar los datos en la tabla
    for fila in datos:
        tabla.insert("", "end", values=fila)

    tabla.pack()

# Función para abrir "banca.py" y cerrar la ventana actual
def abrir_banca():
    app.destroy()  # Cerrar la ventana actual
    subprocess.run(["python", "banca.py"])  # Ejecutar el archivo "banca.py"

# Agregar un botón para regresar
boton_regresar = ttk.Button(frame, text="Regresar", command=abrir_banca)
boton_regresar.pack()

# Llamar a la función para cargar y mostrar los datos
cargar_datos()

# Iniciar la aplicación
app.mainloop()
