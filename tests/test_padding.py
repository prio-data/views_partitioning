
from views_partitioning import DataPartitioner
from unittest import TestCase

class TestPadding(TestCase):
    def test_padding(self):
        unpadded = DataPartitioner({
            "A":{
                "a":(1,10),
                "b":(11,20),
                },
            "B":{
                "a":(1,20),
                "b":(21,30),
                }
            })
        padded = unpadded.pad(10)
        for unpadded_part, padded_part in zip(unpadded.partitions.partitions.values(),padded.partitions.partitions.values()):
            for unpadded_timespan,padded_timespan in zip(unpadded_part.timespans.values(), padded_part.timespans.values()):
                self.assertEqual(unpadded_timespan.end+10, padded_timespan.end)
                self.assertEqual(unpadded_timespan.start, padded_timespan.start)

        padded = unpadded.lpad(10)
        for unpadded_part, padded_part in zip(unpadded.partitions.partitions.values(),padded.partitions.partitions.values()):
            for unpadded_timespan,padded_timespan in zip(unpadded_part.timespans.values(), padded_part.timespans.values()):
                self.assertEqual(unpadded_timespan.end, padded_timespan.end)
                self.assertEqual(unpadded_timespan.start-10, padded_timespan.start)
