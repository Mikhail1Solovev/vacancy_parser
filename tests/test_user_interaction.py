import pytest
from unittest.mock import patch, MagicMock
from src.user_interaction import user_interaction


@pytest.fixture
def mock_hh_api():
    with patch('src.user_interaction.HH') as mock_hh:
        mock_instance = mock_hh.return_value
        mock_instance.load_vacancies = MagicMock()
        mock_instance.get_vacancies = MagicMock(return_value=[])
        yield mock_instance


@pytest.fixture
def mock_json_saver():
    with patch('src.user_interaction.JSONSaver') as mock_saver:
        mock_instance = mock_saver.return_value
        mock_instance.save = MagicMock()
        mock_instance.load = MagicMock(return_value=[])
        yield mock_instance


@patch('builtins.input', side_effect=['1', 'developer', '4'])
def test_user_interaction_search_vacancies(mock_input, mock_hh_api, mock_json_saver):
    user_interaction()
    mock_hh_api.load_vacancies.assert_called_once_with('developer')
    mock_hh_api.get_vacancies.assert_called_once()
    mock_json_saver.save.assert_called_once()


@patch('builtins.input', side_effect=['2', '5', '4'])
def test_user_interaction_get_top_vacancies(mock_input, mock_hh_api, mock_json_saver):
    mock_json_saver.load.return_value = [
        {"salary": {"from": 1000, "to": 2000}},
        {"salary": {"from": 1500, "to": 2500}},
        {"salary": {"from": 2000, "to": 3000}},
    ]
    with patch('src.user_interaction.pprint') as mock_pprint:
        user_interaction()
        mock_pprint.assert_called_once()


@patch('builtins.input', side_effect=['3', 'keyword', '4'])
def test_user_interaction_filter_vacancies(mock_input, mock_hh_api, mock_json_saver):
    mock_json_saver.load.return_value = [
        {"description": "This is a test keyword"},
        {"description": "Another test"},
    ]
    with patch('src.user_interaction.pprint') as mock_pprint:
        user_interaction()
        mock_pprint.assert_called_once()
