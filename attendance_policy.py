class AttendancePolicy:
    """
    Handles the rule for RF02:
    If student does NOT meet minimum attendance -> final grade must be 0.
    """

    def apply(self, base_grade: float, has_min_attendance: bool) -> float:
        if not isinstance(has_min_attendance, bool):
            raise TypeError("Attendance flag must be boolean")

        if not has_min_attendance:
            return 0.0

        return base_grade

