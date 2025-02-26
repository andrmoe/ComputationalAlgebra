from typing import TypeVar, Callable, Iterable
from copy import deepcopy

A = TypeVar("A")


def generic_enumeration(
    n: int,
    default: A,
    search_range_func: Callable[[int, [A], float], Iterable[A]],
    score_func: Callable[[list[A]], float],
    initial_score_bound,
) -> tuple[list[A], float]:

    def sub_search(i: int, a: [A], score_bound: float) -> tuple[list[A], float]:
        if i < 0:
            return a, score_func(a)
        search_range = search_range_func(i, a, score_bound)

        best_score = score_bound
        best_a = []
        for ai in search_range:
            next_a = deepcopy(a)
            next_a[i] = ai
            next_a, score = sub_search(i - 1, next_a, min(best_score, score_bound))
            if score < best_score:
                best_score = score
                best_a = next_a
        return best_a, best_score

    return sub_search(n - 1, [default for _ in range(n)], initial_score_bound)
