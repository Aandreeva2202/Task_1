import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_database_available_buns_count(self):
        db = Database()
        assert len(db.available_buns()) == 3

    def test_database_has_white_bun(self):
        db = Database()
        names = []
        for b in db.available_buns():
            names.append(b.name)
        assert "white bun" in names

    def test_database_available_ingredients_count(self):
        db = Database()
        assert len(db.available_ingredients()) == 6

    def test_database_first_ingredient_is_sauce(self):
        db = Database()
        first = db.available_ingredients()[0]
        assert first.type == INGREDIENT_TYPE_SAUCE

    @pytest.mark.parametrize("expected_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_database_contains_ingredient_type(self, expected_type):
        db = Database()
        types = []
        for i in db.available_ingredients():
            types.append(i.type)
        assert expected_type in types
