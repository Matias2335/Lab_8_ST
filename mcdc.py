from itertools import product


def regra(cartao, documento, grupo_chamado, prioridade):
    """Direto da especificação: embarca quem tem cartão E documento válido,
    E cujo grupo já foi chamado OU que tem prioridade."""
    return cartao and documento and (grupo_chamado or prioridade)


def tabela_verdade(n):
    """Todas as 2**n linhas, na ordem da aula: V antes de F.
    Linha 1 = (V,...,V) e última linha = (F,...,F)."""
    return list(product([True, False], repeat=n))


def pares_independentes(decisao, n):
    """Para cada condição i (0 a n-1), devolve a lista de pares (a, b) de
    linhas da tabela-verdade (numeradas de 1) que diferem SÓ na condição i
    e mudam o valor da decisão."""
    linhas = tabela_verdade(n)
    pares = {i: [] for i in range(n)}
    for a in range(len(linhas)):
        for b in range(a + 1, len(linhas)):
            diferem = [i for i in range(n) if linhas[a][i] != linhas[b][i]]
            if len(diferem) == 1 and decisao(*linhas[a]) != decisao(*linhas[b]):
                pares[diferem[0]].append((a + 1, b + 1))
    return pares
from itertools import combinations

def conjuntos_minimos(decisao, n):
    pares = pares_independentes(decisao, n)
    for tamanho in range(n + 1, 2 ** n + 1):
        achados = []
        for conj in combinations(range(1, 2 ** n + 1), tamanho):
            s = set(conj)
            if all(any(a in s and b in s for a, b in pares[i]) for i in range(n)):
                achados.append(conj)
        if achados:
            return achados

if __name__ == "__main__":
    nomes = ["cartao", "documento", "grupo_chamado", "prioridade"]
    for i, lista in pares_independentes(regra, 4).items():
        print(nomes[i], lista)
    print("conjuntos mínimos:", conjuntos_minimos(regra, 4))