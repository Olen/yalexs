from enum import Enum

from august.device import Device, DeviceDetail


class Lock(Device):
    def __init__(self, device_id, data):
        super().__init__(
            device_id,
            data["LockName"],
            data["HouseID"],
        )

    def __repr__(self):
        return "Lock(id={}, name={}, house_id={})".format(
            self.device_id,
            self.device_name,
            self.house_id)


class LockDetail(DeviceDetail):
    def __init__(self, data):
        super().__init__(
            data["LockID"],
            data["LockName"],
            data["HouseID"],
            data["SerialNumber"],
            data["currentFirmwareVersion"])

        self._battery_level = int(100 * data["battery"])

    @property
    def battery_level(self):
        return self._battery_level


class LockStatus(Enum):
    LOCKED = "kAugLockState_Locked"
    UNLOCKED = "kAugLockState_Unlocked"
    LOCKED_ALIAS = "locked"
    UNLOCKED_ALIAS = "unlocked"
