import pytest
from preco import preco_final


@pytest.mark.parametrize("preco, vip, esperado", [
    (60, True, 50),      # suíte original: o mínimo mascara o desconto duplo
    (200, False, 200),   # suíte original
    (30, False, 50),     # completa All-Uses: par (2, 6, V)
    (200, True, 160),    # completa All-Uses: pares (5, 6, F) e (5, 8)
])
def test_preco_final(preco, vip, esperado):
    assert preco_final(preco, vip) == pytest.approx(esperado)