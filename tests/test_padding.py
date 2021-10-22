
from unittest import TestCase
from views_partitioning import DataPartitioner

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

    def test_trimming(self):
        untrimmed = DataPartitioner({"A":{"a":(1,10),"b":(11,20)},"B":{"a":(21,30),"b":(31,40)}})
        s_a,e_a = untrimmed.partitions.extent()
        s_b,e_b = untrimmed.ltrim(1).partitions.extent()
        self.assertEqual(s_a,s_b-1)
        self.assertEqual(e_a,e_b)

        s_c,e_c = untrimmed.trim(1).partitions.extent()
        self.assertEqual(s_a,s_c)
        self.assertEqual(e_a-1,e_c)
