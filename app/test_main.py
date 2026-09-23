from unittest.mock import patch
from app.main import can_access_google_page


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=True)
def test_accessible(mock_url: str, mock_internet: None) -> None:
    assert can_access_google_page("https://google.com") == "Accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=True)
def test_no_internet(mock_url: str, mock_internet: None) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection", return_value=True)
@patch("app.main.valid_google_url", return_value=False)
def test_invalid_url(mock_url: str, mock_internet: None) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"


@patch("app.main.has_internet_connection", return_value=False)
@patch("app.main.valid_google_url", return_value=False)
def test_no_internet_and_invalid_url(
        mock_url: str,
        mock_internet: None
) -> None:
    assert can_access_google_page("https://google.com") == "Not accessible"
