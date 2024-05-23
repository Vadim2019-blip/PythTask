import typing as tp

import numpy as np


def nonzero_product(matrix: np.ndarray) -> tp.Optional[float]:
    """
    Compute product of nonzero diagonal elements of matrix
    If all diagonal elements are zeros, then return None
    :param matrix: array,
    :return: product value or None
    """
    data = matrix.diagonal()
    nonzero_elements = data[np.where(data != 0)]
    if len(nonzero_elements) == 0:
        return None
    product = np.prod(nonzero_elements)
    return product

