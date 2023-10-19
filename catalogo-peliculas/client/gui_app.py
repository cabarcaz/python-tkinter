# Importo la libreria de UI
import tkinter as tk


#! Creo menu de la app, recibe la ventana principal
def barra_menu(root):
    barra_menu = tk.Menu(root)
    # Anclar barra de menu a la ventana principal
    root.config(menu=barra_menu, width=-300, height=300)
    # ? Objeto que contiene la opcion del menu y el submenu.
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
    #! Submenu del menu de inicio
    menu_inicio.add_command(label="Crear nuevo registro")
    menu_inicio.add_command(label="Eliminar registro")
    # opcion salir funcional.
    menu_inicio.add_command(label="Salir", command=root.destroy)
    #! Debo crear el objeto completo si quiero mas opciones y que sean funcionales
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Consultas", menu=menu_inicio)
    menu_inicio.add_command(label="Consulta 1")
    menu_inicio.add_command(label="Consulta 2")

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Configuaración", menu=menu_inicio)
    menu_inicio.add_command(label="Confi 1")
    menu_inicio.add_command(label="Confi 2")

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Ayuda", menu=menu_inicio)
    menu_inicio.add_command(label="Ayuda 1")
    menu_inicio.add_command(label="Ayuda 2")


# ? Creo el frame
class Frame(tk.Frame):
    # Creo el constructor de la clase
    def __init__(self, root=None):
        # Heredo el construcctor de la clase padre
        super().__init__(root)
        self.root = root
        # Empaqueto la aplicacion
        self.pack()
        # Configuro tamaño del frame
        self.config(width=500, height=500)

        # Ejecuto o llamo a los campos
        self.campos_pelicula()
        # Llamo al metodo para que se inicie todo desabilitado.
        self.desabilitar_campos()

    #! Label para opciones de llenado(campos)
    def campos_pelicula(self):
        # Label de cada campo nombre
        self.label_nombre = tk.Label(self, text="Nombre: ")
        # Personalizo la config del label
        self.label_nombre.config(font=("Arial", 12, "bold"))
        # Especifico posicion del label
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text="Duración: ")
        self.label_duracion.config(font=("Arial", 12, "bold"))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text="Genero: ")
        self.label_genero.config(font=("Arial", 12, "bold"))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        #! Entry o input
        # Limpiar campos
        self.mi_nombre = tk.StringVar()
        # Objeto entry/input para el campo nombre
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        # Personalizo el conf del input.
        self.entry_nombre.config(font=("Arial", 12), width=50)
        # Posicion del input
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(font=("Arial", 12), width=50)
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(font=("Arial", 12), width=50)
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #! Botones
        # Objeto de boton
        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        # Configuracion/personalizacion del boton
        self.boton_nuevo.config(
            font=("Arial", 12, "bold"),
            width=20,
            fg="#DAD5D6",
            bg="#158645",
            cursor="hand2",
            activebackground="#35BD6F",
        )
        # Posicionamiento del boton
        self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.config(
            font=("Arial", 12, "bold"),
            width=20,
            fg="#DAD5D6",
            bg="#1658A2",
            cursor="hand2",
            activebackground="#3586DF",
        )
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(
            self, text="Cancelar", command=self.desabilitar_campos
        )
        self.boton_cancelar.config(
            font=("Arial", 12, "bold"),
            width=20,
            fg="#DAD5D6",
            bg="#BD152E",
            cursor="hand2",
            activebackground="#E15370",
        )
        self.boton_cancelar.grid(row=4, column=2, padx=10, pady=10)

    # ? Habilitar Campos
    def habilitar_campos(self):
        # Envio campos vacios
        self.mi_nombre.set("")
        self.mi_duracion.set("")
        self.mi_genero.set("")

        self.entry_nombre.config(state="normal")
        self.entry_duracion.config(state="normal")
        self.entry_genero.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    # ? Deshabilitar Campos
    def desabilitar_campos(self):
        # Envio campos vacios
        self.mi_nombre.set("")
        self.mi_duracion.set("")
        self.mi_genero.set("")

        # Desabilito los input
        self.entry_nombre.config(state="disabled")
        self.entry_duracion.config(state="disabled")
        self.entry_genero.config(state="disabled")

        # Desabilito los botones
        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    def guardar_datos(self):
        self.desabilitar_campos()
