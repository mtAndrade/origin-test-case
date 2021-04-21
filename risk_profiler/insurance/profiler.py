from risk_profiler.entities.user import User
from risk_profiler.entities.risk_profile import RiskProfile
from risk_profiler.entities.enums import HouseStatus, MaritalStatus
from risk_profiler.insurance.processor import ChainScoreRule
from risk_profiler.insurance.rules import InRange, LessThan, GreaterThan, OneOf, NotExists
from datetime import datetime


class Profiler:
    
    _user: User
    _home_score: int
    _life_score: int
    _disability_score: int
    _auto_score: int

    def __init__(self, user: User):
        self._user = user

        base_score = sum(self._user.risk_questions)

        self._process_auto_score(base_score)
        self._process_disability_score(base_score)
        self._process_home_score(base_score)
        self._process_life_score(base_score)
        
    def _process_home_score(self, base_score:int)->int:
        self._home_score = ChainScoreRule(score=base_score) \
            .when(self._user.house, NotExists()).disable() \
            .when(self._user.age, LessThan(min=30) ).subtract(2) \
            .when(self._user.age, InRange(min=30, max=40)).subtract(1) \
            .when(self._user.income, GreaterThan(min=200000)).subtract(1) \
            .when(self._user.house.ownership_status, OneOf(list(HouseStatus.mortgaged))).add(1) \
            .process()

    def _process_life_score(self, base_score:int)->int:
        self._life_score = ChainScoreRule(score=base_score) \
            .when(self._user.age, GreaterThan(min=60)).disable() \
            .when(self._user.age, LessThan(min=30) ).subtract(2) \
            .when(self._user.age, InRange(min=30, max=40)).subtract(1) \
            .when(self._user.income, GreaterThan(min=200000)).subtract(1) \
            .when(self._user.dependents, GreaterThan(min=0)).add(1) \
            .when(self._user.marital_status, OneOf(list(MaritalStatus.married))).add(1) \
            .process()

    def _process_disability_score(self, base_score:int)->int:
        self._disability_score = ChainScoreRule(score=base_score) \
            .when(self._user.income, LessThan(min=1)).disable() \
            .when(self._user.age, GreaterThan(min=60)).disable() \
            .when(self._user.age, LessThan(min=30) ).subtract(2) \
            .when(self._user.age, GreaterThan(min=60) ).subtract(2) \
            .when(self._user.age, InRange(min=30, max=40)).subtract(1) \
            .when(self._user.income, GreaterThan(min=200000)).subtract(1) \
            .when(self._user.house.ownership_status, OneOf(list(HouseStatus.mortgaged))).add(1) \
            .when(self._user.dependents, GreaterThan(min=0)).add(1) \
            .when(self._user.marital_status, OneOf(list(MaritalStatus.married))).subtract(1) \
            .process()

    def _process_auto_score(self, base_score:int)->int:
        vehicle_age = datetime.today().year - self._user.vehicle.year if self._user.vehicle else None

        self._auto_score = ChainScoreRule(score=base_score) \
            .when(self._user.vehicle, NotExists()).disable() \
            .when(self._user.age, LessThan(min=30) ).subtract(2) \
            .when(self._user.age, InRange(min=30, max=40)).subtract(1) \
            .when(vehicle_age, InRange(min=0, max=5)).add(1) \
            .process()
    
    def get_risk_profile(self)->RiskProfile:
        return RiskProfile(
            auto_score=self._auto_score,
            disability_score=self._disability_score,
            home_score=self._home_score,
            life_score=self._life_score
        )