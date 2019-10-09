from PyDSmT.BinarySet.BAPSCRBasic import BA, conjunctive_rule
from PyDSmT.BinarySet.BAPSCRUtils import unwrapPairValues


# =============================================================================
# Weighted operator is general type of combination rule
# =============================================================================
class WeightedOperator:
    def __init__(self, weight_func):
        self.weight_func = weight_func
        self.true_weight = 0.0
        self.false_weight = 0.0

    @property
    def unknown_weight(self):
        return 1 - self.true_weight - self.false_weight

    def compute_weights(self, a: BA, b: BA):
        self.true_weight, self.false_weight = self.weight_func(a, b)

    def __call__(self, a: BA, b: BA):
        self.compute_weights(a, b)
        c = conjunctive_rule(a, b)
        se = c.empty
        t = c.true + self.true_weight * se
        f = c.false + self.false_weight * se
        u = c.unknown + self.unknown_weight * se
        return BA(t, f, u)


class ConstantWeight:
    def __init__(self, true_weight, false_weight):
        self.true_weight = true_weight
        self.false_weight = false_weight

    def __call__(self, *args, **kwargs):
        return self.true_weight, self.false_weight


# =============================================================================
# Re-implement the basic rules
# =============================================================================
def Dempsters_weights(a: BA, b: BA) -> tuple:
    c = conjunctive_rule(a, b)
    k = 1 - c.empty
    return c.true / k, c.false / k


Yagers_weights = ConstantWeight(0, 0)


# =============================================================================
# PCR1
# Notice that PCR1 == WAO for binary assignment
# =============================================================================
def PCR1_Weights(a: BA, b: BA) -> tuple:
    ts, fs, us, _ = unwrapPairValues(a, b)
    d = sum(ts) + sum(fs) + sum(us)
    return sum(ts) / d, sum(fs) / d


WAO = PCR1_WO = WeightedOperator(PCR1_Weights)


# =============================================================================
# PCR2
# =============================================================================
def PCR2_Weights(a: BA, b: BA) -> tuple:
    ts, fs, _, _ = unwrapPairValues(a, b)
    d = sum(ts) + sum(fs)
    return sum(ts) / d, sum(fs) / d


PCR2_WO = WeightedOperator(PCR1_Weights)
