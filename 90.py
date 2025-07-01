class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def detalhes(self):
        print(f"{self.titulo} por {self.autor}, {self.paginas} páginas")
