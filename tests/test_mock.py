from unittest.mock import patch
import requests

BASE_URL = "http://host.docker.internal:3000"

# Mock test for health check endpoint
@patch('requests.get')
def test_healthcheck(mock_get):
    """Test the healthcheck endpoint with mocking."""
    # Simulate a successful response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"status": "ok"}

    response = requests.get(f"{BASE_URL}/healthcheck", headers={"accept": "application/json"})

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    mock_get.assert_called_once_with(f"{BASE_URL}/healthcheck", headers={"accept": "application/json"})

# Mock test for an API endpoint that returns an error
@patch('requests.get')
def test_healthcheck_failure(mock_get):
    """Test the healthcheck endpoint when the API fails."""
    # Simulate a failure response
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {"error": "Internal Server Error"}

    response = requests.get(f"{BASE_URL}/healthcheck", headers={"accept": "application/json"})

    assert response.status_code == 500
    assert response.json() == {"error": "Internal Server Error"}
    mock_get.assert_called_once_with(f"{BASE_URL}/healthcheck", headers={"accept": "application/json"})
