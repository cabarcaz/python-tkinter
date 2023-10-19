from .conexion_db import ConexionDB


# Crear tablas
def crear_tablas():
    # Objeto para realizar la conexion
    conexion = ConexionDB()

    # Crear query
    sql = """
    CREATE TABLE peliculas(
      id_pelicula INTEGER,
      nombre VARCHAR(100),
      duracion VARCHAR(10),
      genero VARCHAR(100),
      PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    """

    # Ejecutar query
    conexion.cursor.execute(sql)
    # Cerrar la conexion a la BBDD
    conexion.cerrar()


def borrar_tabla():
    conexion = ConexionDB()

    sql = "DROP TABLE peliculas"

    conexion.cursor.execute(sql)
    conexion.cerrar()
