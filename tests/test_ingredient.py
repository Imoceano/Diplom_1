import pytest
from praktikum import ingredient_types
from praktikum.ingredient import Ingredient
from generators_data import generate_random_ingredient_name, generate_random_ingredient_price

@pytest.fixture(scope='function')
def ingredient_name():
    return generate_random_ingredient_name()

@pytest.fixture(scope='function')
def ingredient_price():
    return generate_random_ingredient_price()

class TestIngredient:
    @pytest.mark.parametrize(
        'ingredient_type',
        [
            ingredient_types.INGREDIENT_TYPE_SAUCE,
            ingredient_types.INGREDIENT_TYPE_FILLING
        ]
    )
    def test_ingredient_returns_correct_price(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize(
        'ingredient_type',
        [
            ingredient_types.INGREDIENT_TYPE_SAUCE,
            ingredient_types.INGREDIENT_TYPE_FILLING
        ]
    )
    def test_ingredient_returns_correct_name(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize(
        'ingredient_type',
        [
            ingredient_types.INGREDIENT_TYPE_SAUCE,
            ingredient_types.INGREDIENT_TYPE_FILLING
        ]
    )
    def test_ingredient_returns_correct_type(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_type() == ingredient_type