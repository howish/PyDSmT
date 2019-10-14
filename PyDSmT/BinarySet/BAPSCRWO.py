from types import FunctionType
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
        self.unknown_weight = 0.0

    def compute_weights(self, a: BA, b: BA):
        weights = self.weight_func(a, b)
        if len(weights) == 2:
            self.true_weight, self.false_weight = weights
            self.unknown_weight = 1 - sum(weights)
        elif len(weights) == 3:
            self.true_weight, self.false_weight, self.unknown_weight = weights
        else:
            raise ValueError('Unknown weights length')

    def __call__(self, a: BA, b: BA):
        self.compute_weights(a, b)
        c = conjunctive_rule(a, b)
        se = c.empty
        t = c.true + self.true_weight * se
        f = c.false + self.false_weight * se
        u = c.unknown + self.unknown_weight * se
        return BA(t, f, u)


class ConstantWeight:
    def __init__(self, true_weight, false_weight, unknown_weight=None):
        self.true_weight = true_weight
        self.false_weight = false_weight
        self.unknown_weight = unknown_weight if unknown_weight is not None \
            else 1 - true_weight - false_weight

    def __call__(self, a: BA, b: BA) -> tuple:
        return self.true_weight, self.false_weight, self.unknown_weight


# =============================================================================
# Basic rules
# =============================================================================
def Dempsters_weights(a: BA, b: BA) -> tuple:
    c = conjunctive_rule(a, b)
    k = 1 - c.empty
    return c.true / k, c.false / k


Yagers_weights = ConstantWeight(0, 0)
Smets_weights = ConstantWeight(0, 0, 0)


# =============================================================================
# PCRs
# Notice that PCR1 == WAO for binary assignment
# =============================================================================
def PCR1_Weights(a: BA, b: BA) -> tuple:
    ts, fs, us, _ = unwrapPairValues(a, b)
    d = sum(ts) + sum(fs) + sum(us)
    return sum(ts) / d, sum(fs) / d


def PCR2_Weights(a: BA, b: BA) -> tuple:
    ts, fs, _, _ = unwrapPairValues(a, b)
    d = sum(ts) + sum(fs)
    return sum(ts) / d, sum(fs) / d


# =============================================================================
# Re-implement operators by WO
# =============================================================================
Dempsters_rule = WeightedOperator(Dempsters_weights)
Yagers_rule = WeightedOperator(Yagers_weights)
Smets_rule = WeightedOperator(Smets_weights)

PCR1_WO = WAO = WeightedOperator(PCR1_Weights)
PCR2_WO = WeightedOperator(PCR2_Weights)
