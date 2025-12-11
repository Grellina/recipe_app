from copy import deepcopy

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder
from abc import ABC, abstractmethod

Builder.load_file('styles/main_screen.kv')
Builder.load_file('styles/recipe_screen.kv')
Builder.load_file('components/icon_button.kv')



class RecipeApp(App):
    def build(self):
        sm = ScreenManager()
        main_screen = MainScreen(name='main')
        recipe_screen = RecipeScreen(name='recipe')
        sm.add_widget(main_screen)
        sm.add_widget(recipe_screen)
        sm.current = 'main'
        sm.transition = FadeTransition(duration= 0.3)
        return sm

    def open_recipe(self, text):
        recipe_screen = self.root.get_screen('recipe')
        recipe_screen.label_text = text
        self.root.current = 'recipe'

class MainScreen(Screen):
    pass

class RecipeScreen(Screen):
    label_text = StringProperty('')


class RecipeBase(ABC):

    def __init__(self, name, *args, **kwargs):
        self.base_ingredients = {**kwargs}
        self.current_ingredients = {**kwargs}
        self.name = name




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
        return f'необходимые ингредиенты: {[[k, '=', '%.1f'%(v)] for key, value in self.ingredients.items()]}'


    def get_ingredients(self):

        pass



if __name__ == '__main__':
    RecipeApp().run()