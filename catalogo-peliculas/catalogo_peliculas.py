# Importar liberia de UI
import tkinter as tk
from client.gui_app import Frame, barra_menu


# Función principal
def main():
    # Raiz o ventana principal del proyecto
    root = tk.Tk()
    # Agregar un titulo a la ventana.
    root.title("Catalogo de peliculas")
    # Agragar logo a la app
    root.iconbitmap("img/cp-logo.ico")
    # Definir si se puede ajustar o no la ventana 0 no se modifica, 1 se modifica
    root.resizable(0, 0)
    # ? # Frame contenedor de elementos, se vincula a la ventana principal
    # ? frame = tk.Frame(root)
    # ? # Debo empaquetar el frame
    # ? frame.pack()
    # ? # Definir tamaño del frame
    # ? frame.config(width=400, height=400)

    # Ejecuto la bara del menu agregada a la ventana principal
    barra_menu(root)
    # Importo el modulo de frame.
    app = Frame(root=root)

    # Se agrega al final para mantener en funcionamiento el programa.
    app.mainloop()


# Entri point
if __name__ == "__main__":
    main()
