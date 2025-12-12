from main import RecipeBase
from copy import deepcopy


class MeringueRoll(RecipeBase):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.base_ingredients = {'egg_white': 190, 'sugar': 250, 'starch': 25}
        self.base_ingredients_list = ['egg_white', 'sugar', 'starch']
        self.current_ingredients = {**kwargs}
        self.ingredients = {}


    def recalculate_ingredients(self, **kwargs):
        '''перерасчёт всех ингредиентов относительно изменения одного из них'''
        if len(kwargs) != 1:
            raise ValueError('recalculate_ingredients принимает только 1 аргумент')
        ingredient, mass = next(iter(kwargs.items()))
        my_list = deepcopy(self.base_ingredients_list)  #копия ингредиентов, с удалённым перерасчётным
        my_list.remove(ingredient)
        for i in my_list:
            i_add = self.base_ingredients[i] * mass / self.base_ingredients[i]
            self.ingredients.update({i: i_add})
        self.ingredients.update(kwargs)


    def __str__(self):
        if not self.ingredients:
            return self.base_ingredients
        else:
            return f'необходимые ингредиенты: {[[key, '=', '%.1f'%(value)] for key, value in self.ingredients.items()]}'


    def get_ingredients(self):

        pass