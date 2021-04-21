import unittest
from risk_profiler.insurance.profiler import Profiler
from risk_profiler.entities.user import User
from risk_profiler.entities.vehicle import Vehicle
from risk_profiler.entities.house import House
from risk_profiler.entities.risk_profile import RiskProfile
from risk_profiler.entities import enums


class ProfilerTestCase(unittest.TestCase):

    def test_user(self):
        return User(
            age=35,
            dependents=2,
            house=House(ownership_status="owned"),
            income=0,
            marital_status="married",
            risk_questions=[0, 1, 0],
            vehicle=Vehicle(year=2018)
        )        

    def test_profiler_adder_subtractor(self):
        expectation = RiskProfile(auto_score=1, home_score=0, life_score=1)
        risk_profile = Profiler(user=self.test_user()).get_risk_profile()
        
        self.assertEqual(expectation.auto, risk_profile.auto)
        self.assertEqual(expectation.home, risk_profile.home)
        self.assertEqual(expectation.life, risk_profile.life)
        self.assertEqual(expectation.disability, risk_profile.disability)
