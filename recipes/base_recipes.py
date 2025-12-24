from abc import ABC, abstractmethod
from copy import deepcopy


class RecipeBase(ABC):

    def __init__(self, name=None, **kwargs):
        self.base_ingredients = {}
        self.base_ingredients_list = []
        self.ingredients_dict = {}
        self.current_ingredients = {}
        self.ingredients = {}
        self.id = ''
        self.name = ''

    @abstractmethod
    def get_base_ingredients(self):
        return self.base_ingredients

    def recalculate_ingredients(self, **kwargs):
        '''перерасчёт всех ингредиентов относительно изменения одного из них'''

        if len(kwargs) != 1:
            raise ValueError('recalculate_ingredients принимает только 1 аргумент')
        ingredient, mass = next(iter(kwargs.items()))
        if mass == '':
            return self.get_base_ingredients()
        elif mass.find('.') != -1:
            mass = float(mass)
        else:
            mass = int(mass)

        my_list = deepcopy(self.ingredients_list)  #копия ингредиентов, с удалённым перерасчётным
        my_list.remove(ingredient)
        for i in my_list:

            i_add = round((self.base_ingredients[i] * mass) / self.base_ingredients[ingredient], 1)
            self.ingredients.update({i: i_add})
        self.ingredients.update(kwargs)
        return self