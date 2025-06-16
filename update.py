from db import cursor, conn


def actualizar_producto(id_producto, nombre, cantidad, precio):
    cursor.execute("UPDATE productos SET nombre=?, cantidad=?, precio=? WHERE id=?",
                   (nombre, cantidad, precio, id_producto))
    conn.commit()
