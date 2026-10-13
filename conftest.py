import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "test bun"
    bun.get_price.return_value = 150.0
    return bun

@pytest.fixture
def mock_ingredient():
    ing = Mock()
    ing.get_type.return_value = "SAUCE"
    ing.get_name.return_value = "hot sauce"
    ing.get_price.return_value = 100.0
    return ing

@pytest.fixture
def burger_with_mocks(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger, mock_bun, mock_ingredient
