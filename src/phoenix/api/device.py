from phoenix.services.device_service import DeviceService

_service = DeviceService()


def get_device():
    return _service.read()