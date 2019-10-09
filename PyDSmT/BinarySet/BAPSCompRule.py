from .BinaryAssignment import BAPS

BA = BAPS


# =============================================================================
# Combination rules applied on binary assignments
# =============================================================================

# =============================================================================
# Utils
# =============================================================================
def unwrapValues(a: BA, b: BA) -> tuple:
    return a.true, a.false, a.unknown, a.empty, b.true, b.false, b.unknown, b.empty


def unwrapPairValues(a: BA, b: BA) -> tuple:
    return (a.true, b.true), (a.false, b.false), (a.unknown, b.unknown), (a.empty, b.empty)


def cross(n: tuple, m: tuple) -> float:
    return n[0] * m[1] + n[1] * m[0]


def norm(n: tuple) -> float:
    return n[0] * n[1]


# =============================================================================
# Basic rules
# =============================================================================
def conjunctive_rule(a: BA, b: BA) -> BA:
    ts, fs, us, _ = unwrapPairValues(a, b)
    t = cross(ts, us) + norm(ts)
    f = cross(fs, us) + norm(fs)
    u = norm(us)
    return BA(t, f, u)


def disjunctive_rule(a: BA, b: BA) -> BA:
    ts, fs, us, _ = unwrapPairValues(a, b)
    t = norm(ts)
    f = norm(fs)
    u = 1 - t - f
    return BA(t, f, u)


# =============================================================================
# Various rules
#
# Notice that:
# 1. Smet's rule is the only one assign mass on empty set.
# 2. In spite of fact 1, we shouldn't assume source assigment with
#    empty assignment 0
# 3. The Yager's rule and the Dubois Prade's rule are the same when
#    applied on binary assignment.
# =============================================================================


def Dempsters_rule(a: BA, b: BA) -> BA:
    c = conjunctive_rule(a, b)
    k = 1 - c.empty
    t = c.true / k
    f = c.false / k
    u = c.unknown / k
    return BA(t, f, u)


def Smets_rule(a: BA, b: BA) -> BA:
    return conjunctive_rule(a, b)


def Yagers_rule(a: BA, b: BA) -> BA:
    c = conjunctive_rule(a, b)
    t = c.true
    f = c.false
    u = c.unknown + c.empty
    return BA(t, f, u)


def Dubois_Prades_rule(a: BA, b: BA) -> BA:
    ts, fs, us, _ = unwrapPairValues(a, b)
    t = cross(ts, us) + norm(ts)
    f = cross(fs, us) + norm(fs)
    u = norm(us) + cross(ts, fs)
    return BA(t, f, u)


# =============================================================================
# Weighted operator rules (WO rules)
# =============================================================================


# =============================================================================
# Proportional Conflict Redistribution rules (PCR rules)
# =============================================================================

def PCR5_f1(n: float, m: float) -> float:
    return (n**2 * m) / (n + m)


def PCR5_f2(n: tuple, m: tuple) -> float:
    return PCR5_f1(n[0], m[1]) + PCR5_f1(n[1], m[0])


def PCR5(a: BA, b: BA) -> BA:
    ts, fs, us, es = unwrapPairValues(a, b)
    c = conjunctive_rule(a, b)
    t = c.true + PCR5_f2(ts, fs) + PCR5_f2(ts, es)
    f = c.false + PCR5_f2(fs, ts) + PCR5_f2(fs, es)
    u = c.unknown + PCR5_f2(us, es)
    return BA(t, f, u)

