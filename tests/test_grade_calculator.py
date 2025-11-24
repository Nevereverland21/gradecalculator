from evaluation import Evaluation
from evaluation_list import EvaluationList
from attendance_policy import AttendancePolicy
from extra_points_policy import ExtraPointsPolicy
from grade_calculator import GradeCalculator

def test_shouldComputeFinalGradeNormally():
    evals = EvaluationList([
        Evaluation(15, 0.5),
        Evaluation(17, 0.5)
    ])
    calc = GradeCalculator(AttendancePolicy(), ExtraPointsPolicy([True]))

    result = calc.calculate(evals, True)

    assert result.final_grade == 16 + 1  # 17

def test_shouldReturnZeroWhenNoAttendance():
    evals = EvaluationList([ Evaluation(18, 1.0) ])
    calc = GradeCalculator(AttendancePolicy(), ExtraPointsPolicy([True, True]))

    result = calc.calculate(evals, False)
    assert result.final_grade == 0

def test_shouldNotExceedMaxGradeTwenty():
    evals = EvaluationList([
        Evaluation(20, 0.7),
        Evaluation(20, 0.3),
    ])
    calc = GradeCalculator(AttendancePolicy(), ExtraPointsPolicy([True, True, True]))

    result = calc.calculate(evals, True)
    assert result.final_grade == 20

