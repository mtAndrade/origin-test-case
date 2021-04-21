from risk_profiler.insurance.rules import InRange, LessThan, GreaterThan, OneOf, NotExists
import unittest

class ConditionsTestCase(unittest.TestCase):
    def test_in_range_condition(self):

        with self.subTest("When boundaries range inclusive"):
            in_range_10 = InRange(0,10)
            self.assertTrue(in_range_10.check(4))
            self.assertTrue(in_range_10.check(0))
            self.assertTrue(in_range_10.check(10))
            self.assertFalse(in_range_10.check(11))
            self.assertFalse(in_range_10.check(-1))
        
        with self.subTest("When range no lower boundarie"):
            in_range_lower = InRange(max=10)
            self.assertTrue(in_range_lower.check(1))
            self.assertTrue(in_range_lower.check(-1))
            self.assertTrue(in_range_lower.check(-100))
            self.assertFalse(in_range_lower.check(11))
        
        with self.subTest("When range no upper boundarie"):
            in_range_upper = InRange(min=10)
            self.assertTrue(in_range_upper.check(10))
            self.assertTrue(in_range_upper.check(100))
            self.assertFalse(in_range_upper.check(9))

        with self.subTest("When range non inclusive boundaries"):
            not_min_inclusive = InRange(min=10, max=15, min_inclusive=False)
            self.assertTrue(not_min_inclusive.check(11))
            self.assertFalse(not_min_inclusive.check(10))
            
            not_max_inclusive = InRange(min=10, max=15, max_inclusive=False)
            self.assertTrue(not_max_inclusive.check(10))
            self.assertFalse(not_max_inclusive.check(15))


    def test_less_than_condition(self):
        less_than_5 = LessThan(5)
        self.assertTrue(less_than_5.check(4))
        self.assertFalse(less_than_5.check(5))
        self.assertFalse(less_than_5.check(6))

    def test_greater_than_condition(self):
        greater_than_5 = GreaterThan(5)
        self.assertFalse(greater_than_5.check(4))
        self.assertFalse(greater_than_5.check(5))
        self.assertTrue(greater_than_5.check(6))

    def test_one_of_condition(self):
        with self.subTest("When one of strings"):
            one_of_strings = OneOf(["hello", "world"])
            self.assertTrue(one_of_strings.check("hello"))
            self.assertTrue(one_of_strings.check("world"))
            self.assertFalse(one_of_strings.check("goodbye"))
            self.assertFalse(one_of_strings.check(1))
        
        with self.subTest("When one of mixed types"):
            one_of_mixed = OneOf(["hello", 2, "world"])
            self.assertTrue(one_of_mixed.check("hello"))
            self.assertTrue(one_of_mixed.check(2))
            self.assertFalse(one_of_mixed.check("2"))
            self.assertFalse(one_of_mixed.check("goodbye"))
            self.assertFalse(one_of_mixed.check(1))

    def test_not_exists_condition(self):
        not_exists = NotExists()
        none_variable = None
        variable = dict()
        self.assertTrue(not_exists.check(none_variable))
        self.assertFalse(not_exists.check(variable))