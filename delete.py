from db import cursor, conn


def eliminar_producto(id_producto):
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conn.commit()
