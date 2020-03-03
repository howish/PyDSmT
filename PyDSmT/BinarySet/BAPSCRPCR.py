from PyDSmT.BinarySet.BAPSCRBasic import BA, conjunctive_rule
from PyDSmT.BinarySet.BAPSCRUtils import unwrapPairValues, cross, norm


# =============================================================================
# Proportional Conflict Redistribution rules (PCR rules)
# =============================================================================
# PCR1
def PCR1(a: BA, b: BA) -> BA:
    ts, fs, us, _ = unwrapPairValues(a, b)
    c = conjunctive_rule(a, b)
    se = c.empty
    d = sum(ts) + sum(fs) + sum(us)
    t = c.true + sum(ts) / d * se
    f = c.false + sum(fs) / d * se
    u = c.unknown + sum(us) / d * se
    return BA(t, f, u)


# PCR2
def PCR2(a: BA, b: BA) -> BA:
    ts, fs, _, _ = unwrapPairValues(a, b)
    c = conjunctive_rule(a, b)
    se = c.empty
    d = sum(ts) + sum(fs)
    t = c.true + sum(ts) / d * se
    f = c.false + sum(fs) / d * se
    u = c.unknown
    return BA(t, f, u)


# PCR3
def PCR3_f1(n: tuple, m: tuple) -> float:
    return cross(n, m) / (sum(n) + sum(m))


def PCR3(a: BA, b: BA) -> BA:
    ts, fs, us, es = unwrapPairValues(a, b)
    c = conjunctive_rule(a, b)
    t = c.true + sum(ts) * (PCR3_f1(ts, fs) + PCR3_f1(ts, es))
    f = c.false + sum(fs) * (PCR3_f1(fs, ts) + PCR3_f1(fs, es))
    u = c.unknown + sum(us) * (PCR3_f1(us, es))
    return BA(t, f, u)  #TODO


# PCR4
def PCR4_f1(n: float, m: float) -> float:
    return 1 / (n + m)


def PCR4(a: BA, b: BA) -> BA:
    c = conjunctive_rule(a, b)
    st, sf, su, se = c.vals
    t = c.true * (1 + se * PCR4_f1(st, sf))
    f = c.false * (1 + se * PCR4_f1(sf, st))
    u = c.unknown
    return BA(t, f, u)


# PCR5
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
