import numpy as np
import matplotlib.pyplot as plt

from unittest import TestCase
from tqdm import tqdm

from PyDSmT.BinarySet.BinaryAssignment import BAPS
from PyDSmT.BinarySet.BAPSCRUtils import get_sample_BAPS, err_BAPS
from PyDSmT.BinarySet.BAPSCRBasic import \
    Dempsters_rule, Smets_rule, Yagers_rule, Dubois_Prades_rule
from PyDSmT.BinarySet.BAPSCRPCR import \
    PCR1, PCR2, PCR3, PCR4, PCR5


class TestOperatorRules(TestCase):
    showGraph = False
    fp_eps = 1e-10
    mode = 0

    @staticmethod
    def util_random_sample():
        raise NotImplementedError('Test sample not implemented')

    def util_random_batch(self) -> np.ndarray:
        n = 1000
        errs = np.zeros((n, ))
        for idx in tqdm(range(n)):
            errs[idx] = self.util_random_sample()
        return errs

    def util_test_random_sample(self):
        errs = self.util_random_sample()
        self.assertLessEqual(errs, self.fp_eps)

    def util_test_random_batch(self):
        errs = self.util_random_batch()
        if self.showGraph:
            plt.plot(errs)
            plt.show()
        self.assertLessEqual(max(errs), self.fp_eps)

    def util_test(self):
        if self.mode == 0:
            self.util_test_random_batch()
        else:
            self.util_test_random_sample()

    def test_Dempster_rule(self):
        BAPS.set_comb_rule(Dempsters_rule)
        self.util_test()

    def test_Smets_rule(self):
        BAPS.set_comb_rule(Smets_rule)
        self.util_test()

    def test_Yagers_rule(self):
        BAPS.set_comb_rule(Yagers_rule)
        self.util_test()

    def test_Dubois_Prades_rule(self):
        BAPS.set_comb_rule(Dubois_Prades_rule)
        self.util_test()

    def test_PCR1(self):
        BAPS.set_comb_rule(PCR1)
        self.util_test()

    def test_PCR2(self):
        BAPS.set_comb_rule(PCR2)
        self.util_test()

    def test_PCR3(self):
        BAPS.set_comb_rule(PCR3)
        self.util_test()

    def test_PCR4(self):
        BAPS.set_comb_rule(PCR4)
        self.util_test()

    def test_PCR5(self):
        BAPS.set_comb_rule(PCR5)
        self.util_test()


class TestValid(TestOperatorRules):
    @staticmethod
    def util_random_sample() -> float:
        get_sample_BAPS() * get_sample_BAPS()
        return 0.0


class TestCommutative(TestOperatorRules):
    @staticmethod
    def util_random_sample() -> float:
        a, b = get_sample_BAPS(), get_sample_BAPS()
        return err_BAPS(a * b, b * a)


class TestAssocaitive(TestOperatorRules):
    @staticmethod
    def util_random_sample() -> float:
        a, b, c = get_sample_BAPS(), get_sample_BAPS(), get_sample_BAPS()
        return err_BAPS(a * (b * c), (a * b) * c)
