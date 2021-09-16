
import unittest
from views_partitioning import legacy

class TestLegacyValidation(unittest.TestCase):
    def test_validation(self):
        cases = [
                (legacy.Period("",1,10,11,20), True),
                (legacy.Period("",-1,10,11,20), False),
                (legacy.Period("",10,1,11,20), False),
                (legacy.Period("",1,15,11,20), False),
                (legacy.Period("",1,15,11,20), False),
                (legacy.Period("",11,20,1,10), False),
            ]

        def test(case):
            period,outcome = case
            self.assertEqual(legacy.period_object_is_valid(period), outcome)

        for c in cases:
            test(c)
