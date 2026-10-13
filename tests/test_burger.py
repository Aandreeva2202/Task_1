from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_assigns_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient_appends_to_list(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[-1] is mock_ingredient

    def test_remove_ingredient_decreases_list_length(self, burger_with_mocks):
        burger, _, mock_ingredient = burger_with_mocks
        initial_len = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == initial_len - 1

    def test_move_ingredient_changes_order(self, burger_with_mocks, mock_ingredient):
        # Добавляем второй ингредиент, чтобы было что двигать
        burger, mock_bun, _ = burger_with_mocks
        second_ing = Mock()
        second_ing.get_type.return_value = "FILLING"
        second_ing.get_name.return_value = "cutlet"
        second_ing.get_price.return_value = 120.0
        burger.add_ingredient(second_ing)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] is second_ing

    def test_get_price_calculates_correctly(self, burger_with_mocks, mock_bun, mock_ingredient):
        burger, _, _ = burger_with_mocks
        expected = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        assert burger.get_price() == expected

    def test_get_receipt(self, burger_with_mocks):
        burger, _, _ = burger_with_mocks
        expected = (
            "(==== test bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== test bun ====)\n\n"
            "Price: 400.0"
        )
        assert burger.get_receipt() == expected
