"""Una editorial de libros y discos desea crear fichas que almacenen el título y el
precio de cada publicación. Definir la correspondiente clase Publicacion que
implemente los datos anteriores. Derive dos clases, una llamada Libro, que
contenga para cada libro el número de páginas, año de publicación y precio, y la
clase Disco, con la duración en minutos y precio. Programar una aplicación que
pruebe las clases."""

class Publicacion:
    def ___init__(self, titulo: str, precio: int):
        self.titulo = titulo
        self.precio = precio

class Libro(Publicacion):
    def __init__(self, titulo, precio, paginas: int, añoPublicacion: int ):
        super().__init__(titulo, precio)
        self.paginas= paginas
        self.añoPublicacion = añoPublicacion

        
class Discos(Publicacion): 
    def __init__(self, titulo, precio, duracion: int) :
        super().__init__(titulo, precio)
        self.duracion = duracion        
        
#faltan pruebas
