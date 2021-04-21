from .house import House
from .vehicle import Vehicle
from .enums import MaritalStatus
from typing import List

class User:
    age : int
    dependents : int
    house : House
    income : int
    marital_status : MaritalStatus 
    risk_questions : List[int]
    vehicle : Vehicle

    def __init__(self, age=None, dependents=None, income=None, marital_status=None, risk_questions=None, house=None, vehicle=None):
        self.age = age
        self.dependents = dependents
        self.house = house
        self.income = income
        self.marital_status = marital_status
        self.risk_questions = risk_questions
        self.vehicle = vehicle