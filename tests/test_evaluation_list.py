import pytest
from evaluation import Evaluation
from evaluation_list import EvaluationList

def test_shouldComputeBaseGradeCorrectly():
    lst = EvaluationList([
        Evaluation(10, 0.4),
        Evaluation(20, 0.6),
    ])
    assert lst.compute_base_grade() == 16

def test_shouldFailWhenMoreThanTenEvaluations():
    with pytest.raises(ValueError):
        EvaluationList([Evaluation(10, 0.1)] * 11)

def test_shouldFailWhenTotalWeightNotOne():
    with pytest.raises(ValueError):
        EvaluationList([
            Evaluation(10, 0.3),
            Evaluation(10, 0.3),
        ])

