from .BinaryAssignment import BAPS

BA = BAPS
# =============================================================================
# Combination rules applied on binary assignments
#
# Notice that:
# 1. Smet's rule is the only one assign mass on empty set.
# 2. In spite of fact 1, we shouldn't assume source assigment with
#    empty assignment 0
# 3. The Yager's rule and the Dubois Prade's rule are the same when
#    applied on binary assignment.
# =============================================================================


def disjunctive_rule(a: BA, b: BA) -> BA:
    t1, f1, u1, t2, f2, u2 = a.true, a.false, a.unknown, b.true, b.false, b.unknown
    t = t1 * t2
    f = f1 * f2
    u = 1 - t - f
    return BA(t, f, u)


def Dempsters_rule(a: BA, b: BA) -> BA:
    t1, f1, u1, t2, f2, u2 = a.true, a.false, a.unknown, b.true, b.false, b.unknown
    k = 1 - t1 * f2 - t2 * f1 - a.empty - b.empty
    t = (u1 * t2 + t1 * u2 + t1 * t2) / k
    f = (u1 * f2 + f1 * u2 + f1 * f2) / k
    u = u1 * u2 / k
    return BA(t, f, u)


def Smets_rule(a: BA, b: BA) -> BA:
    t1, f1, u1, t2, f2, u2 = a.true, a.false, a.unknown, b.true, b.false, b.unknown
    t = u1 * t2 + t1 * u2 + t1 * t2
    f = u1 * f2 + f1 * u2 + f1 * f2
    u = u1 * u2
    return BA(t, f, u)


def Yagers_rule(a: BA, b: BA) -> BA:
    t1, f1, u1, t2, f2, u2 = a.true, a.false, a.unknown, b.true, b.false, b.unknown
    t = u1 * t2 + t1 * u2 + t1 * t2
    f = u1 * f2 + f1 * u2 + f1 * f2
    u = u1 * u2 + t1 * f2 + t2 * f1
    return BA(t, f, u)


def Dubois_Prades_rule(a: BA, b: BA) -> BA:
    t1, f1, u1, t2, f2, u2 = a.true, a.false, a.unknown, b.true, b.false, b.unknown
    t = u1 * t2 + t1 * u2 + t1 * t2
    f = u1 * f2 + f1 * u2 + f1 * f2
    u = u1 * u2 + t1 * f2 + t2 * f1
    return BA(t, f, u)

