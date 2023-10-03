import tkinter as tk
from tkinter import ttk
import sqlite3
import subprocess

def guardar_datos():
    import sqlite3

    # Conectar a la base de datos (si no existe, se creará automáticamente)
    conn = sqlite3.connect("UsuarioWallet.db")

    # Crear una tabla llamada "usuarios" si no existe
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            apellido TEXT,
            dni TEXT,
            telefono TEXT,
            password TEXT
        )
    ''')

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

    # Obtener los datos ingresados por el usuario
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    dni = dni_entry.get()
    telefono = telefono_entry.get()
    password = password_entry.get()
    repite_password = repite_password_entry.get()

    # Validar los datos
    if nombre and apellido and dni and telefono and password and repite_password:
        if password == repite_password:
            try:
                # Conectar a la base de datos SQLite3
                conn = sqlite3.connect("UsuarioWallet.db")
                cursor = conn.cursor()

                # Insertar los datos en la tabla
                cursor.execute(
                    "INSERT INTO usuarios (nombre, apellido, dni, telefono, password) VALUES (?, ?, ?, ?, ?)",
                    (nombre, apellido, dni, telefono, password))

                # Guardar los cambios en la base de datos
                conn.commit()

                # Cerrar la conexión
                conn.close()

                # Limpiar los campos de entrada después de guardar los datos
                nombre_entry.delete(0, tk.END)
                apellido_entry.delete(0, tk.END)
                dni_entry.delete(0, tk.END)
                telefono_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                repite_password_entry.delete(0, tk.END)

                # Opcional: mostrar un mensaje de éxito o realizar otras acciones después de guardar los datos
                print("Datos guardados con éxito.")

                # Volver al archivo "Main.py"
                subprocess.Popen(["python", "Main.py"])

                # Cerrar la ventana actual
                app.destroy()
            except sqlite3.Error as e:
                print("Error al insertar datos en la base de datos:", e)
        else:
            print("Las contraseñas no coinciden.")
    else:
        # Mostrar un mensaje de error si faltan datos
        print("Por favor, complete todos los campos.")

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

# Botones y cajas dentro del contenedor
nombre_label = ttk.Label(frame, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=5, pady=5)
nombre_entry = ttk.Entry(frame)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

apellido_label = ttk.Label(frame, text="Apellido:")
apellido_label.grid(row=1, column=0, padx=5, pady=5)
apellido_entry = ttk.Entry(frame)
apellido_entry.grid(row=1, column=1, padx=5, pady=5)

dni_label = ttk.Label(frame, text="DNI:")
dni_label.grid(row=2, column=0, padx=5, pady=5)
dni_entry = ttk.Entry(frame)
dni_entry.grid(row=2, column=1, padx=5, pady=5)

telefono_label = ttk.Label(frame, text="Teléfono:")
telefono_label.grid(row=3, column=0, padx=5, pady=5)
telefono_entry = ttk.Entry(frame)
telefono_entry.grid(row=3, column=1, padx=5, pady=5)

password_label = ttk.Label(frame, text="Password:")
password_label.grid(row=4, column=0, padx=5, pady=5)
password_entry = ttk.Entry(frame, show="*")
password_entry.grid(row=4, column=1, padx=5, pady=5)

repite_password_label = ttk.Label(frame, text="Repite el Password:")
repite_password_label.grid(row=5, column=0, padx=5, pady=5)
repite_password_entry = ttk.Entry(frame, show="*")
repite_password_entry.grid(row=5, column=1, padx=5, pady=5)

aceptar_button = ttk.Button(frame, text="Aceptar", command=guardar_datos)
aceptar_button.grid(row=6, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
app.mainloop()
