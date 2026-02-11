# Nomes: Camila Gomes Barbosa e Pedro Lucas Carvalho Mendes
import time
import re
from avl import AVL

def formatar_resultado_me(valor):
    if valor == -1: return "Palavra não encontrada no índice."
    if valor == 0: return "A palavra foi encontrada e está em perfeito equilíbrio (ME = 0)."
    return "A palavra foi encontrada e seu ME foi impresso acima."

def main():
    arv = AVL()
    total_p = 0
    inicio = time.time()
    
    try:
        with open('texto_origem.txt', 'r', encoding='utf-8') as f:
            for i, linha in enumerate(f, 1):
                palavras = re.findall(r'\b\w+\b', linha.lower())
                for p in palavras:
                    total_p += 1
                    arv.insere(p, i)
    except FileNotFoundError:
        print("Erro: 'texto_origem.txt' não encontrado.")
        return

    fim = time.time()
    tempo_total = fim - inicio

    p_distintas = 0
    with open('indice_remissivo.txt', 'w', encoding='utf-8') as out:
        def salvar(no):
            nonlocal p_distintas
            if no:
                salvar(no.esq)
                out.write(f"{no.palavra} {', '.join(map(str, sorted(no.linhas)))}\n")
                p_distintas += 1
                salvar(no.dir)
        salvar(arv._raiz)
        
        out.write("\n" + "-"*30 + "\n")
        out.write(f"Número total de palavras: {total_p}\n")
        out.write(f"Número de palavras distintas: {p_distintas}\n")
        out.write(f"Total de palavras descartadas (repetidas na linha): {arv.palavras_descartadas}\n")
        out.write(f"Tempo de construção: {tempo_total:.4f}s\n")
        out.write(f"Total de rotações executadas: {arv.total_rotacoes}\n")

    print(f"Palavra mais frequente: {arv.mais_frequente()}")
    print(f"Busca por prefixo 'alg': {arv.busca_prefixo('alg')}")
    
    print("\n--- Teste de Medidor de Equilíbrio ---")
    palavra_teste = input("Digite uma palavra para buscar o ME: ").lower()
    resultado = arv.busca_ME(palavra_teste)
    print(formatar_resultado_me(resultado))

if __name__ == "__main__":
    main()
