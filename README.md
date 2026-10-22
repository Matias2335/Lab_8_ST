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

## Exercício 1 - d) Teste de laços

O `if len(senha) < 8` da linha 2 retorna antes do `for`, então o laço só executa com senhas de 8 ou mais caracteres. O laço tem **mínimo de 8 voltas** e nenhum máximo.

| Caso | Voltas | Viável? | Entrada |
|---|---|---|---|
| Zero voltas | 0 | Não | `""` retorna `"fraca"` na linha 3 |
| Uma e duas voltas | 1, 2 | Não | senha curta, retorna na linha 3 |
| Mínimo − 1 | 7 | Não | `"abcdefg"` retorna `"fraca"` |
| Mínimo | 8 | Sim | `"abcdefgh"` (P2 da base) |
| Mínimo + 1 | 9 | Sim | `"abcdefghi"` (P6 da base) |
| Típico | 20 | Sim | `"ab1!" * 5` |
| Muitas voltas | 1000 | Sim | `"a" * 1000` |
| n − 1, n, n + 1 | - | Não se aplica | não existe número máximo de voltas |

Os casos inviáveis continuam no teste (`""` e `"abcdefg"`) porque confirmam a fronteira do `if` da linha 2: eles mostram que o laço não é alcançado, e não que ele dá poucas voltas.

Casos acrescentados:
- **Típico e muitas voltas:** 20 e 1000 voltas, para o laço acumular pontos em várias voltas.
- **Primeira e última volta:** `"1abcd111"` e `"111abcd1"` somam 4 pontos apenas se o primeiro (ou o último) caractere for lido. Detectam defeitos de limite como `for c in senha[1:]` ou `for c in senha[:-1]`.
- **Fronteira do `pontos >= 4`:** `"!1abcdef"` (3 pontos, `"media"`) e `"!!abcdef"` (4 pontos, `"forte"`).

Resultado:

<img width="927" height="352" alt="image" src="https://github.com/user-attachments/assets/dcb15cc6-4160-4026-a444-2d20109ef745" />


Todos os testes passam. A cobertura de ramos já era 100% antes desses casos: eles não aumentam a cobertura, aumentam a chance de achar defeitos nas voltas do laço.

## Exercício 2 - a) `mcdc.py`

Implementadas em `mcdc.py`:

- `regra(cartao, documento, grupo_chamado, prioridade)`: escrita direto da especificação, `cartao and documento and (grupo_chamado or prioridade)`.
- `pares_independentes(decisao, n)`: para cada condição, devolve os pares de linhas da tabela-verdade (numeradas de 1, com V antes de F) que diferem só nela e mudam a decisão.

Saída de `python mcdc.py`:

<img width="796" height="161" alt="image" src="https://github.com/user-attachments/assets/00f129b0-69ad-40f9-ae39-f947675416ac" />

## Exercício 2 - b) Pares e conjuntos MC/DC mínimos

A decisão só é V nas linhas 1 (VVVV), 2 (VVVF) e 3 (VVFV), e F nas demais.

| Condição | Pares | Quantidade |
|---|---|---|
| cartao | (1,9), (2,10), (3,11) | 3 |
| documento | (1,5), (2,6), (3,7) | 3 |
| grupo_chamado | (2,4) | 1 |
| prioridade | (3,4) | 1 |

**Conjuntos mínimos:** grupo_chamado e prioridade têm um único par cada, (2,4) e (3,4), então as linhas 2, 3 e 4 entram sempre. Para cartao, os pares (2,10) e (3,11) reaproveitam a linha 2 ou a 3 e acrescentam só uma linha nova (10 ou 11). Para documento, vale o mesmo com (2,6) e (3,7), que acrescentam 6 ou 7. As linhas F de cartao (9, 10, 11) e de documento (5, 6, 7) nunca coincidem, então nenhuma linha atende às duas condições ao mesmo tempo.

O mínimo é **5 casos** (n + 1) e existem **4 conjuntos mínimos**, 2 escolhas para cartao vezes 2 para documento:

| Conjunto | Linhas |
|---|---|
| M1 | 2, 3, 4, 6, 10 |
| M2 | 2, 3, 4, 7, 10 |
| M3 | 2, 3, 4, 6, 11 |
| M4 | 2, 3, 4, 7, 11 |

O MCC exigiria 2⁴ = 16 casos.

## Exercício 2 - c) Todos V e todos F

Comparação de `pode_embarcar` com `regra` em dois testes:

| Teste | Entrada | `regra` | `pode_embarcar` |
|---|---|---|---|
| Todos V | (V, V, V, V) | True | True |
| Todos F | (F, F, F, F) | False | False |

As duas funções concordam nos dois testes: o defeito **não é detectado**. Em todos V, `cartao and documento and grupo_chamado` já é V; em todos F, as duas partes do `or` são F. A divergência só aparece quando `prioridade` é V e alguma das outras condições é F.

Medição de ramos:

```
pytest -q -k todos --cov=embarque --cov-branch --cov-report=term-missing
```

<img width="1026" height="300" alt="image" src="https://github.com/user-attachments/assets/c6730d86-3084-4376-9ff5-0c96ca5a7695" />


Os dois testes dão **100% de ramos**: todos V percorre o ramo V do `if` e todos F percorre o ramo F. Ou seja, uma suíte com 100% de ramos passa sem ver o defeito, porque C1 só exige que a decisão assuma V e F, e não que cada condição mostre seu efeito.

## Exercício 2 - d) Conjuntos MC/DC e correção

**Defeito:** em Python `and` tem precedência sobre `or`, então o código avalia `(cartao and documento and grupo_chamado) or prioridade`, enquanto a especificação pede `cartao and documento and (grupo_chamado or prioridade)`. As duas divergem quando `prioridade` é V e `cartao` ou `documento` é F (linhas 5, 7, 9, 11, 13 e 15 da tabela): o código deixa embarcar sem cartão ou sem documento.

| Conjunto | Linhas | Linha divergente | Acha o defeito? |
|---|---|---|---|
| M1 | 2, 3, 4, 6, 10 | nenhuma | não |
| M2 | 2, 3, 4, 7, 10 | 7 | sim |
| M3 | 2, 3, 4, 6, 11 | 11 | sim |
| M4 | 2, 3, 4, 7, 11 | 7 e 11 | sim |

**Explicação:** M1 usa as linhas 6 e 10 para os pares de documento e cartao, e nelas `prioridade` é F, então o `or prioridade` não atua e as funções coincidem. M2, M3 e M4 incluem a linha 7 (VFFV) ou a 11 (FVFV), com `prioridade` V e uma condição obrigatória F, onde a precedência faz diferença. Conjuntos MC/DC mínimos diferentes acham defeitos diferentes.

**MCC:** executa as 16 combinações, incluindo as linhas divergentes, então sempre acharia o defeito (16 casos contra 5).

**Correção:**

```python
def pode_embarcar(cartao, documento, grupo_chamado, prioridade):
    if cartao and documento and (grupo_chamado or prioridade):
        return True
    return False
```

Após a correção, `pode_embarcar` e `regra` concordam nas 16 linhas, e todos os testes passam.

<img width="887" height="227" alt="image" src="https://github.com/user-attachments/assets/7975c3c2-c569-4fa9-99b0-ba69ba0319e2" />

## Exercício 3 - a) Definições, usos e pares du

| Variável | Linha | Tipo |
|---|---|---|
| `total` | 2 | def |
| `total` | 5 | c-use e def |
| `total` | 6 | p-use |
| `total` | 7 | def |
| `total` | 8 | c-use |
| `desconto` | 4 | def |
| `desconto` | 5 | c-use |

Na linha 5, o uso de `total` precede a nova definição, então a definição da linha 5 não alcança o uso da própria linha 5. A linha 7 só define `total`, portanto não há par (2, 7).

**Pares du de `total`** (o p-use da linha 6 gera um par por ramo):

| Par | Tipo | Caminho exigido | Exemplo |
|---|---|---|---|
| (2, 5) | c-use | VIP | `(60, True)` |
| (2, 6, V) | p-use | sem VIP, preço abaixo de 50 | `(30, False)` |
| (2, 6, F) | p-use | sem VIP, preço a partir de 50 | `(200, False)` |
| (2, 8) | c-use | sem VIP, preço a partir de 50 | `(200, False)` |
| (5, 6, V) | p-use | VIP, total com desconto abaixo de 50 | `(60, True)` |
| (5, 6, F) | p-use | VIP, total com desconto a partir de 50 | `(200, True)` |
| (5, 8) | c-use | VIP, total com desconto a partir de 50 | `(200, True)` |
| (7, 8) | c-use | passa pelo mínimo de R$50 | `(30, False)` |

**Pares du de `desconto`:**

| Par | Tipo | Caminho exigido | Exemplo |
|---|---|---|---|
| (4, 5) | c-use | VIP | `(60, True)` |

Total: 9 pares du (8 de `total` e 1 de `desconto`).

## Exercício 3 - b) Pares não percorridos pela suíte atual

A suíte atual, `preco_final(60, True) == 50` e `preco_final(200, False) == 200`, tem 100% de ramos.

**Teste `(60, True)`:** `total = 60` (linha 2), `desconto = 12` (linha 4), `total = 36` (linha 5), `36 < 50` é V, `total = 50` (linha 7), `return 50`. Percorre (2,5), (4,5), (5,6,V) e (7,8).

**Teste `(200, False)`:** `total = 200` (linha 2), pula o `if vip`, `200 < 50` é F, `return 200`. Percorre (2,6,F) e (2,8).

| Par | Tipo | Percorrido? |
|---|---|---|
| (2, 5) | c-use | sim |
| (2, 6, V) | p-use | **não** |
| (2, 6, F) | p-use | sim |
| (2, 8) | c-use | sim |
| (5, 6, V) | p-use | sim |
| (5, 6, F) | p-use | **não** |
| (5, 8) | c-use | **não** |
| (7, 8) | c-use | sim |
| (4, 5) | c-use | sim |

**Não percorridos (3 de 9):**

- **(2, 6, V):** sem VIP e preço abaixo de 50.
- **(5, 6, F) e (5, 8):** VIP com total com desconto a partir de 50. Nenhum teste leva o valor com desconto ao `return` sem passar pelo mínimo.

A suíte cobre todos os ramos, mas não todos os pares du.

## Exercício 3 - c) All-Uses, defeito e por que a suíte não o viu

**O que falta (da especificação):** VIP tem 20% de desconto e todo pedido custa no mínimo R$50.

| Teste | Esperado | Pares que cobre |
|---|---|---|
| `(30, False)` | 50 | (2, 6, V) |
| `(200, True)` | 160 | (5, 6, F) e (5, 8) |

Com `(60, True)` e `(200, False)`, esses 4 testes cobrem os 9 pares du (All-Uses).

**O que acontece:** a linha 5, `total = total * 0.8 - desconto`, aplica o desconto duas vezes: `total * 0.8` já desconta 20%, e `desconto = preco * 0.2` desconta outros 20%. O VIP paga 60% do preço. `(200, True)` devolve 120 e a especificação pede 160, então o teste falha.

**Por que a suíte atual não viu:** o único teste VIP, `(60, True)`, dá 36 pelo código e 48 pela especificação. Os dois são menores que 50 e o `if total < 50` os substitui por 50, escondendo o erro. Nenhum teste levava o valor com desconto da linha 5 direto ao `return` da linha 8, o par (5, 8). A suíte tinha 100% de ramos, mas esse par du ficava de fora.

Resultado antes da correção:

<img width="992" height="370" alt="image" src="https://github.com/user-attachments/assets/a73850b7-9006-4408-a001-97e8ddce1c8e" />

## Exercício 3 - d) Correção e suíte completa

**Correção:** a linha 5 subtraía o `desconto` depois de já multiplicar por 0,8, aplicando o desconto de 20% duas vezes. A correção retira o `* 0.8` e mantém a subtração do desconto:

```python
def preco_final(preco, vip):
    total = preco
    if vip:
        desconto = preco * 0.2
        total = total - desconto
    if total < 50:
        total = 50
    return total
```

A estrutura de definições e usos é a mesma dos itens (a) e (b), então os 9 pares du seguem válidos.

Com a função corrigida, `(200, True)` devolve 160, como a especificação pede, e os 4 testes de `test_preco.py` passam.

Suíte inteira:

(colar aqui a captura de `pytest -q` com tudo passando)

Cobertura:

<img width="863" height="372" alt="image" src="https://github.com/user-attachments/assets/cfc00512-ccb6-4081-bf2d-176a6d2cb40b" />


