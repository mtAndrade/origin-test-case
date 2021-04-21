from aiohttp.test_utils import unittest_run_loop
from aiohttp import web
from tests.base import BaseTestCase

class RiskProfilerResourceContract(BaseTestCase):

    def _basic_user_data(self)->dict:
        return {
            "age": 35,
            "dependents": 2,
            "house": {"ownership_status": "owned"},
            "income": 0,
            "marital_status": "married",
            "risk_questions": [0, 1, 0],
            "vehicle": {"year": 2018}
        }

    @unittest_run_loop
    async def test_example(self):
        data = self._basic_user_data()
        resp = await self.client.post("/risk/profile", json=data)
        assert resp.status == 200

    @unittest_run_loop
    async def test_age(self):
        data = self._basic_user_data()

        with self.subTest("Age as a required param"):
            data.pop("age")
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["age"][0], "Missing data for required field.")

        with self.subTest("Age as a integer param"):
            data["age"] = "35"
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["age"][0], "Not a valid integer.")

        with self.subTest("Age as a non negative param"):
            data["age"] = -1
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["age"][0], "Must be greater than or equal to 0.")

    @unittest_run_loop
    async def test_dependent(self):
        data = self._basic_user_data()

        with self.subTest("Dependents as a required param"):
            data.pop("dependents")
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["dependents"][0], "Missing data for required field.")

        with self.subTest("Dependents as a integer param"):
            data["dependents"] = "35"
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["dependents"][0], "Not a valid integer.")

        with self.subTest("Dependents as a non negative param"):
            data["dependents"] = -1
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["dependents"][0], "Must be greater than or equal to 0.")

    @unittest_run_loop
    async def test_income(self):
        data = self._basic_user_data()

        with self.subTest("Income as a required param"):
            data.pop("income")
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["income"][0], "Missing data for required field.")

        with self.subTest("Income as a integer param"):
            data["income"] = "35"
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["income"][0], "Not a valid integer.")

        with self.subTest("Income as a non negative param"):
            data["income"] = -1
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["income"][0], "Must be greater than or equal to 0.")

    @unittest_run_loop
    async def test_house(self):
        data = self._basic_user_data()
        
        with self.subTest("Marital status as one of owned or mortgaged param"):
            data["house"]["ownership_status"] = "anything"
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["house"]["ownership_status"][0], "Must be one of: owned, mortgaged.")

        with self.subTest("House.ownership_status as required param"):
            data["house"].pop("ownership_status")
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["house"]["ownership_status"][0], "Missing data for required field.")
       
        with self.subTest("House as a required param"):
            data.pop("house")
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["house"][0], "Missing data for required field.")

    @unittest_run_loop
    async def test_vehicle(self):
        data = self._basic_user_data()
        
        with self.subTest("Vehicle.year as one of integer param"):
            data["vehicle"]["year"] = "anything"
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["vehicle"]["year"][0], "Not a valid integer.")

        with self.subTest("Vehicle.year as a non negative param"):
            data["age"] = -1
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["age"][0], "Must be greater than or equal to 0.")

        with self.subTest("Vehicle.year as required param"):
            data["vehicle"].pop("year")
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["vehicle"]["year"][0], "Missing data for required field.")
       
        with self.subTest("Vehicle as a required param"):
            data.pop("vehicle")
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["vehicle"][0], "Missing data for required field.")
        
    @unittest_run_loop
    async def test_marital_status(self):
        data = self._basic_user_data()
        
        with self.subTest("Marital status as one of married or single param"):
            data["marital_status"] = "anything"
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["marital_status"][0], "Must be one of: single, married.")

        with self.subTest("Marital status as string param"):
            data["marital_status"] = 1
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["marital_status"][0], "Not a valid string.")

        with self.subTest("Marital status as required param"):
            data.pop("marital_status")
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["marital_status"][0], "Missing data for required field.")

    @unittest_run_loop
    async def test_risk_questions(self):
        data = self._basic_user_data()
        
        with self.subTest("Risk questions as a list param"):
            data["risk_questions"] = "anything"
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["risk_questions"][0], "Not a valid list.")

        with self.subTest("Risk questions as list of integers param"):
            data["risk_questions"] = ["anything"]
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["risk_questions"]["0"][0], "Not a valid integer.")

        with self.subTest("Risk questions as list of boolean integers param"):
            data["risk_questions"] = [2]
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["risk_questions"]["0"][0], "Must be one of: 0, 1.")
        
        with self.subTest("Risk questions as list of 3 params"):
            data["risk_questions"] = [1,1,1,1]
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["risk_questions"][0], "Risk questions should be a list with 3 entries")
        
        with self.subTest("Risk questions as required param"):      
            data.pop("risk_questions")
            resp = await self.client.post("/risk/profile", json=data)
            message = await resp.json()
            self.assertEqual(resp.status, 422)
            self.assertEqual(message["json"]["risk_questions"][0], "Missing data for required field.")