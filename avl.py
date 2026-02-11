# Nomes: Camila Gomes Barbosa e Pedro Lucas Carvalho Mendes
from no import NO

class AVL:
    def __init__(self):
        self._raiz = None
        self.total_rotacoes = 0
        self.palavras_descartadas = 0 # repetidas na mesma linha

    def _altura(self, no):
        return no.altura if no else -1

    def _fatorBalanceamento(self, no):
        """Diferença de altura entre subárvores."""
        if not no: return 0
        return self._altura(no.esq) - self._altura(no.dir)

    def _maior(self, x, y):
        return x if x > y else y

    def _RotacaoLL(self, A):
        self.total_rotacoes += 1
        B = A.esq
        A.esq = B.dir
        B.dir = A
        A.altura = self._maior(self._altura(A.esq), self._altura(A.dir)) + 1
        B.altura = self._maior(self._altura(B.esq), A.altura) + 1
        return B

    def _RotacaoRR(self, A):
        self.total_rotacoes += 1
        B = A.dir
        A.dir = B.esq
        B.esq = A
        A.altura = self._maior(self._altura(A.esq), self._altura(A.dir)) + 1
        B.altura = self._maior(self._altura(B.dir), A.altura) + 1
        return B

    def _RotacaoLR(self, A):
        A.esq = self._RotacaoRR(A.esq)
        return self._RotacaoLL(A)

    def _RotacaoRL(self, A):
        A.dir = self._RotacaoLL(A.dir)
        return self._RotacaoRR(A)

    # inserção
    def insere(self, palavra, linha):
        self._raiz = self._insereValor(self._raiz, palavra, linha)

    def _insereValor(self, atual, palavra, linha):
        if atual is None:
            return NO(palavra, linha)
        
        if palavra == atual.palavra:
            if linha not in atual.linhas:
                atual.linhas.append(linha)
            else:
                self.palavras_descartadas += 1
            return atual
        
        if palavra < atual.palavra:
            atual.esq = self._insereValor(atual.esq, palavra, linha)
            if abs(self._fatorBalanceamento(atual)) >= 2:
                if palavra < atual.esq.palavra:
                    atual = self._RotacaoLL(atual)
                else:
                    atual = self._RotacaoLR(atual)
        else:
            atual.dir = self._insereValor(atual.dir, palavra, linha)
            if abs(self._fatorBalanceamento(atual)) >= 2:
                if palavra > atual.dir.palavra:
                    atual = self._RotacaoRR(atual)
                else:
                    atual = self._RotacaoRL(atual)

        atual.altura = self._maior(self._altura(atual.esq), self._altura(atual.dir)) + 1
        return atual

    # remoção
    def remove(self, palavra, linha):
        self._raiz = self._removeLogica(self._raiz, palavra, linha)

    def _removeLogica(self, atual, palavra, linha):
        if not atual: return None
        
        if palavra < atual.palavra:
            atual.esq = self._removeLogica(atual.esq, palavra, linha)
        elif palavra > atual.palavra:
            atual.dir = self._removeLogica(atual.dir, palavra, linha)
        else:
            # encontra a palavra
            if linha in atual.linhas:
                atual.linhas.remove(linha)
            
            # se ainda restam linhas, mantem o nó
            if len(atual.linhas) > 0:
                return atual
            
            # caso contrário, remove o nó
            if not atual.esq or not atual.dir:
                atual = atual.esq if atual.esq else atual.dir
            else:
                temp = self._procuraMenor(atual.dir)
                atual.palavra, atual.linhas = temp.palavra, temp.linhas
                atual.dir = self._removeLogica(atual.dir, temp.palavra, temp.linhas[0])
        
        if not atual: return None
        atual.altura = self._maior(self._altura(atual.esq), self._altura(atual.dir)) + 1
        return self._rebalancear(atual)

    def _procuraMenor(self, atual):
        while atual.esq: atual = atual.esq
        return atual

    def _rebalancear(self, no):
        fb = self._fatorBalanceamento(no)
        if fb >= 2:
            if self._fatorBalanceamento(no.esq) >= 0: return self._RotacaoLL(no)
            return self._RotacaoLR(no)
        if fb <= -2:
            if self._fatorBalanceamento(no.dir) <= 0: return self._RotacaoRR(no)
            return self._RotacaoRL(no)
        return no

    # funções extras
    def busca_prefixo(self, prefixo):
        lista = []
        def percorrer(no):
            if no:
                percorrer(no.esq)
                if no.palavra.startswith(prefixo): lista.append(no.palavra)
                percorrer(no.dir)
        percorrer(self._raiz)
        return lista

    def busca_ME(self, palavra):
        no = self._buscar(self._raiz, palavra)
        if not no: return -1
        me = no.contar_elementos(no.esq) - no.contar_elementos(no.dir)
        if me == 0: return 0
        print(f"ME calculado para '{palavra}': {me}")
        return 1

    def _buscar(self, no, palavra):
        if not no or no.palavra == palavra: return no
        return self._buscar(no.esq if palavra < no.palavra else no.dir, palavra)

    def mais_frequente(self):
        self.mf_palavra = ""
        self.mf_count = 0
        def percorrer(no):
            if no:
                percorrer(no.esq)
                if len(no.linhas) > self.mf_count:
                    self.mf_count = len(no.linhas)
                    self.mf_palavra = no.palavra
                percorrer(no.dir)
        percorrer(self._raiz)
        return self.mf_palavra
