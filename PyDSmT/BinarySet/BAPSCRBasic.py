from PyDSmT.BinarySet.BAPSCRUtils import unwrapPairValues, cross, norm
from PyDSmT.BinarySet.BinaryAssignment import BA


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
# Various named rules
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
