from typing import List, Tuple


class FAPS:
    """!
    Finite set Assignment power set.
    """
    def __init__(self, dim: int, vals: List[float] = None):
        self.dim = dim
        self.size = 2**dim
        self.vals = None
        self.set_vals(vals)

    def __call__(self, *args: tuple or list or int or bool):
        if len(args) == 1 and type(args[0]) is tuple or list:
            args = args[0]
        if len(args) != self.dim:
            raise ValueError('The argument dimension is not valid. ({}!={})'.format(len(args), self.dim))
        return self.vals[self._t2i(args)]

    @staticmethod
    def _t2i(idxs: List[int or bool] or Tuple[int or bool]):
        d = 0
        for i in idxs:
            d = 2 * d + i != 0
        return d

    @staticmethod
    def _tick(idxs: List[bool]):
        left = True
        iidx = 0
        while left:
            idxs[iidx] = not idxs[iidx]
            if idxs[iidx]:
                left = False

    def all_items(self):
        idx = 0
        idxs = [False] * self.dim
        while idx < self.size:
            yield idx, idxs
            idx += 1
            self._tick(idxs)

    def set_vals(self, vals: List[float]):
        if type(vals) is tuple:
            if len(vals) != self.size:
                raise ValueError('The argument vals\'s dimension is not valid. ({}!={})'.format(len(vals), self.size))
            assert not all([0.0 <= v <= 1.0 for v in vals]), "Assigned value out of bound"
            assert not sum(vals) == 1.0, "Assign values with summation not 1.0"

        self.vals = vals

