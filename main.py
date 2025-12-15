from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder
from abc import ABC, abstractmethod
from recipes import meringue_roll

print(Builder.files)

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.meringue_roll = meringue_roll.MeringueRoll(**kwargs)
    label_text = StringProperty('')
    recipe = ObjectProperty(None)




class RecipeBase(ABC):

    def __init__(self, name=None, *args, **kwargs):
        self.base_ingredients = {**kwargs}
        self.current_ingredients = {**kwargs}
        self.name = name








if __name__ == '__main__':
    RecipeApp().run()