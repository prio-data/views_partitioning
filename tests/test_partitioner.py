
import unittest
import numpy as np
import pandas as pd
from toolz.functoolz import curry, compose
from views_partitioning import data_partitioner, legacy

data_time = lambda d: d.index.get_level_values(0)
min_time, max_time = (curry(compose(fn, data_time)) for fn in (min,max))

class TestDataPartitioner(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame(np.zeros((128*32,3)),
                index = pd.MultiIndex.from_product((range(128),range(32))),
                columns = list("abc"))

    def test_manual_init(self):
        partitioner = data_partitioner.DataPartitioner({
                "evaluation":{"train":(10,20),"test":(21,40)},
                "prediction":{"train":(10,30),"predict":(31,40)},
            }, self.data)

        self.assertEqual(min_time(partitioner["evaluation","train"]), 10)
        self.assertEqual(max_time(partitioner["evaluation","train"]), 20)

        self.assertEqual(min_time(partitioner["prediction","predict"]), 31)
        self.assertEqual(max_time(partitioner["prediction","predict"]), 40)

    def test_legacy_import(self):
        partitioner = data_partitioner.DataPartitioner.from_legacy_periods([
                legacy.Period("A",10,20,21,30),
                legacy.Period("B",10,30,31,40),
                legacy.Period("C",10,40,41,50),
            ],
            self.data)

        self.assertEqual(min_time(partitioner["A","train"]), 10)
        self.assertEqual(max_time(partitioner["A","train"]), 20)

        self.assertEqual(min_time(partitioner["A","predict"]), 21)
        self.assertEqual(max_time(partitioner["A","predict"]), 30)

        self.assertEqual(min_time(partitioner["B","train"]), 10)
        self.assertEqual(max_time(partitioner["B","train"]), 30)

        self.assertEqual(min_time(partitioner["B","predict"]), 31)
        self.assertEqual(max_time(partitioner["B","predict"]), 40)

        self.assertEqual(min_time(partitioner["C","train"]), 10)
        self.assertEqual(max_time(partitioner["C","train"]), 40)

        self.assertEqual(min_time(partitioner["C","predict"]), 41)
        self.assertEqual(max_time(partitioner["C","predict"]), 50)
