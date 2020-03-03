from unittest import TestCase
from tqdm import tqdm

from PyDSmT.BinarySet.BAPSCRUtils import get_sample_BAPS


class TestUtils(TestCase):
    def test_sampling_BAPS(self):
        n = 1000
        for _ in tqdm(range(n)):
            get_sample_BAPS()
