import pytest
from unittest.mock import MagicMock
from app.models.batch_management_status import BatchManagementStatus
from app.db.models.batch_management import BatchManagement
from app.repositories.batch_management_repository import BatchManagementRepository
from app.services.batch_management_service import BatchManagementService

class TestBatchManagementService:

    def setup_method(self):
        self.mock_repository = MagicMock(spec=BatchManagementRepository)
        self.service = BatchManagementService(self.mock_repository)

    def test_get_active_batch_by_name_given_valid_batch_name_when_job_is_active_then_returns_job(self):
        # Given
        batch_name = "test_batch"
        active_job = BatchManagement(batch_name=batch_name, status=BatchManagementStatus.active)
        self.mock_repository.get_active_batch_by_name.return_value = active_job

        # When
        result = self.service.get_active_batch_by_name(batch_name)

        # Then
        self.mock_repository.get_active_batch_by_name.assert_called_once_with(batch_name)
        assert result == active_job

    def test_get_active_batch_by_name_given_invalid_batch_name_when_job_not_found_then_raises_value_error(self):
        # Given
        batch_name = "nonexistent_batch"
        self.mock_repository.get_active_batch_by_name.return_value = None

        # When / Then
        with pytest.raises(ValueError, match=f"Active batch with name '{batch_name}' not found."):
            self.service.get_active_batch_by_name(batch_name)

    def test_get_active_batch_by_name_given_inactive_batch_name_when_job_is_inactive_then_raises_value_error(self):
        # Given
        batch_name = "test_batch"
        inactive_job = BatchManagement(batch_name=batch_name, status=BatchManagementStatus.inactive)
        self.mock_repository.get_active_batch_by_name.return_value = inactive_job

        # When / Then
        with pytest.raises(ValueError, match=f"Job '{batch_name}' is not active."):
            self.service.get_active_batch_by_name(batch_name)
