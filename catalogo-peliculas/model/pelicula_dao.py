from .conexion_db import ConexionDB
from tkinter import messagebox


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

    try:
        # Ejecutar query
        conexion.cursor.execute(sql)
        # Cerrar la conexion a la BBDD
        conexion.cerrar()
        titulo = "Crear registro"
        mensaje = "Se creo la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = "Crear registro"
        mensaje = "La tabla ya esta creada"
        messagebox.showwarning(titulo, mensaje)


def borrar_tabla():
    conexion = ConexionDB()

    sql = "DROP TABLE peliculas"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Borrar registro"
        mensaje = "La tabla se borro con exito"
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = "Borrar registro"
        mensaje = "No hay tabla para borrar"
        messagebox.showerror(titulo, mensaje)


# Modelo de la pelicula
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    # Estado del objeto
    def __str__(self):
        return f"Pelicula[{self.nombre}, {self.duracion}, {self.genero}]"


# Func para guardar datos
def guardar(pelicula):
    # Me conecto a la base de datos
    conexion = ConexionDB()
    # Query para insertar data en la tabla.
    sql = f"""INSERT INTO peliculas(nombre, duracion, genero) VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""

    try:
        # Ejecuto la query
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Conexion al registro"
        mensaje = "La tabla pelicula no esta creada en la base de datos"
        messagebox.showwarning(titulo, mensaje)


# Listar datos
def listar():
    conexion = ConexionDB()

    # Lista vacia que recupera el registro
    lista_peliculas = []
    sql = "SELECT * FROM peliculas"

    try:
        conexion.cursor.execute(sql)
        # Agrego los datos a la lista
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = "Conexion al registro"
        mensaje = "Crear tabla en la bbdd"
        messagebox.showwarning(titulo, mensaje)

    return lista_peliculas


# Editar datos.
def editar(pelicula, id_pelicula):
    conexion = ConexionDB()

    sql = f"""UPDATE peliculas
  SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}'
  WHERE id_pelicula = {id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Edicion de datos"
        mensaje = "No se pudo editar los datos"
        messagebox.showerror(titulo, mensaje)


# Eliminar
def eliminar(id_pelicula):
    conexion = ConexionDB()

    sql = f"DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Eliminar Datos"
        mensaje = "No se pudo eliminar los datos"
        messagebox.showerror(titulo, mensaje)
