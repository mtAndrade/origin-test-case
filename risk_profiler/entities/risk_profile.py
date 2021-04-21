from risk_profiler.entities.enums import ScoreLabel

class RiskProfile:

    auto: int
    disability: int
    home: int
    life: int

    def __init__(self, auto_score=None, disability_score=None, home_score=None, life_score=None):
        self.auto = auto_score
        self.disability = disability_score
        self.home = home_score
        self.life = life_score        

    @staticmethod
    def get_readable_status(score):
        if score is None:
            return ScoreLabel.ineligible.value
        if score >= 3:
            return ScoreLabel.responsible.value            
        if score >= 1:
            return ScoreLabel.regular.value
        return ScoreLabel.economic.value

    def to_dict(self):
        return dict(
            auto=self.get_readable_status(self.auto),
            disability=self.get_readable_status(self.disability),
            home=self.get_readable_status(self.home),
            life=self.get_readable_status(self.life)
        )