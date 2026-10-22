# Lab_8_ST

## Exercício 1 - a) GFC de `forca` e V(G)

### Grafo de fluxo de controle

Cada nó é o número da linha do comando em `senha.py`. Os losangos são nós de decisão (`if`, `elif`, `for`) e os três `return` levam ao nó `fim`.

<img width="4484" height="7374" alt="Senha Strength Classification Flow-2026-10-22-225242" src="https://github.com/user-attachments/assets/ba84a75d-b893-448a-9a0f-19b329f9ff61" />


### Contagem

- **Nós (N):** 12 (linhas 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 e o nó `fim`)
- **Arestas (E):** 16
  2→3, 2→4, 3→fim, 4→5, 5→6, 5→10, 6→7, 6→8, 7→5, 8→9, 8→5, 9→5, 10→11, 10→12, 11→fim, 12→fim
- **Nós de decisão (P):** 5 (linhas 2, 5, 6, 8 e 10; o `elif` da linha 8 conta como decisão própria)

### Complexidade ciclomática

| Fórmula | Cálculo | Resultado |
|---|---|---|
| V(G) = E − N + 2 | 16 − 12 + 2 | **6** |
| V(G) = P + 1 | 5 + 1 | **6** |

As duas fórmulas coincidem: **V(G) = 6**, então a base de caminhos terá 6 caminhos linearmente independentes.

## Exercício 1 - b) Base de caminhos

### Arestas numeradas (para os vetores)

| Aresta | Trecho | Aresta | Trecho |
|---|---|---|---|
| e1 | 2→3 | e9 | 7→5 |
| e2 | 2→4 | e10 | 8→9 |
| e3 | 3→fim | e11 | 8→5 |
| e4 | 4→5 | e12 | 9→5 |
| e5 | 5→6 | e13 | 10→11 |
| e6 | 5→10 | e14 | 10→12 |
| e7 | 6→7 | e15 | 11→fim |
| e8 | 6→8 | e16 | 12→fim |

### Base com V(G) = 6 caminhos

Método do caminho de referência: parte-se de um caminho típico (P2, só letras, 8 voltas) e inverte-se uma decisão por vez.

| Caminho | Como foi obtido, na ordem | Entrada | Esperado |
|---|---|---|---|
| P2 | referência: senha típica só com letras, 8 voltas | `"abcdefgh"` | `"media"` |
| P1 | inverte o nó 2; aresta nova 2→3 | `"abc"` | `"fraca"` |
| P3 | inverte o nó 6; aresta nova 6→7 | `"1bcdefgh"` | `"media"` |
| P4 | inverte o nó 8; aresta nova 8→9 | `"!bcdefgh"` | `"media"` |
| P5 | inverte o nó 10; aresta nova 10→11 (exige trocar letras por símbolos para chegar a 4 pontos) | `"!!bcdefg"` | `"forte"` |
| P6 | inverter o nó 5 daria zero voltas (inviável); troca por 9 voltas só com letras | `"abcdefghi"` | `"media"` |

### Vetores dos caminhos (nº de vezes que passa por cada aresta)

| Caminho | e1 | e2 | e3 | e4 | e5 | e6 | e7 | e8 | e9 | e10 | e11 | e12 | e13 | e14 | e15 | e16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| P2 | 0 | 1 | 0 | 1 | 8 | 1 | 0 | 8 | 0 | 0 | 8 | 0 | 0 | 1 | 0 | 1 |
| P3 | 0 | 1 | 0 | 1 | 8 | 1 | 1 | 7 | 1 | 0 | 7 | 0 | 0 | 1 | 0 | 1 |
| P4 | 0 | 1 | 0 | 1 | 8 | 1 | 0 | 8 | 0 | 1 | 7 | 1 | 0 | 1 | 0 | 1 |
| P5 | 0 | 1 | 0 | 1 | 8 | 1 | 0 | 8 | 0 | 2 | 6 | 2 | 1 | 0 | 1 | 0 |
| P6 | 0 | 1 | 0 | 1 | 9 | 1 | 0 | 9 | 0 | 0 | 9 | 0 | 0 | 1 | 0 | 1 |

### Justificativa da independência

Suponha a·P1 + b·P2 + c·P3 + d·P4 + e·P5 + f·P6 = 0. Posição por posição:

- **e1:** só P1 passa por 2→3, então a = 0.
- **e7:** só P3 passa por 6→7, então c = 0.
- **e13:** só P5 passa por 10→11, então e = 0.
- **e10:** só P4 passa por 8→9 entre os que sobraram, então d = 0.
- **e6 e e5:** restam P2 e P6. Em e6 temos b + f = 0, e em e5 temos 8b + 9f = 0. Substituindo b = −f: −8f + 9f = f = 0, logo b = 0.

Todos os coeficientes são zero, então nenhum vetor é combinação linear dos outros. Os 6 caminhos formam uma base, com o tamanho exigido por V(G) = 6.

P2 e P6 percorrem as mesmas arestas e diferem só no número de voltas do ciclo 5→6→8→5 (8 contra 9). É essa diferença nos contadores que os torna independentes.

### Caminho inviável

O caminho **2→4→5→10→…** (zero voltas do `for`, aresta 5→10 logo depois do 4→5) é **inviável**. Para passar do `if` da linha 2, a senha precisa ter pelo menos 8 caracteres, então o `for` dá no mínimo 8 voltas e nunca vai direto de 5 para 10 na primeira vez. É por isso que, ao inverter o nó 5 a partir da referência, o caminho resultante não é executável e foi substituído por P6 (9 voltas).

Por consequência, qualquer caminho com menos de 8 voltas depois do nó 4 também é inviável. Entre os viáveis, P2 e P6 são o mínimo (8 voltas) e o mínimo mais um.


## Exercício 1 - c) Teste parametrizado e cobertura

Os 6 caminhos da base são viáveis e foram implementados em `test_base_de_caminhos` com `@pytest.mark.parametrize`.

Medição:

```
pytest -q --cov=senha --cov-branch --cov-report=term-missing
```

<img width="927" height="218" alt="image" src="https://github.com/user-attachments/assets/b303d08b-576a-4b48-8789-acdbb4ee7050" />

<img width="941" height="255" alt="image" src="https://github.com/user-attachments/assets/3661fff9-7109-4241-8a3f-d01624584073" />

### Quantos testes dão 100% de ramos?

| Conjunto | Nº de testes | Ramos |
|---|---|---|
| Base de caminhos | 6 = V(G) | 100% |
| Conjunto mínimo para C1 | 3 | 100% |

O conjunto mínimo é `"abc"` (ramo V da linha 2), `"ab1!!cde"` (dígito, símbolo e letra no laço, 5 pontos, ramo V da linha 10) e `"abcdefgh"` (ramo F da linha 10).

Dois testes não bastam: o ramo V da linha 2 só se alcança com senha curta, que termina em `"fraca"` e não executa o resto da função. Os ramos V e F da linha 10 exigem então dois outros testes, o que dá no mínimo 3.

**Conclusão:** C1 pede 3 testes e a base pede V(G) = 6, coerente com a relação testes de C0 ≤ testes de C1 ≤ V(G) da aula. A base cobre todos os ramos, mas um conjunto menor já basta para C1. Os testes a mais da base exercitam caminhos que C1 não exige: por exemplo, o P3 e o P4 isolam o dígito e o símbolo em senhas que terminam em "media", e o P6 acrescenta uma volta ao laço (9 contra 8).
