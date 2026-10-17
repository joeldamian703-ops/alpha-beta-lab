import pytest

from src.alpha_beta import alpha_beta
from src.game_tree import (
    medium_tree,
    ordered_tree_for_pruning,
    sample_tree,
)
from src.minimax import minimax


@pytest.mark.parametrize(
    "builder, expected, leaves",
    [
        (sample_tree, 3, 4),
        (medium_tree, 7, 12),
        (ordered_tree_for_pruning, 8, 12),
    ],
)
def test_resultados_y_reduccion(builder, expected, leaves):
    tree = builder()
    basic = minimax(tree)
    optimized = alpha_beta(tree)

    assert basic.value == expected
    assert optimized.value == expected
    assert basic.nodes_evaluated == leaves
    assert optimized.nodes_evaluated < basic.nodes_evaluated
    assert optimized.branches_pruned > 0


@pytest.mark.parametrize("algorithm", [minimax, alpha_beta])
def test_hoja_individual(algorithm):
    result = algorithm(-5)
    assert result.value == -5
    assert result.nodes_evaluated == 1


@pytest.mark.parametrize("algorithm", [minimax, alpha_beta])
def test_raiz_minimizadora(algorithm):
    result = algorithm(
        [[3, 5], [2, 9]],
        maximizing_player=False,
    )
    assert result.value == 5


@pytest.mark.parametrize("algorithm", [minimax, alpha_beta])
def test_arbol_vacio(algorithm):
    with pytest.raises(ValueError, match="listas vacías"):
        algorithm([])


@pytest.mark.parametrize("algorithm", [minimax, alpha_beta])
def test_valores_iguales(algorithm):
    result = algorithm([[4, 4], [4, 4]])
    assert result.value == 4
    
def test_programa_completo(capsys):
    import runpy

    runpy.run_module("src.main", run_name="__main__")
    output = capsys.readouterr().out

    assert output.count("Arbol:") == 3
    assert "Valor Minimax: 3" in output
    assert "Valor Minimax: 7" in output
    assert "Valor Minimax: 8" in output
    assert "Valor Alfa-Beta: 3" in output
    assert "Valor Alfa-Beta: 7" in output
    assert "Valor Alfa-Beta: 8" in output
    assert "Reduccion de hojas evaluadas: 25.00%" in output
    assert output.count(
        "Reduccion de hojas evaluadas: 33.33%"
    ) == 2