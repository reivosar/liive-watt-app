from enum import Enum

class BatchManagementStatus(Enum):
    active = 'active'
    inactive = 'inactive'

    @property
    def is_active(self):
        return self == BatchManagementStatus.active

    @property
    def is_inactive(self):
        return self == BatchManagementStatus.inactive