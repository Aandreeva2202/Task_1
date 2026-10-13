import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_ingredient_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150.5)
        assert ingredient.get_name() == "cutlet"

    def test_ingredient_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200.0)
        assert ingredient.get_price() == 200.0

    @pytest.mark.parametrize(
        "ingredient_type",
        [
            INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
        ]
    )
    def test_ingredient_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "hot sauce", 100.0)
        assert ingredient.get_type() == ingredient_type

    def test_ingredient_with_empty_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "", 0.0)
        assert ingredient.get_name() == ""

    def test_ingredient_with_zero_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "free item", 0.0)
        assert ingredient.get_price() == 0.0
