from db import cursor, conn


def obtener_productos():
    cursor.execute("SELECT * FROM productos")
    return cursor.fetchall()
