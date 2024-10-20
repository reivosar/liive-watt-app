from unittest.mock import MagicMock
from app.models.batch_execution_status import BatchExecutionStatus
from app.db.models.batch_execution_history import BatchExecutionHistory
from app.services.batch_execution_logger import BatchExecutionLogger
from app.repositories.batch_execution_history_repository import BatchExecutionHistoryRepository

class TestLogExecutionHistory:

    def setup_method(self):
        self.mock_repository = MagicMock(spec=BatchExecutionHistoryRepository)
        self.logger = BatchExecutionLogger(self.mock_repository)

    def test_log_execution_history_given_valid_data_when_logging_then_it_is_saved(self):
        # Given
        batch_id = 1
        status = BatchExecutionStatus.running
        message = "Test run"

        expected_history = BatchExecutionHistory(
            id=1, batch_id=batch_id, status=status, message=message
        )
        self.mock_repository.log_execution_history.return_value = expected_history

        # When
        result = self.logger.log_execution_history(batch_id, status, message)

        # Then
        self.mock_repository.log_execution_history.assert_called_once_with(batch_id, status, message)
        assert result == expected_history

class TestUpdateExecutionHistory:

    def setup_method(self):
        self.mock_repository = MagicMock(spec=BatchExecutionHistoryRepository)
        self.logger = BatchExecutionLogger(self.mock_repository)

    def test_update_execution_history_given_existing_execution_id_when_updating_then_it_is_updated(self):
        # Given
        execution_id = 1
        status = BatchExecutionStatus.success
        message = "Test success"

        # When
        self.logger.update_execution_history(execution_id, status, message)

        # Then
        self.mock_repository.update_execution_history.assert_called_once_with(execution_id, status, message)

    def test_update_execution_history_given_nonexistent_execution_id_when_nothing_is_updated(self):
        # Given
        execution_id = 999
        status = BatchExecutionStatus.failed
        message = "Test failure"

        self.mock_repository.update_execution_history.return_value = None

        # When
        self.logger.update_execution_history(execution_id, status, message)

        # Then
        self.mock_repository.update_execution_history.assert_called_once_with(execution_id, status, message)
