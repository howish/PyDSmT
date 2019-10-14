import numpy as np
from PyDSmT.BinarySet.BinaryAssignment import BA


# =============================================================================
# Utils
# =============================================================================
def unwrapValues(a: BA, b: BA) -> tuple:
    return a.vals + b.vals


def unwrapPairValues(a: BA, b: BA) -> tuple:
    return (a.true, b.true), (a.false, b.false), (a.unknown, b.unknown), (a.empty, b.empty)


def cross(n: tuple, m: tuple) -> float:
    return n[0] * m[1] + n[1] * m[0]


def norm(n: tuple) -> float:
    return n[0] * n[1]


def get_sample_BAPS() -> BA:
    x, y, z = np.random.rand(3).tolist()
    if y + z > 1:
        y, z = 1.0 - y, 1.0 - z
    if x + z > 1:
        x, z = 1.0 - x, 1.0 - y - z
    if x + y + z > 1:
        x, y = 1.0 - z - x, 1.0 - z - y
    return BA(x, y, z)


def err_BAPS(a: BA, b: BA) -> float:
    return np.linalg.norm(np.asarray(a.vals) - np.asarray(b.vals))
