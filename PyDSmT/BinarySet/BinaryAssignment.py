class BAPS:
    """!
    Binary Assignment power set.

    * Notice that hyper power set == power set for binary assignmnets.
    (Since x intersect ~x = empty)
    """
    comb_rule = None

    def __init__(self, true: float, false: float, unknown: float):
        self.true = true
        self.false = false
        self.unknown = unknown

        self.check_valid()

    def __str__(self):
        return '({:.4f}, {:.4f}, {:.4f}, {:.4f})'.format(*self.vals)

    def __mul__(self, other) -> 'BAPS':
        if self.comb_rule is None:
            raise NotImplementedError('The combination rule is not defined.')
        return self.comb_rule(other)

    @classmethod
    def set_comb_rule(cls, comb_rule) -> None:
        cls.comb_rule = comb_rule

    @property
    def vals(self) -> tuple:
        return self.true, self.false, self.unknown, self.empty

    @property
    def empty(self) -> float:
        return 1 - self.true - self.false - self.unknown

    def check_valid(self):
        assert 0.0 <= self.true <= 1.0, 'Unvalid value true = {}'.format(self.true)
        assert 0.0 <= self.false <= 1.0, 'Unvalid value false = {}'.format(self.false)
        assert 0.0 <= self.unknown <= 1.0, 'Unvalid value unknown = {}'.format(self.unknown)
        assert self.true + self.false <= 1.0, \
            'Unvalid value true + false + unknown = {}'.format(self.true + self.false + self.unknown)


BA = BAPS
