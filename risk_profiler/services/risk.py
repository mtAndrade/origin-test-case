from risk_profiler.entities.user import User
from risk_profiler.entities.risk_profile import RiskProfile
from risk_profiler.insurance.profiler import Profiler


class RiskService:

    @staticmethod
    def accertain_risk_profile(user: User):
        """Accertain risk profile from User"""
        risk_profile = Profiler(user).get_risk_profile()
        readable_profile = risk_profile.to_dict()
        return readable_profile