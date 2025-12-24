from .base_recipes import RecipeBase
from copy import deepcopy

class Cheesecake(RecipeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id ='cheesecake'
        self.name = 'Чизкейк'
        self.base_ingredients = {'cookies': 300,'butter': 100, 'white_cheese': 600, 'sugar': 150, 'eggs': 250, 'cream': 200}
        self.ingredients_list = ['cookies', 'butter', 'white_cheese', 'sugar', 'eggs', 'cream']
        self.ingredients_dict = {'cookies': 'печенье', 'butter': 'масло', 'white_cheese': 'сливочный сыр', 'sugar': 'сахар', 'eggs': 'яйца', 'cream': 'сливки'}
        self.current_ingredients = {**kwargs}
        self.ingredients = {}

    def get_base_ingredients(self):
        return (f'необходимые ингредиенты: печенье = {self.base_ingredients["cookies"]} г. \n'
                    f'масло = {self.base_ingredients["butter"]} г. \n '
                    f'сливочный сыр = {self.base_ingredients["white_cheese"]} г. \n '
                    f'сахар = {self.base_ingredients["sugar"]} г. \n '
                    f'яйца = {self.base_ingredients["eggs"]} г. \n '
                    f'сливки = {self.base_ingredients["cream"]} г. \n ')


    def __str__(self):
        if not self.ingredients:
            return self.base_ingredients
        else:
            return (f'необходимые ингредиенты: печенье = {self.ingredients["cookies"]} г. \n'
                    f'масло = {self.ingredients["butter"]} г. \n '
                    f'сливочный сыр = {self.ingredients["white_cheese"]} г. \n '
                    f'сахар = {self.ingredients["sugar"]} г. \n '
                    f'яйца = {self.ingredients["eggs"]} г. \n '
                    f'сливки = {self.ingredients["cream"]} г. \n ')