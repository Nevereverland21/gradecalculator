from dto import GradeResult

class GradeCalculator:
    MAX_GRADE = 20.0

    def __init__(self, attendance_policy, extra_points_policy):
        self.attendance_policy = attendance_policy
        self.extra_points_policy = extra_points_policy

    def calculate(self, evaluation_list, has_min_attendance: bool) -> GradeResult:
        base = evaluation_list.compute_base_grade()

        # Apply attendance rule (RF02)
        after_attendance = self.attendance_policy.apply(base, has_min_attendance)

        # If attendance is NOT met → final grade must be 0 (RF02)
        if not has_min_attendance:
            return GradeResult(
                base_grade=base,
                after_attendance=0.0,
                extra_points=0,
                final_grade=0.0
            )

        # Attendance is OK → Apply extra points
        extra = self.extra_points_policy.compute_extra_points()

        final = after_attendance + extra
        final = min(final, self.MAX_GRADE)

        return GradeResult(
            base_grade=base,
            after_attendance=after_attendance,
            extra_points=extra,
            final_grade=final
        )

