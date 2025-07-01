class Livro:
    total = 0
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Livro.total += 1
    @classmethod
    def mostrar_total(cls):
        print("Total de livros:", cls.total)
