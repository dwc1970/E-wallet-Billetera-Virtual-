import tkinter as tk
from tkinter import ttk
import sqlite3
import os

# Función para crear las tablas en la base de datos si no existen
def crear_tablas_si_no_existen():
    # Conectar a la base de datos o crearla si no existe
    conn = sqlite3.connect("movimientos.db")
    cursor = conn.cursor()

    # Crear la tabla movimientos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesos REAL,
            pago_en_pesos REAL,
            dolares REAL,
            pago_en_dolares REAL
        )
    """)

    # Guardar los cambios y cerrar la conexión a la base de datos
    conn.commit()
    conn.close()

# Función para obtener el último movimiento desde la base de datos "movimientos.db"
def obtener_ultimo_movimiento_movimientos():
    # Conectar a la base de datos
    conn = sqlite3.connect("movimientos.db")
    cursor = conn.cursor()

    # Obtener el último movimiento de la tabla movimientos
    cursor.execute("SELECT * FROM movimientos ORDER BY id DESC LIMIT 1")
    ultimo_movimiento = cursor.fetchone()

    # Cerrar la conexión a la base de datos
    conn.close()

    return ultimo_movimiento

# Función para crear las tablas en la base de datos "ul_mov.db" si no existen
def crear_tablas_si_no_existen_ul_mov():
    # Conectar a la base de datos o crearla si no existe
    conn = sqlite3.connect("ul_mov.db")
    cursor = conn.cursor()

    # Crear la tabla movimientos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ul_mov (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            saldo_dolares REAL,
            saldo_pesos REAL
        )
    """)

    # Guardar los cambios y cerrar la conexión a la base de datos
    conn.commit()
    conn.close()

# Función para obtener el último movimiento desde la base de datos "ul_mov.db"
def obtener_ultimo_movimiento_ul_mov():
    # Conectar a la base de datos
    conn = sqlite3.connect("ul_mov.db")
    cursor = conn.cursor()

    # Obtener el último movimiento de la tabla ul_mov
    cursor.execute("SELECT * FROM ul_mov ORDER BY id DESC LIMIT 1")
    ultimo_movimiento = cursor.fetchone()

    # Cerrar la conexión a la base de datos
    conn.close()

    return ultimo_movimiento

# Función para actualizar la información de saldo en la interfaz
def actualizar_saldo():
    # Obtener el último movimiento desde "movimientos.db"
    ultimo_movimiento_movimientos = obtener_ultimo_movimiento_movimientos()

    if ultimo_movimiento_movimientos:
        # Obtener los valores del último movimiento
        _, dolares_movimientos, pesos_movimientos, _ = ultimo_movimiento_movimientos
    else:
        # En caso de que no haya movimientos en la base de datos "movimientos.db"
        dolares_movimientos = 0
        pesos_movimientos = 0

    # Obtener el último movimiento desde "ul_mov.db"
    ultimo_movimiento_ul_mov = obtener_ultimo_movimiento_ul_mov()

    if ultimo_movimiento_ul_mov:
        # Obtener los valores del último movimiento
        _, saldo_dolares, saldo_pesos = ultimo_movimiento_ul_mov
    else:
        # En caso de que no haya movimientos en la base de datos "ul_mov.db"
        saldo_dolares = 0
        saldo_pesos = 0

    # Actualizar las etiquetas en la interfaz
    label_saldo_dolares.config(text=f"Saldo en Dólares (movimientos.db): {dolares_movimientos}")
    label_saldo_pesos.config(text=f"Saldo en Pesos (movimientos.db): {pesos_movimientos}")
    label_saldo_dolares_ul.config(text=f"Saldo en Dólares (ul_mov.db): {saldo_dolares}")
    label_saldo_pesos_ul.config(text=f"Saldo en Pesos (ul_mov.db): {saldo_pesos}")

# Función para cerrar la ventana actual y abrir el archivo "banca.py"
def cerrar_y_abrir_banca():
    app.destroy()
    os.system("python banca.py")

# Crear la ventana de la aplicación
app = tk.Tk()
app.title("Billetera Virtual")
app.geometry("360x540")  # Tamaño de pantalla de un celular estándar (360x540)

background_color = "#ADD8E6"
app.configure(bg=background_color)

# Contenedor principal (frame)
frame = ttk.Frame(app)
frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)
frame.configure(borderwidth=2, relief="solid")

# Etiquetas y resultados organizados en una sola columna y con 40 píxeles de separación vertical
label_saldo_dolares = tk.Label(frame, text="Saldo en Dólares: N/A", bg=background_color)
label_saldo_dolares.grid(row=0, column=0, padx=10, pady=40, sticky="w")

label_saldo_pesos = tk.Label(frame, text="Saldo en Pesos: N/A", bg=background_color)
label_saldo_pesos.grid(row=1, column=0, padx=10, pady=5, sticky="w")

label_saldo_dolares_ul = tk.Label(frame, text="Saldo en Dólares (ul_mov.db): N/A", bg=background_color)
label_saldo_dolares_ul.grid(row=2, column=0, padx=10, pady=5, sticky="w")

label_saldo_pesos_ul = tk.Label(frame, text="Saldo en Pesos (ul_mov.db): N/A", bg=background_color)
label_saldo_pesos_ul.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Botón para cerrar la ventana actual y abrir "banca.py"
boton_cerrar = ttk.Button(frame, text="Cerrar y Abrir Banca", command=cerrar_y_abrir_banca)
boton_cerrar.grid(row=4, column=0, pady=10)

# Configurar el sistema de filas y columnas para que los elementos estén centrados
frame.grid_rowconfigure(4, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Crear las tablas en las bases de datos si no existen
crear_tablas_si_no_existen()
crear_tablas_si_no_existen_ul_mov()

# Inicializar la información de saldo
actualizar_saldo()

# Ejecutar la aplicación
app.mainloop()
