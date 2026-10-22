import pytest
from senha import forca


@pytest.mark.parametrize("senha, esperado", [
    ("abcdefgh", "media"),    # P2: referência, só letras, 8 voltas
    ("abc", "fraca"),         # P1: inverte o nó 2
    ("1bcdefgh", "media"),    # P3: inverte o nó 6 (dígito)
    ("!bcdefgh", "media"),    # P4: inverte o nó 8 (símbolo)
    ("!!bcdefg", "forte"),    # P5: inverte o nó 10 (pontos >= 4)
    ("abcdefghi", "media"),   # P6: 9 voltas, só letras
])
def test_base_de_caminhos(senha, esperado):
    assert forca(senha) == esperado


@pytest.mark.parametrize("senha, esperado", [
    ("abc", "fraca"),        # ramo V da linha 2
    ("ab1!!cde", "forte"),   # dígito, símbolo e letra no laço; 5 pontos
    ("abcdefgh", "media"),   # ramo F da linha 10
])
def test_minimo_para_ramos(senha, esperado):
    assert forca(senha) == esperado

@pytest.mark.parametrize("senha, esperado", [
    # tamanhos de laço (o de 8 e o de 9 voltas já estão na base: P2 e P6)
    ("ab1!" * 5, "forte"),      # típico: 20 voltas
    ("a" * 1000, "media"),      # muitas voltas
    # tamanhos que não chegam ao laço (inviáveis para o for)
    ("", "fraca"),              # 0 voltas
    ("abcdefg", "fraca"),       # 7 voltas: fronteira do if da linha 2
    # a primeira e a última volta precisam contar
    ("1abcd111", "forte"),      # 4 dígitos, o primeiro caractere decide
    ("111abcd1", "forte"),      # 4 dígitos, o último caractere decide
    # fronteira do pontos >= 4
    ("!1abcdef", "media"),      # 3 pontos
    ("!!abcdef", "forte"),      # 4 pontos
])
def test_lacos_e_fronteiras(senha, esperado):
    assert forca(senha) == esperado