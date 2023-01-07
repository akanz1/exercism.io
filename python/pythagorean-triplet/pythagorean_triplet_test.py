import unittest

from pythagorean_triplet import triplets_with_sum

# Tests adapted from `problem-specifications//canonical-data.json`

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, "assertCountEqual"):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class PythagoreanTripletTest(unittest.TestCase):
    def test_triplets_whose_sum_is_12(self):
        self.assertCountEqual(triplets_with_sum(12), [[3, 4, 5]])

    def test_triplets_whose_sum_is_108(self):
        self.assertCountEqual(triplets_with_sum(108), [[27, 36, 45]])

    def test_triplets_whose_sum_is_1000(self):
        self.assertCountEqual(triplets_with_sum(1000), [[200, 375, 425]])

    def test_no_matching_triplets_for_1001(self):
        self.assertCountEqual(triplets_with_sum(1001), [])

    def test_returns_all_matching_triplets(self):
        self.assertCountEqual(triplets_with_sum(90), [[9, 40, 41], [15, 36, 39]])

    def test_several_matching_triplets(self):
        self.assertCountEqual(
            triplets_with_sum(840),
            [
                [40, 399, 401],
                [56, 390, 394],
                [105, 360, 375],
                [120, 350, 370],
                [140, 336, 364],
                [168, 315, 357],
                [210, 280, 350],
                [240, 252, 348],
            ],
        )

    def test_triplets_for_medium_number(self):
        self.assertCountEqual(
            triplets_with_sum(12000),
            [
                [3000, 4000, 5000],
                [2625, 4320, 5055],
                [2400, 4500, 5100],
                [2000, 4800, 5200],
                [750, 5600, 5650],
                [480, 5750, 5770],
            ],
        )


if __name__ == "__main__":
    unittest.main()
