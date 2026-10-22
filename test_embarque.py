import pytest
from embarque import pode_embarcar
from mcdc import regra


@pytest.mark.parametrize("entrada", [
    (True, True, True, True),      # todos V
    (False, False, False, False),  # todos F
])
def test_todos_v_e_todos_f(entrada):
    assert pode_embarcar(*entrada) == regra(*entrada)

from mcdc import regra, tabela_verdade, conjuntos_minimos


def pode_embarcar_defeituoso(cartao, documento, grupo_chamado, prioridade):
    """Cópia da versão original, com o defeito de precedência."""
    if cartao and documento and grupo_chamado or prioridade:
        return True
    return False


def acha_defeito(conjunto):
    linhas = tabela_verdade(4)
    return any(
        pode_embarcar_defeituoso(*linhas[i - 1]) != regra(*linhas[i - 1])
        for i in conjunto
    )


@pytest.mark.parametrize("conjunto, acha", [
    ((2, 3, 4, 6, 10), False),   # M1
    ((2, 3, 4, 7, 10), True),    # M2
    ((2, 3, 4, 6, 11), True),    # M3
    ((2, 3, 4, 7, 11), True),    # M4
])
def test_conjuntos_mcdc_contra_defeito(conjunto, acha):
    assert acha_defeito(conjunto) == acha


def test_os_quatro_conjuntos_sao_os_calculados():
    assert len(conjuntos_minimos(regra, 4)) == 4


def test_mcc_acha_o_defeito():
    assert acha_defeito(range(1, 17))


def test_funcao_corrigida_em_todas_as_16_linhas():
    for linha in tabela_verdade(4):
        assert pode_embarcar(*linha) == regra(*linha)