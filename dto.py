class GradeResult:
    """
    Defines the output of the grade calculation.
    Contains base grade, attendance-modified grade,
    extra points, and final grade.
    """

    def __init__(self, base_grade: float, after_attendance: float, extra_points: int, final_grade: float):
        self.base_grade = base_grade
        self.after_attendance = after_attendance
        self.extra_points = extra_points
        self.final_grade = final_grade

    def __repr__(self):
        return (
            f"GradeResult(base={self.base_grade}, "
            f"after_attendance={self.after_attendance}, "
            f"extra={self.extra_points}, "
            f"final={self.final_grade})"
        )

