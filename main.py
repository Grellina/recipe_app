from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder

from recipes import load_recipes
from screens.recipe_detail import RecipeScreen



Builder.load_file('screens/menu_screen.kv')
Builder.load_file('screens/recipe_screen.kv')
Builder.load_file('components/icon_button.kv')




class RecipeApp(App):
    def build(self):
        self.recipes = load_recipes()
        return self.build_screen_manager()

    def build_screen_manager(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(RecipeScreen(name='recipe_detail'))
        sm.transition = FadeTransition(duration=0.3)
        return sm


    def open_recipe(self, recipe_id):
        recipe_screen = self.root.get_screen('recipe_detail')
        recipe_screen.label_text = self.recipes[recipe_id].name
        recipe_screen.recipe = self.recipes[recipe_id]      #recipe - свойство экрана RecipeScreen
        self.root.current = 'recipe_detail'

class MenuScreen(Screen):
    pass



if __name__ == '__main__':
    RecipeApp().run()