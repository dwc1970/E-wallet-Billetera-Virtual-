import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import os
import subprocess

def verificar_clave():
    clave = clave_entry.get()

    # Conectar a la base de datos SQLite3
    conn = sqlite3.connect("UsuarioWallet.db")
    cursor = conn.cursor()

    # Buscar la clave en la base de datos
    cursor.execute("SELECT COUNT(*) FROM usuarios WHERE password=?", (clave,))
    resultado = cursor.fetchone()[0]

    # Cerrar la conexión
    conn.close()

    if resultado > 0:
        # Clave correcta
        mensaje_label.config(text="Clave correcta")
        # Abre el archivo "banca.py"
        abrir_banca()
        # Cierra la ventana actual
        app.destroy()
    else:
        # Clave incorrecta
        mensaje_label.config(text="Clave incorrecta")

def abrir_banca():
    # Abre el archivo "banca.py" usando el comando "python"
    try:
        subprocess.Popen(["python", "banca.py"])
    except FileNotFoundError:
        mensaje_label.config(text="Error al abrir banca.py")

def abrir_registro():
    # Abre el archivo "validar_datos.py" usando el comando "python"
    try:
        subprocess.Popen(["python", "validar_datos.py"])
        # Cierra la ventana actual
        app.destroy()
    except FileNotFoundError:
        mensaje_label.config(text="Error al abrir validar_datos.py")

# Crear la ventana principal
app = tk.Tk()
app.title("Billetera Virtual")
app.geometry("360x540")  # Tamaño de pantalla de un celular estándar (360x640)

# Fondo azul claro
background_color = "#ADD8E6"
app.configure(bg=background_color)

# Contenedor principal (frame)
frame = ttk.Frame(app)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
frame.configure(borderwidth=2, relief="solid")

# Etiqueta de "Billetera Virtual"
titulo_label = ttk.Label(frame, text="Billetera Virtual", font=("Helvetica", 18))
titulo_label.pack(pady=20)

# Etiqueta "Ingresar Clave"
clave_label = ttk.Label(frame, text="Ingresar Clave:")
clave_label.pack(pady=10)

# Entrada para la clave
clave_entry = ttk.Entry(frame, show="*")  # La clave se muestra como asteriscos
clave_entry.pack(pady=10)

# Botón para ingresar
ingresar_button = ttk.Button(frame, text="Ingresar", command=verificar_clave)
ingresar_button.pack()

# Botón para registrarse
registro_button = ttk.Button(frame, text="Registrarse", command=abrir_registro)
registro_button.pack()

# Etiqueta para mostrar mensajes
mensaje_label = ttk.Label(frame, text="", foreground="red")
mensaje_label.pack()

# Ejecutar la aplicación
app.mainloop()
