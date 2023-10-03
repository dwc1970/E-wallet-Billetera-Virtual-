import os
import tkinter as tk
from tkinter import ttk
import sqlite3
import subprocess

# Función para abrir "CambiarClave.py" y cerrar la ventana actual
def abrir_cambiar_clave():
    try:
        # Abre "CambiarClave.py" usando el comando "python"
        subprocess.Popen(["python", "CambiarClave.py"])
        app.destroy()  # Cierra la ventana actual
    except FileNotFoundError:
        print("Error al abrir CambiarClave.py")

# Función para registrar un movimiento en la base de datos SQLite
def registrar_movimiento(accion, monto, moneda, saldo_actual):
    conn = sqlite3.connect("movimientos.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movimientos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        accion TEXT,
                        monto REAL,
                        moneda TEXT,
                        saldo_actual REAL,
                        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    cursor.execute('''INSERT INTO movimientos (accion, monto, moneda, saldo_actual)
                      VALUES (?, ?, ?, ?)''', (accion, monto, moneda, saldo_actual))
    conn.commit()
    conn.close()

# Función para ver los últimos movimientos
def ver_ultimos_movimientos():
    try:
        # Abre "U_M.py" usando el comando "python"
        subprocess.Popen(["python", "U_M.py"])
        app.destroy()  # Cierra la ventana actual
    except FileNotFoundError:
        print("Error al abrir U_M.py")

# Función para abrir "saldo.py" y cerrar la ventana actual
def ver_saldo():
    try:
        # Abre "saldo.py" usando el comando "python"
        subprocess.Popen(["python", "saldo.py"])
        app.destroy()  # Cierra la ventana actual
    except FileNotFoundError:
        print("Error al abrir saldo.py")

# Funciones para otras opciones (ver_billetera, etc.)
def ver_billetera():
    try:
        # Abre "billetera_1.py" usando el comando "python"
        subprocess.Popen(["python", "billetera_1.py"])
        app.destroy()  # Cierra la ventana actual
    except FileNotFoundError:
        print("Error al abrir billetera_1.py")

# Función para cerrar sesión y abrir "One.py"
def cerrar_sesion():
    app.destroy()  # Cerrar la ventana actual
    os.system("python One.py")  # Abrir el archivo One.py

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
frame.configure(borderwidth=2, relief="solid")

# Crear un LabelFrame para organizar los botones en grupos de dos
botones_frame = ttk.LabelFrame(frame, text="Opciones")
botones_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Botones organizados en grupos de dos (arriba y abajo)
boton_cambiar_clave = ttk.Button(botones_frame, text="Cambiar Clave", command=abrir_cambiar_clave)
boton_cambiar_clave.grid(row=0, column=0, padx=5, pady=(5, 25), sticky="ew")
boton_billetera = ttk.Button(botones_frame, text="Tu Billetera", command=ver_billetera)
boton_billetera.grid(row=0, column=1, padx=5, pady=(5, 25), sticky="ew")
boton_saldo = ttk.Button(botones_frame, text="Tu Saldo", command=ver_saldo)
boton_saldo.grid(row=1, column=0, padx=5, pady=(5, 25), sticky="ew")
boton_ultimos_movimientos = ttk.Button(botones_frame, text="Últimos Movimientos", command=ver_ultimos_movimientos)
boton_ultimos_movimientos.grid(row=1, column=1, padx=5, pady=(5, 25), sticky="ew")

# Botón "Cerrar Sesión"
boton_cerrar_sesion = ttk.Button(frame, text="Cerrar Sesión", command=cerrar_sesion)
boton_cerrar_sesion.grid(row=2, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

# Iniciar la aplicación
app.mainloop()
