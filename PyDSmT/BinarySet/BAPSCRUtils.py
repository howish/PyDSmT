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
