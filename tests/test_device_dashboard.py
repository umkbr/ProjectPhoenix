from phoenix.dashboard.device_dashboard import DeviceDashboard


def test_dashboard():

    dashboard = DeviceDashboard()

    data = dashboard.load()

    assert isinstance(data, dict)