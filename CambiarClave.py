import tkinter as tk
from tkinter import ttk
import sqlite3
import os

# Función para verificar la contraseña actual y el número de DNI
def verificar_password_dni():
    password_actual = password_actual_entry.get()
    dni_actual = dni_actual_entry.get()

    # Conectar a la base de datos
    try:
        conn = sqlite3.connect("UsuarioWallet.db")
        cursor = conn.cursor()

        # Verificar si la contraseña actual y el número de DNI son correctos
        cursor.execute("SELECT password, dni FROM usuarios WHERE id = 1")  # Cambia el "1" por el ID del usuario actual
        resultado = cursor.fetchone()

        if resultado is not None and resultado[0] == password_actual and resultado[1] == dni_actual:
            mensaje_label.config(text="Contraseña y DNI actuales correctos")
            # Habilitar la entrada para la nueva contraseña
            nueva_password_entry.config(state="normal")
            repetir_nueva_password_entry.config(state="normal")
            confirmar_boton.config(state="normal")
        else:
            mensaje_label.config(text="La contraseña o el DNI actual es incorrecto")
            nueva_password_entry.config(state="disabled")
            repetir_nueva_password_entry.config(state="disabled")
            confirmar_boton.config(state="disabled")

        conn.close()
    except sqlite3.Error as e:
        mensaje_label.config(text=f"Error de base de datos: {e}")
# Función para retroceder a la página principal (Main.py)
def retroceder_pagina():
    app.destroy()  # Cerrar la ventana actual
    os.system("python banca.py")  # Abrir el archivo Main.py

# Función para confirmar la nueva contraseña
def confirmar_nueva_password():
    nueva_password = nueva_password_entry.get()
    repetir_nueva_password = repetir_nueva_password_entry.get()

    # Verificar que la nueva contraseña y la repetición coincidan
    if nueva_password != repetir_nueva_password:
        mensaje_label.config(text="Las nuevas contraseñas no coinciden")
        return

    # Conectar a la base de datos
    try:
        conn = sqlite3.connect("UsuarioWallet.db")
        cursor = conn.cursor()

        # Actualizar la contraseña en la base de datos
        cursor.execute("UPDATE usuarios SET password = ? WHERE id = 1", (nueva_password,))
        conn.commit()
        conn.close()
        mensaje_label.config(text="Contraseña actualizada correctamente")

        # Cerrar la ventana actual y abrir "banca.py"
        app.destroy()
        os.system("python banca.py")
    except sqlite3.Error as e:
        mensaje_label.config(text=f"Error de base de datos: {e}")

# Crear la ventana principal
app = tk.Tk()
app.title("Billetera Virtual")
app.geometry("360x540")

background_color = "#ADD8E6"
app.configure(bg=background_color)

frame = ttk.Frame(app)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
frame.configure(borderwidth=2, relief="solid")

# Etiqueta y entrada para la contraseña actual
password_actual_label = ttk.Label(frame, text="Contraseña actual:")
password_actual_label.pack()

password_actual_entry = ttk.Entry(frame, show="*")  # La contraseña se muestra como asteriscos
password_actual_entry.pack()

# Etiqueta y entrada para el número de DNI actual
dni_actual_label = ttk.Label(frame, text="DNI actual:")
dni_actual_label.pack()

dni_actual_entry = ttk.Entry(frame)
dni_actual_entry.pack()

# Botón para verificar la contraseña actual y el número de DNI
verificar_boton = ttk.Button(frame, text="Verificar", command=verificar_password_dni)
verificar_boton.pack()

# Etiqueta y entrada para la nueva contraseña
nueva_password_label = ttk.Label(frame, text="Ingrese nueva contraseña:")
nueva_password_label.pack()

nueva_password_entry = ttk.Entry(frame, show="*", state="disabled")  # La nueva contraseña se muestra como asteriscos
nueva_password_entry.pack()

# Etiqueta y entrada para repetir la nueva contraseña
repetir_nueva_password_label = ttk.Label(frame, text="Repita nueva contraseña:")
repetir_nueva_password_label.pack()

repetir_nueva_password_entry = ttk.Entry(frame, show="*", state="disabled")  # La repetición se muestra como asteriscos
repetir_nueva_password_entry.pack()

# Botón para confirmar la nueva contraseña
confirmar_boton = ttk.Button(frame, text="Confirmar Nueva Contraseña", command=confirmar_nueva_password, state="disabled")
confirmar_boton.pack()

# Etiqueta para mostrar mensajes
mensaje_label = ttk.Label(frame, text="")
mensaje_label.pack()

# Botón para retroceder de página (flecha izquierda)
retroceder_button = ttk.Button(frame, text="←", command=retroceder_pagina)
retroceder_button.place(relx=0.1, rely=0.95, anchor=tk.SW)

app.mainloop()
