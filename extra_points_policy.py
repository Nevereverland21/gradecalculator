class ExtraPointsPolicy:
    """
    Handles RF03 and RF04:
    - Count extra points from teachers.
    - Each True in the list gives +1 point.
    """

    def __init__(self, teachers_flags: list[bool]):
        self._validate_flags(teachers_flags)
        self.teachers_flags = teachers_flags

    def _validate_flags(self, flags):
        if not isinstance(flags, list):
            raise TypeError("Teachers flags must be a list")

        if not all(isinstance(f, bool) for f in flags):
            raise ValueError("Each teacher flag must be a boolean")

    def compute_extra_points(self) -> int:
        return sum(1 for f in self.teachers_flags if f)

