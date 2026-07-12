class PhoenixError(Exception):
    """Base exception Project Phoenix."""


class DeviceNotFoundError(PhoenixError):
    """No Android device connected."""


class ADBNotFoundError(PhoenixError):
    """ADB executable not found."""