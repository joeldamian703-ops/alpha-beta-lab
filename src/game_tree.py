"""Árboles de juego con listas como ramas y enteros como hojas."""

from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]


def sample_tree() -> GameTree:
    """Árbol pequeño. Valor Minimax esperado: 3."""
    return [
        [3, 5],
        [2, 9],
    ]


def medium_tree() -> GameTree:
    """Árbol mediano. Valor Minimax esperado: 7."""
    return [
        [[3, 5], [6, 9]],
        [[1, 2], [0, -1]],
        [[7, 4], [8, 6]],
    ]


def ordered_tree_for_pruning() -> GameTree:
    """Árbol ordenado para favorecer la poda. Valor esperado: 8."""
    return [
        [[10, 9], [8, 7]],
        [[6, 5], [4, 3]],
        [[2, 1], [0, -1]],
    ]