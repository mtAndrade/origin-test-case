import unittest
from risk_profiler.entities.user import User
from risk_profiler.insurance.processor import ChainScoreRule
from risk_profiler.entities import enums
from risk_profiler.insurance.rules.base import Condition

class TrueFakeCondition(Condition):
    def check(self, value):
        return True

class FalseFakeCondition(Condition):
    def check(self, value):
        return False

class ChainScoreTestCase(unittest.TestCase): 

    def test_chain_adder_subtractor(self):
        true_condition = TrueFakeCondition()
        false_condition = FalseFakeCondition()

        with self.subTest("Chain when condition is true adds"):
            chain = ChainScoreRule()\
                    .when("something", true_condition).add(1) \
                    .when("something", true_condition).add(1)
            self.assertEqual(chain.process(), 2)
        
        with self.subTest("Chain when condition is false adds"):
            chain = ChainScoreRule()\
                    .when("something", false_condition).add(1) \
                    .when("something", false_condition).add(1)
            self.assertEqual(chain.process(), 0)
        
        with self.subTest("Chain when condition is true subtracts"):
            chain = ChainScoreRule()\
                    .when("something", true_condition).subtract(1) \
                    .when("something", true_condition).subtract(1)
            self.assertEqual(chain.process(), -2)
        
        with self.subTest("Chain when condition is false subtracts"):
            chain = ChainScoreRule()\
                    .when("something", false_condition).subtract(1) \
                    .when("something", false_condition).subtract(1)
            self.assertEqual(chain.process(), 0)

        with self.subTest("Chain when base value is diferent than zero false"):
            positive_chain = ChainScoreRule(score=5)\
                    .when("something", true_condition).add(1) \
                    .when("something", false_condition).add(1) 
            self.assertEqual(positive_chain.process(), 6)
    
    def test_disable_chain(self):
        true_condition = TrueFakeCondition()

        with self.subTest("When chain score is empty"):
            chain = ChainScoreRule().when("something", true_condition).disable()
            self.assertIsNone(chain.process())

        with self.subTest("When chain score is not empty"):
            chain = ChainScoreRule(5).when("something", true_condition).disable()
            self.assertIsNone(chain.process())

        with self.subTest("When chain has mutiple steps"):
            chain = ChainScoreRule()\
                .when("something", true_condition).add(1) \
                .when("something", true_condition).subtract(1)\
                .when("something", true_condition).disable()
            self.assertIsNone(chain.process())