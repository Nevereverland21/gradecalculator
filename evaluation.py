class Evaluation:
    def __init__(self, score: float, weight: float):
        self._validate_score(score)
        self._validate_weight(weight)

        self.score = score
        self.weight = weight

    @staticmethod
    def _validate_score(score):
        if not isinstance(score, (int, float)):
            raise TypeError("Score must be a number")
        if score < 0 or score > 20:
            raise ValueError("Score must be between 0 and 20")

    @staticmethod
    def _validate_weight(weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
        if weight <= 0 or weight > 1:
            raise ValueError("Weight must be between 0 and 1")

