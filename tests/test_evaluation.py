import pytest
from evaluation import Evaluation

def test_shouldCreateEvaluationWhenValidValues():
    ev = Evaluation(18, 0.5)
    assert ev.score == 18
    assert ev.weight == 0.5

def test_shouldRaiseErrorWhenScoreInvalid():
    with pytest.raises(ValueError):
        Evaluation(25, 0.5)

def test_shouldRaiseErrorWhenWeightInvalid():
    with pytest.raises(ValueError):
        Evaluation(15, 1.2)

