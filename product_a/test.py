import random
import unittest
from time import sleep


class TestCase(unittest.TestCase):
    def test_very_long(self):
        sleep(60 * 10)
        self.assertTrue(sum(1, 1) == 2)

    def test_random_fail(self):
        if random.random() < 0.1:
            self.assertTrue(False)
