from unittest.mock import Mock

import pytest



class TestBurger:


    def test_set_buns_success(self, mock_bun, burger):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient_success(self, mock_ingredient, burger):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    @pytest.mark.parametrize('index', [0, 1])
    def test_remove_ingredient_success(self, burger, index, mock_ingredient, mock_ingredient_2, mock_ingredient_3):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        removed = burger.ingredients[index]
        initial_len = len(burger.ingredients)
        print(initial_len, 'len')
        burger.remove_ingredient(index)
        assert len(burger.ingredients) == initial_len - 1 and removed not in burger.ingredients

    def test_move_ingredient_success(self):
       pass

    @pytest.mark.parametrize(
        ('bun_price', 'ingredient_price', 'result'),
        [
            (100, 30, 230),
            (120, 12, 252)
        ]
    )
    def test_get_price_success(self, bun_price, ingredient_price, result, mock_bun, mock_ingredient, burger):
        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        sum_price = burger.get_price()
        assert sum_price == result


    def test_get_receipt_success(self):
        pass