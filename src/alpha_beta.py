"""Búsqueda Alfa-Beta con conteo de hojas y ramas omitidas."""

from dataclasses import dataclass

from src.game_tree import GameTree
from src.minimax import is_leaf


@dataclass
class AlphaBetaResult:
    value: int
    nodes_evaluated: int
    branches_pruned: int


def alpha_beta(
    node: GameTree,
    alpha: float = float("-inf"),
    beta: float = float("inf"),
    maximizing_player: bool = True,
) -> AlphaBetaResult:
    if is_leaf(node):
        return AlphaBetaResult(node, 1, 0)

    if not node:
        raise ValueError("El árbol no puede contener listas vacías")

    nodes_evaluated = 0
    branches_pruned = 0
    value = float("-inf") if maximizing_player else float("inf")

    for index, child in enumerate(node):
        result = alpha_beta(
            child, alpha, beta, not maximizing_player
        )

        nodes_evaluated += result.nodes_evaluated
        branches_pruned += result.branches_pruned

        if maximizing_player:
            value = max(value, result.value)
            alpha = max(alpha, value)
        else:
            value = min(value, result.value)
            beta = min(beta, value)

        if beta <= alpha:
            branches_pruned += len(node) - index - 1
            break

    return AlphaBetaResult(
        value=int(value),
        nodes_evaluated=nodes_evaluated,
        branches_pruned=branches_pruned,
    )