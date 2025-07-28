import pytest

from main import get_random_cat

def test_get_random_cat(mocker):
    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"id":"36v","url":"https://cdn2.thecatapi.com/images/36v.jpg","width":720,"height":540}]
    assert get_random_cat() == "https://cdn2.thecatapi.com/images/36v.jpg"

def test_get_random_cat_full(mocker):
    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"id":"36v","url":"https://cdn2.thecatapi.com/images/36v.jpg","width":720,"height":540}]
    assert get_random_cat(full=True) == {"id":"36v","url":"https://cdn2.thecatapi.com/images/36v.jpg","width":720,"height":540}

def test_get_random_cat_error(mocker):
    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.status_code = 404
    assert get_random_cat() == None

