class NO:
    def __init__(self, palavra, linha):
        self.palavra = palavra
        self.linhas = [linha]
        self.altura = 0
        self.esq = None
        self.dir = None

    def contar_elementos(self, no):
        """Retorna a contagem total de nós em uma subárvore."""
        if no is None:
            return 0
        return 1 + self.contar_elementos(no.esq) + self.contar_elementos(no.dir)