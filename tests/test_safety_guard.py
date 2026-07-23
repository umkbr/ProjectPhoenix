from phoenix.safety.safety_guard import SafetyGuard


def test_battery_ok():

    guard = SafetyGuard()

    guard.battery_level = lambda: 85

    assert guard.battery_ok()


def test_battery_low():

    guard = SafetyGuard()

    guard.battery_level = lambda: 10

    assert not guard.battery_ok()