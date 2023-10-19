# SQLite no necestia servidor.

import sqlite3


# Conexion a la base de datos
class ConexionDB:
    def __init__(self):
        # Especificamos la ruta de la ubicacion del archivo de la BBDD
        self.base_datos = "database/peliculas.db"
        # Variable para realizar la conexion
        self.conexion = sqlite3.connect(self.base_datos)
        # Cursor para realizar las consultas
        self.cursor = self.conexion.cursor()

    # Cerrar la conexion a la BBDD
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
