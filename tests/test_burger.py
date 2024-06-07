import pytest
from praktikum.burger import Burger
from generators_data import *
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def mock_add_ingredients():
    class MockAddIngredients:
        def __init__(self):
            self.ingredients = ['meat', 'bun', 'sauce']
        
        def move_ingredient(self, old_index, new_index):
            ingredient = self.ingredients.pop(old_index)
            self.ingredients.insert(new_index, ingredient)
    
    return MockAddIngredients()

class TestBurger:
    def test_set_buns_correctly(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_correctly(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_correctly(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        index = burger.ingredients.index(mock_ingredient)
        burger.remove_ingredient(index)

        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient_to_new_index(self, mock_add_ingredients):
        ingredient = mock_add_ingredients.ingredients[0]
        mock_add_ingredients.move_ingredient(1, 0)

        assert mock_add_ingredients.ingredients[1] == ingredient

    def test_calculate_price_correctly(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)

        mock_bun.get_price.return_value = bun_price
        mock_ingredient.get_price.return_value = ingredient_price

        assert burger.get_price() == bun_price * 2 + ingredient_price

    def test_get_receipt_with_bun_name(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)

        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        assert bun_name in burger.get_receipt()

    def test_get_receipt_with_ingredient_name(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)

        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = ingredient_name
        mock_ingredient.get_price.return_value = ingredient_price

        receipt = f'(==== {bun_name} ====)\n' \
                           f'= sauce {ingredient_name} =\n' \
                           f'(==== {bun_name} ====)\n' \
                           f'\nPrice: {bun_price * 2 + ingredient_price}'

        assert burger.get_receipt() == receipt