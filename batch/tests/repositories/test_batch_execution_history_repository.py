from unittest.mock import MagicMock
from app.repositories.batch_execution_history_repository import BatchExecutionHistoryRepository
from app.db.models.batch_execution_history import BatchExecutionHistory
from app.models.batch_execution_status import BatchExecutionStatus
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

class TestLogExecutionHistory:
    
    def setup_method(self):
        self.db_session = MagicMock(spec=Session)
        self.repository = BatchExecutionHistoryRepository(self.db_session)
    
    def test_log_execution_history_given_valid_data_when_logging_execution_history_then_it_is_saved(self, mocker):
        # Given
        batch_id = 1
        status = BatchExecutionStatus.running
        message = "Test run"
        
        mock_add = mocker.patch.object(self.db_session, 'add')
        mock_commit = mocker.patch.object(self.db_session, 'commit')

        # When
        result = self.repository.log_execution_history(batch_id, status, message)

        # Then
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

        assert isinstance(result, BatchExecutionHistory)
        assert result.batch_id == batch_id
        assert result.status == status
        assert result.message == message

class TestUpdateExecutionHistory:
    
    def setup_method(self):
        self.db_session = MagicMock(spec=Session)
        self.repository = BatchExecutionHistoryRepository(self.db_session)
    
    def test_update_execution_history_given_existing_execution_id_when_updating_execution_then_it_is_updated_correctly(self, mocker):
        # Given
        execution_id = 1
        status = BatchExecutionStatus.success
        message = "Test success"
        
        mock_execution_history = MagicMock(spec=BatchExecutionHistory)
        self.db_session.query().filter().first.return_value = mock_execution_history

        mock_commit = mocker.patch.object(self.db_session, 'commit')

        # When
        self.repository.update_execution_history(execution_id, status, message)

        # Then
        self.db_session.query().filter().first.assert_called_once() 
        mock_commit.assert_called_once()

        assert mock_execution_history.status == status
        assert mock_execution_history.message == message

    def test_update_execution_history_given_nonexistent_execution_id_when_updating_execution_then_nothing_is_updated(self, mocker):
        # Given
        execution_id = 999
        status = BatchExecutionStatus.failed
        message = "Test failure"

        self.db_session.query().filter().first.return_value = None

        mock_commit = mocker.patch.object(self.db_session, 'commit')

        # When
        self.repository.update_execution_history(execution_id, status, message)

        # Then
        self.db_session.query().filter().first.assert_called_once() 
        mock_commit.assert_not_called() 
