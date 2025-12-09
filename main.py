from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.lang import Builder

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


if __name__ == '__main__':
    RecipeApp().run()