import pytest
from praktikum.bun import Bun
from data import BUN_PRICE, BUN_NAME, INGREDIENT_NAME, INGREDIENT_PRICE, INGREDIENT_TYPE
from praktikum.ingredient import Ingredient


@pytest.fixture(scope='session')
def bun():
    bun = Bun(price=BUN_PRICE, name=BUN_NAME)
    return bun



@pytest.fixture(scope='session')
def ingredient():
    ingredient = Ingredient(ingredient_type=INGREDIENT_TYPE, price=INGREDIENT_PRICE, name=INGREDIENT_NAME)
    return ingredient