from types import FunctionType


class BAPS:
    """!
    Binary Assignment power set.
    """
    def __init__(self, true: float, false: float, unknown: float, comb_rule: FunctionType = None):
        self.true = true
        self.false = false
        self.unknown = unknown
        self.comb_rule = comb_rule

        self.check_valid()

    def __str__(self):
        return '({:.4f}, {:.4f}, {:.4f})'.format(self.true, self.false, self.unknown)

    def __mul__(self, other) -> 'BAPS':
        if self.comb_rule is None:
            raise NotImplementedError('The combination rule is not defined.')
        return self.comb_rule(self, other)

    @property
    def empty(self):
        return 1 - self.true - self.false - self.unknown

    def check_valid(self):
        assert 0.0 <= self.true <= 1.0, 'Unvalid value true = {}'.format(self.true)
        assert 0.0 <= self.false <= 1.0, 'Unvalid value false = {}'.format(self.false)
        assert 0.0 <= self.unknown <= 1.0, 'Unvalid value unknown = {}'.format(self.unknown)
        assert self.true + self.false <= 1.0, \
            'Unvalid value true + false + unknown = {}'.format(self.true + self.false + self.unknown)


class BAHPS:
    """!
    Binary Assignment hyper power set.
    """
    def __init__(self, true: float, false: float, conflict: float):
        self.true = true
        self.false = false
        self.conflict = conflict
        self.check_valid()

    def __str__(self):
        return '({:.4f}, {:.4f})'.format(self.true, self.false)

    def __add__(self, other):
        o1, e1, o2, e2 = self.true, self.false, other.o, other.e
        k = 1 - o1 * e2 - o2 * e1
        o = (o1 * (1 - e2) + o2 * (1 - e1) - o1 * o2) / k
        e = ((1 - o2) * e1 + (1 - o1) * e2 - e1 * e2) / k
        return BAHPS(o, e)

    def check_valid(self):
        assert 0.0 <= self.true <= 1.0, 'Unvalid value true = {}'.format(self.true)
        assert 0.0 <= self.false <= 1.0, 'Unvalid value false = {}'.format(self.false)
        assert 0.0 <= self.conflict <= 1.0, 'Unvalid value conflict = {}'.format(self.conflict)
        assert self.true + self.false + self.conflict <= 1.0, \
            'Unvalid value true + false + conflict = {}'.format(self.true + self.false + self.conflict)
