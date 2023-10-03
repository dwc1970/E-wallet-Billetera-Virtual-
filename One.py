import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import sys
import os

# Función para abrir "Main.py" y cerrar la ventana actual
def abrir_Main():
    try:
        # Obtiene la ruta al intérprete de Python actual
        python_exe = sys.executable
        # Ruta completa al archivo "Main.py"
        main_script = os.path.join(os.path.dirname(__file__), "Main.py")
        # Ejecuta "Main.py" con el intérprete de Python actual
        subprocess.Popen([python_exe, main_script])
        app.destroy()  # Cierra la ventana actual
    except Exception as e:
        print("Error al abrir Main.py:", e)

# Crear la ventana principal
app = tk.Tk()
app.title("Billetera Virtual")
app.geometry("360x540")  # Tamaño de pantalla de un celular estándar (360x640)
app.geometry("360x540")

# Contenedor principal (frame)
frame = ttk.Frame(app)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
frame.configure(borderwidth=2, relief="solid")

# Cargar la imagen de fondo
bg_image = Image.open("vito.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Crear un widget Label para mostrar la imagen de fondo centrada
bg_label = tk.Label(frame, image=bg_photo)
bg_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Botón de "Acceso"
boton_acceso = ttk.Button(frame, text="Ingrese a su Billetera", command=abrir_Main)
boton_acceso.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Ejecutar la aplicación
app.mainloop()
