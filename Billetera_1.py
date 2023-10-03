import tkinter as tk
from tkinter import ttk
import sqlite3
import os
import subprocess

# Función para cargar saldo en pesos y dólares
def cargar_saldo():
    monto = float(cargar_saldo_entry.get())
    saldo_actual = float(saldo_label.cget("text").split("$")[1])
    nuevo_saldo = saldo_actual + monto
    saldo_label.config(text=f"Saldo: ${nuevo_saldo:.2f}")

    # Guardar el registro en la base de datos
    agregar_movimiento("Cargar Saldo", monto, "Pesos")

# Función para pagar con dinero
def pagar_dinero():
    monto = float(pagar_dinero_entry.get())
    saldo_actual = float(saldo_label.cget("text").split("$")[1])
    if saldo_actual >= monto:
        nuevo_saldo = saldo_actual - monto
        saldo_label.config(text=f"Saldo: ${nuevo_saldo:.2f}")

        # Guardar el registro en la base de datos
        agregar_movimiento("Pagar con Pesos", -monto, "Pesos")
    else:
        resultado_label.config(text="Saldo insuficiente")

# Función para cargar dólares
def cargar_dolares():
    monto = float(cargar_dolares_entry.get())
    saldo_actual_dolares = float(saldo_dolares_label.cget("text").split("$")[1])
    nuevo_saldo_dolares = saldo_actual_dolares + monto
    saldo_dolares_label.config(text=f"Saldo en Dólares: ${nuevo_saldo_dolares:.2f}")

    # Guardar el registro en la base de datos
    agregar_movimiento("Cargar Dólares", monto, "Dólares")

# Función para pagar con dólares
def pagar_dolares():
    monto = float(pagar_dolares_entry.get())
    saldo_actual_dolares = float(saldo_dolares_label.cget("text").split("$")[1])
    if saldo_actual_dolares >= monto:
        nuevo_saldo_dolares = saldo_actual_dolares - monto
        saldo_dolares_label.config(text=f"Saldo en Dólares: ${nuevo_saldo_dolares:.2f}")

        # Guardar el registro en la base de datos
        agregar_movimiento("Pagar con Dólares", -monto, "Dólares")
    else:
        resultado_dolares_label.config(text="Saldo en Dólares insuficiente")

# Función para agregar un registro de movimiento en la base de datos
def agregar_movimiento(accion, monto, moneda):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "movimientos.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movimientos (accion, monto, moneda) VALUES (?, ?, ?)", (accion, monto, moneda))
    conn.commit()
    conn.close()

# Función para retroceder de página
def retroceder_pagina():
    # Cerrar la ventana actual
    app.destroy()

    # Abrir el archivo "banca.py" en un nuevo proceso
    subprocess.Popen(['python', 'banca.py'])

# Crear la base de datos SQLite3
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "movimientos.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS movimientos (id INTEGER PRIMARY KEY AUTOINCREMENT, accion TEXT, monto REAL, moneda TEXT)")
conn.commit()
conn.close()

# Crear la ventana principal
app = tk.Tk()
app.title("Billetera Virtual")
app.geometry("360x540")

# Fondo azul claro
background_color = "#ADD8E6"
app.configure(bg=background_color)

# Contenedor principal (frame)
frame = ttk.Frame(app)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
frame.configure(borderwidth=2, relief="solid")

# Etiqueta para el saldo en pesos
saldo_label = ttk.Label(frame, text="Saldo: $0.00")
saldo_label.pack(pady=10)

# Botón y entrada para cargar saldo en pesos y dólares
cargar_saldo_label = ttk.Label(frame, text="Cargar Saldo:")
cargar_saldo_label.pack()
cargar_saldo_entry = ttk.Entry(frame)
cargar_saldo_entry.pack()
cargar_saldo_button = ttk.Button(frame, text="Cargar", command=cargar_saldo)
cargar_saldo_button.pack()

# Botón y entrada para pagar con pesos
pagar_dinero_label = ttk.Label(frame, text="Pagar con Pesos:")
pagar_dinero_label.pack()
pagar_dinero_entry = ttk.Entry(frame)
pagar_dinero_entry.pack()
pagar_dinero_button = ttk.Button(frame, text="Pagar", command=pagar_dinero)
pagar_dinero_button.pack()
resultado_label = ttk.Label(frame, text="")
resultado_label.pack()

# Etiqueta para el saldo en dólares
saldo_dolares_label = ttk.Label(frame, text="Saldo en Dólares: $0.00")
saldo_dolares_label.pack(pady=10)

# Botón y entrada para cargar dólares
cargar_dolares_label = ttk.Label(frame, text="Cargar Dólares:")
cargar_dolares_label.pack()
cargar_dolares_entry = ttk.Entry(frame)
cargar_dolares_entry.pack()
cargar_dolares_button = ttk.Button(frame, text="Cargar", command=cargar_dolares)
cargar_dolares_button.pack()

# Botón y entrada para pagar con dólares
pagar_dolares_label = ttk.Label(frame, text="Pagar con Dólares:")
pagar_dolares_label.pack()
pagar_dolares_entry = ttk.Entry(frame)
pagar_dolares_entry.pack()
pagar_dolares_button = ttk.Button(frame, text="Pagar", command=pagar_dolares)
pagar_dolares_button.pack()
resultado_dolares_label = ttk.Label(frame, text="")
resultado_dolares_label.pack()

# Crear el botón de retroceso
retroceder_button = ttk.Button(frame, text="←", command=retroceder_pagina)
retroceder_button.place(relx=0.1, rely=0.95, anchor=tk.SW)

app.mainloop()
