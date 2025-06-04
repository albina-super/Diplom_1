import pytest

from data import receipt_data_names, receipt_data_prices, receipt_data_names_2, receipt_data_prices_2, \
    receipt_data_names_3, receipt_data_prices_3


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
        burger.remove_ingredient(index)
        assert len(burger.ingredients) == initial_len - 1 and removed not in burger.ingredients


    @pytest.mark.parametrize('names, prices, result', [
        (receipt_data_names, receipt_data_prices, '== Чёрная булка =='),
        (receipt_data_names_2, receipt_data_prices_2, '= сыры Сулугуни ='),
        (receipt_data_names_3, receipt_data_prices_3, 'Price: 330')
    ])

    def test_get_receipt_success(self, burger, mock_bun, mock_ingredient, result, names, prices):

        mock_bun.get_name.return_value = names[0]
        mock_bun.get_price.return_value = prices[0]
        mock_ingredient.get_name.return_value = names[1]
        mock_ingredient.get_price.return_value = prices[1]
        mock_ingredient.get_type.return_value = names[2]
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()

        assert result in receipt




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


    @pytest.mark.parametrize(
        ('index', 'new_index'),
        [(0, 1), (1, 2)]
    )
    def test_move_ingredient_success(self, index, new_index, mock_ingredient, mock_ingredient_2, mock_ingredient_3, burger):
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.add_ingredient(mock_ingredient)
        ingredient_before_move = burger.ingredients[index]
        burger.move_ingredient(index, new_index)
        ingredient_after_move = burger.ingredients[new_index]

        assert ingredient_before_move == ingredient_after_move