from evaluation import Evaluation

class EvaluationList:
    MAX_EVALUATIONS = 10

    def __init__(self, evaluations: list[Evaluation]):
        self._validate_list(evaluations)
        self.evaluations = evaluations

    def _validate_list(self, evaluations):
        if not evaluations:
            raise ValueError("Evaluations list cannot be empty")

        if len(evaluations) > self.MAX_EVALUATIONS:
            raise ValueError(f"Maximum allowed evaluations is {self.MAX_EVALUATIONS}")

        if not all(isinstance(e, Evaluation) for e in evaluations):
            raise TypeError("All items must be Evaluation objects")

        total_weight = sum(e.weight for e in evaluations)
        if abs(total_weight - 1.0) > 0.0001:  # margen muy pequeño
            raise ValueError("Total weight of evaluations must be exactly 1.0")

    def compute_base_grade(self) -> float:
        """
        Computes weighted sum → RF05 (parte del cálculo)
        This function must be deterministic (RNF03)
        """
        return sum(e.score * e.weight for e in self.evaluations)

