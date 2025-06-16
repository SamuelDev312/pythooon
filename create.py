from db import cursor, conn


def insertar_producto(nombre, cantidad, precio):
    cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
                   (nombre, cantidad, precio))
    conn.commit()
