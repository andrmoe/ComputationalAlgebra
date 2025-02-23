import numpy as np
from gram_schmidt import gram_schmidt_basis


def search_bounds(i: int, a: np.ndarray, bstar: np.ndarray, r: np.ndarray[np.float64], A: float) -> np.ndarray:
    if i == a.shape[0] - 1:
        return np.array((0.0, A))
    Ai = np.sqrt(A ** 2 - np.sum(r[i + 1:, i + 1:].dot(a[i + 1:]) ** 2)) / np.linalg.norm(bstar.T[i])
    Mi = r[i, i + 1:].dot(a[i + 1:])

    return np.array((-Mi - Ai, -Mi + Ai))


def search_smallest_vector(basis: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Finding the smallest vector, conditional on the coefficients after i being fixed
    def sub_search(i: int, a: np.ndarray, b: np.ndarray, bstar: np.ndarray, r: np.ndarray, A: float
                   ) -> tuple[float | None, np.ndarray]:
        bounds = search_bounds(i, a, bstar, r, A)
        shortest_vectors: list[tuple[float, np.ndarray]] = []

        current_coefficient = np.ceil(bounds[0])
        while current_coefficient < bounds[1]:
            next_a = np.copy(a)
            next_a[i] = current_coefficient
            if i == 0:
                if np.any(next_a != 0):
                    shortest_vectors.append((np.linalg.norm(b.dot(next_a)), next_a))
                current_coefficient += 1
                continue
            length, full_a = sub_search(i-1, next_a, b, bstar, r, A)
            if length is not None and length != 0:
                shortest_vectors.append((length, full_a))
            current_coefficient += 1
        if shortest_vectors:
            return min(shortest_vectors, key=lambda x: x[0])
        else:
            return None, np.array([])

    # bstar is orthogonal and r is upper-triangular
    bstar, r = gram_schmidt_basis(basis)
    base_A = min([np.linalg.norm(b) for b in basis.T])
    a = np.zeros(basis.shape[1])

    shortest_length, shortest_coefficients = sub_search(basis.shape[0]-1, a, basis, bstar, r, base_A)
    return basis.dot(shortest_coefficients), shortest_coefficients

# basis = np.array([[8, 0, 1],
#                   [8, 5, 4],
#                   [3, 2, 0]])
# print(search_smallest_vector(basis))
