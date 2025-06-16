import tkinter as tk
from tkinter import messagebox
from CRUD.create import insertar_producto
from CRUD.read import obtener_productos
from CRUD.update import actualizar_producto
from CRUD.delete import eliminar_producto


def agregar():
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()
    if not nombre or not cantidad or not precio:
        messagebox.showwarning("Campos incompletos", "Completa todos los campos.")
        return
    try:
        insertar_producto(nombre, int(cantidad), float(precio))
        mostrar()
        limpiar()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar():
    lista.delete(0, tk.END)
    for p in obtener_productos():
        lista.insert(tk.END, f"{p[0]} | {p[1]} | {p[2]} | ${p[3]:.2f}")

def eliminar():
    seleccion = lista.curselection()
    if not seleccion:
        messagebox.showinfo("Selecciona", "Selecciona un producto.")
        return
    id_producto = lista.get(seleccion[0]).split(" | ")[0]
    eliminar_producto(id_producto)
    mostrar()

def actualizar():
    seleccion = lista.curselection()
    if not seleccion:
        messagebox.showinfo("Selecciona", "Selecciona un producto.")
        return
    id_producto = lista.get(seleccion[0]).split(" | ")[0]
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()
    if not nombre or not cantidad or not precio:
        messagebox.showwarning("Campos incompletos", "Completa todos los campos.")
        return
    actualizar_producto(id_producto, nombre, int(cantidad), float(precio))
    mostrar()
    limpiar()

def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

# === Interfaz gráfica ===
root = tk.Tk()
root.title("Inventario CRUD Modularizado")

tk.Label(root, text="Nombre").grid(row=0, column=0)
tk.Label(root, text="Cantidad").grid(row=1, column=0)
tk.Label(root, text="Precio").grid(row=2, column=0)

entry_nombre = tk.Entry(root)
entry_cantidad = tk.Entry(root)
entry_precio = tk.Entry(root)

entry_nombre.grid(row=0, column=1)
entry_cantidad.grid(row=1, column=1)
entry_precio.grid(row=2, column=1)

tk.Button(root, text="Agregar", command=agregar).grid(row=0, column=2)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=1, column=2)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=2, column=2)

lista = tk.Listbox(root, width=50)
lista.grid(row=3, column=0, columnspan=3, pady=10)

mostrar()
root.mainloop()
