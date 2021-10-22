
import unittest
from views_schema import TimeSpan, Partitions
from views_partitioning import DataPartitioner

class TestViewsStuff(unittest.TestCase):
    """
    Tests the operations performed in the ViewsRun module
    """

    def test_pad_overlap_in_extent(self):
        dp = DataPartitioner(Partitions(partitions={"A":TimeSpan(start = 1, end = 100).to_partition({"a":.5, "b":.5})}))
        shifted = dp.shift_left(10)
        self.assertEqual(shifted.extent(),dp.extent())

        p = shifted.partitions.partitions["A"]

        self.assertFalse(p.has_overlap)
        self.assertEqual(p.timespans["a"].end, 40)
        self.assertEqual(p.timespans["b"].start, 41)

        shifted = dp.shift_right(10)
        self.assertEqual(shifted.extent(),dp.extent())

        p = shifted.partitions.partitions["A"]

        self.assertFalse(p.has_overlap)
        self.assertEqual(p.timespans["a"].end, 60)
        self.assertEqual(p.timespans["b"].start, 61)
