from unittest.mock import Mock

import pytest
from praktikum.bun import Bun
from data import BUN_PRICE, BUN_NAME, INGREDIENT_NAME, INGREDIENT_PRICE, INGREDIENT_TYPE
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun():
    bun = Bun(price=BUN_PRICE, name=BUN_NAME)
    return bun



@pytest.fixture
def ingredient():
    ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE, price=INGREDIENT_PRICE, name=INGREDIENT_NAME)
    return ingredient


@pytest.fixture
def database():
    database = Database()
    return database


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = BUN_NAME
    mock_bun.price = 100
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.name = INGREDIENT_NAME
    mock_ingredient.type = INGREDIENT_TYPE
    return mock_ingredient


@pytest.fixture
def mock_ingredient_2():
    mock_ingredient_2 = Mock()
    mock_ingredient_2.name = 'INGREDIENT_NAME'
    mock_ingredient_2.type = 'INGREDIENT_TYPE'
    return mock_ingredient_2


@pytest.fixture
def mock_ingredient_3():
    mock_ingredient_3 = Mock()
    mock_ingredient_3.name = 'name'
    mock_ingredient_3.type = 'type'
    return mock_ingredient_3
