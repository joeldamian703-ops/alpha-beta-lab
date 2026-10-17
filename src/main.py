"""Comparación de Minimax y Poda Alfa-Beta."""

from src.alpha_beta import alpha_beta
from src.game_tree import (
    GameTree,
    medium_tree,
    ordered_tree_for_pruning,
    sample_tree,
)
from src.minimax import minimax


def compare_algorithms(name: str, tree: GameTree) -> None:
    minimax_result = minimax(tree)
    alpha_beta_result = alpha_beta(tree)

    saved = (
        minimax_result.nodes_evaluated
        - alpha_beta_result.nodes_evaluated
    )
    percentage = saved / minimax_result.nodes_evaluated * 100

    print(f"\nArbol: {name}")
    print(f"Valor Minimax: {minimax_result.value}")
    print(f"Valor Alfa-Beta: {alpha_beta_result.value}")
    print(f"Hojas Minimax: {minimax_result.nodes_evaluated}")
    print(f"Hojas Alfa-Beta: {alpha_beta_result.nodes_evaluated}")
    print(f"Ramas podadas: {alpha_beta_result.branches_pruned}")
    print(f"Reduccion de hojas evaluadas: {percentage:.2f}%")


def main() -> None:
    compare_algorithms("Pequeno", sample_tree())
    compare_algorithms("Mediano", medium_tree())
    compare_algorithms("Ordenado", ordered_tree_for_pruning())


if __name__ == "__main__":
    main()