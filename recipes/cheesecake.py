from .base_recipes import RecipeBase
from copy import deepcopy

class Cheesecake(RecipeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id ='cheesecake'
        self.name = 'Чизкейк'
        self.base_ingredients = {'cookies': 300,'butter': 100, 'white_cheese': 600, 'sugar': 150, 'eggs': 3, 'cream': 200}
        self.base_ingredients_list = ['cookies', 'butter', 'white_cheese', 'sugar', 'eggs', 'cream']
        self.current_ingredients = {**kwargs}
        self.ingredients = {}

    def get_base_ingredients(self):
        return self.base_ingredients_list

    def recalculate_ingredients(self, **kwargs):
        '''перерасчёт всех ингредиентов относительно изменения одного из них'''
        if len(kwargs) != 1:
            raise ValueError('recalculate_ingredients принимает только 1 аргумент')
        ingredient, mass = next(iter(kwargs.items()))
        mass = int(mass)
        my_list = deepcopy(self.base_ingredients_list)  #копия ингредиентов, с удалённым перерасчётным
        my_list.remove(ingredient)
        for i in my_list:

            i_add = round((self.base_ingredients[i] * mass) / self.base_ingredients[ingredient], 1)
            self.ingredients.update({i: i_add})
        self.ingredients.update(kwargs)
        return self

    def __str__(self):
        return self.ingredients