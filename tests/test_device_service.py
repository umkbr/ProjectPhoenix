import pytest

from phoenix.core.exceptions import DeviceNotFoundError
from phoenix.services.device_service import DeviceService


def test_service_created():
    service = DeviceService()
    assert service is not None


def test_read_without_device(monkeypatch):
    service = DeviceService()

    monkeypatch.setattr(service.adb, "devices", lambda: [])

    with pytest.raises(DeviceNotFoundError):
        service.read()