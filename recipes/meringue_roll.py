from copy import deepcopy
from .base_recipes import RecipeBase



class MeringueRoll(RecipeBase):
    def __init__(self, name=None,**kwargs):
        super().__init__(**kwargs)
        self.base_ingredients = {'egg_white': 190, 'sugar': 250, 'starch': 25}
        self.base_ingredients_list = ['egg_white', 'sugar', 'starch']
        self.current_ingredients = {**kwargs}
        self.ingredients = {}
        self.id = 'meringue_roll'


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
        if not self.ingredients:
            return self.base_ingredients
        else:
            return (f'необходимые ингредиенты: белки = {self.ingredients["egg_white"]} \n'
                    f'сахар = {self.ingredients["sugar"]} \n '
                    f'крахмал = {self.ingredients["starch"]} \n ')


    def get_base_ingredients(self):

        return (f'белки = {self.base_ingredients["egg_white"]} \n'
                f'сахар = {self.base_ingredients["sugar"]} \n'
                f'крахмал = {self.base_ingredients["starch"]} \n ')

