from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.db.models.batch_management import BatchManagement
from app.repositories.batch_management_repository import BatchManagementRepository

def test_get_active_batch_by_name_found():
    # Given
    mock_db = MagicMock(spec=Session)
    mock_batch = BatchManagement(id=1, batch_name='test_batch')
    mock_db.query().filter().one.return_value = mock_batch

    repository = BatchManagementRepository(mock_db)

    # When
    result = repository.get_active_batch_by_name('test_batch')

    # Then
    assert result == mock_batch
    mock_db.query().filter().one.assert_called_once()

def test_get_active_batch_by_name_not_found():
    # Given
    mock_db = MagicMock(spec=Session)
    mock_db.query().filter().one.side_effect = NoResultFound

    repository = BatchManagementRepository(mock_db)

    # When
    result = repository.get_active_batch_by_name('non_existent_batch')

    # Then
    assert result is None
    mock_db.query().filter().one.assert_called_once()
