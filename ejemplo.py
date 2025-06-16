import tkinter as tk
from tkinter import messagebox

# Lista para guardar el inventario
inventario = []

# Función para agregar producto
def agregar_producto():
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()

    if not nombre or not cantidad.isdigit():
        messagebox.showerror("Error", "Ingrese un nombre y una cantidad válida.")
        return

    inventario.append({"Producto": nombre, "Cantidad": int(cantidad)})
    actualizar_lista()
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

# Función para mostrar inventario en la lista
def actualizar_lista():
    lista.delete(0, tk.END)
    for producto in inventario:
        lista.insert(tk.END, f"{producto['Producto']} - {producto['Cantidad']} unidades")

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Inventario")
ventana.geometry("400x300")

# Etiquetas y campos
tk.Label(ventana, text="Producto:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Cantidad:").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

# Botón
tk.Button(ventana, text="Agregar", command=agregar_producto).pack(pady=10)

# Lista para mostrar inventario
lista = tk.Listbox(ventana, width=50)
lista.pack()

# Ejecutar ventana
ventana.main()

#fin del codigo