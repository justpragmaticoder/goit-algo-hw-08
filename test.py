import unittest
from main import get_minimum_cost_order


class Test(unittest.TestCase):
    def test_min_cost_on_small_array(self):
        network_cables = [1, 2, 4, 10]
        total_cost, order = get_minimum_cost_order(network_cables)

        self.assertEqual(total_cost, 27)
        self.assertEqual(order, [(1, 2), (3, 4), (7, 10)])

    def test_min_cost_on_long_array(self):
        network_cables = [1, 2, 4, 10, 5, 7, 19, 26, 91, 8, 12, 15, 18]
        total_cost, order = get_minimum_cost_order(network_cables)

        self.assertEqual(total_cost, 632)
        self.assertEqual(
            order,
            [
                (1, 2),
                (3, 4),
                (5, 7),
                (7, 8),
                (10, 12),
                (12, 15),
                (15, 18),
                (19, 22),
                (26, 27),
                (33, 41),
                (53, 74),
                (91, 127),
            ],
        )
