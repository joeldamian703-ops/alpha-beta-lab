"""Búsqueda Minimax y conteo de hojas evaluadas."""

from dataclasses import dataclass

from src.game_tree import GameTree


@dataclass
class SearchResult:
    value: int
    nodes_evaluated: int


def is_leaf(node: GameTree) -> bool:
    return isinstance(node, int)


def minimax(
    node: GameTree,
    maximizing_player: bool = True,
) -> SearchResult:
    if is_leaf(node):
        return SearchResult(value=node, nodes_evaluated=1)

    if not node:
        raise ValueError("El árbol no puede contener listas vacías")

    results = [
        minimax(child, not maximizing_player)
        for child in node
    ]

    total_leaves = sum(
        result.nodes_evaluated for result in results
    )

    if maximizing_player:
        best_value = max(result.value for result in results)
    else:
        best_value = min(result.value for result in results)

    return SearchResult(
        value=best_value,
        nodes_evaluated=total_leaves,
    )