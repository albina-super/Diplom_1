import pytest

from data import INGREDIENT_PRICE, INGREDIENT_TYPE, INGREDIENT_NAME, INGREDIENT_TYPE_1, INGREDIENT_TYPE_2
from praktikum.ingredient import Ingredient


class TestIngredient:


    def test_get_price_success(self, ingredient):
        assert ingredient.get_price() == INGREDIENT_PRICE


    def test_get_name_success(self, ingredient):
        assert ingredient.get_name() == INGREDIENT_NAME

    @pytest.parametrize(
        'ingredient_type',
    [
        INGREDIENT_TYPE,
        INGREDIENT_TYPE_1,
        INGREDIENT_TYPE_2
    ])
    def test_get_type_success(self, ingredient_type):
        ingredient = Ingredient(name=INGREDIENT_NAME, price=INGREDIENT_PRICE, ingredient_type=ingredient_type)
        assert ingredient.get_type() == INGREDIENT_TYPE