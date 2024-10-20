from app.models.batch_management_status import BatchManagementStatus

def test_is_active():
    status = BatchManagementStatus.active
    assert status.is_active  
    assert not status.is_inactive

def test_is_inactive():
    status = BatchManagementStatus.inactive
    assert status.is_inactive
    assert not status.is_active

def test_enum_values():
    assert BatchManagementStatus.active.value == 'active'
    assert BatchManagementStatus.inactive.value == 'inactive'