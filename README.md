# Índice Remissivo com Árvore AVL

Este projeto automatiza a criação de um índice remissivo a partir de um arquivo de texto. Ele identifica as palavras, registra em quais linhas aparecem e organiza tudo em uma Árvore AVL para garantir que a busca e a inserção sejam sempre rápidas, mesmo com textos grandes.

#  Como funciona?

A lógica do programa segue três passos simples:
**Leitura:** O arquivo texto_origem.txt é lido linha por linha.

**Processamento:** Usamos Regex para extrair apenas palavras (removendo pontuação) e as inserimos na árvore em letras minúsculas.

**Balanceamento:** A cada nova palavra, a árvore verifica se ficou "torta". Se o peso de um lado for muito maior que o outro, ela executa rotações automáticas para se manter equilibrada (O(log n)).

#  Estrutura do Código:

**no.py**:
Define o nó da árvore. Além da palavra e dos ponteiros (esquerda/direita), ele guarda uma lista com os números das linhas onde a palavra foi encontrada e sua altura atual na árvore.

**avl.py e sua lógica:**

Inserção/Remoção: Faz o trabalho padrão de busca binária, mas dispara o rebalanceamento logo em seguida.

Rotações (LL, RR, LR, RL): Funções que reorganizam os ponteiros para manter a árvore balanceada.

Busca de Prefixo: Retorna todas as palavras que começam com um determinado termo (ex: "prog" -> "programação", "programa").

Medidor de Equilíbrio (ME): Uma função extra que calcula a diferença de quantidade de nós entre a subárvore esquerda e direita de uma palavra específica.

**main.py**:
Lê o arquivo de entrada, alimenta a árvore e gera o arquivo final indice_remissivo.txt. No final da execução, ele exibe estatísticas como tempo de construção, total de rotações e a palavra mais frequente.

#  Exemplos de Uso:

**O que entra (texto_origem.txt)**


Dados e algoritmos.
Busca em árvore.
Algoritmos são dados.

        
**O que sai (indice_remissivo.txt)**


As palavras aparecem em ordem alfabética seguidas pelas linhas:


algoritmos 1, 3
árvore 2
busca 2
dados 1, 3

Total de palavras: 8
Palavras distintas: 4
Rotações: 2


**Busca por Prefixo**

No console, você pode testar buscas rápidas:

#Exemplo interno:

arv.busca_prefixo("alg") 

#Saída: ['algoritmos']


**Medidor de Equilíbrio**

O sistema permite verificar o quão distribuída está a árvore abaixo de um nó:


Digite uma palavra para buscar o ME: dados
ME calculado para 'dados': 1
A palavra foi encontrada e seu ME foi impresso acima.
