from attendance_policy import AttendancePolicy

def test_shouldReturnZeroWhenNoAttendance():
    policy = AttendancePolicy()
    assert policy.apply(15, False) == 0

def test_shouldReturnSameValueWhenAttendanceOk():
    policy = AttendancePolicy()
    assert policy.apply(15, True) == 15

