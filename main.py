from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


class Recipe(Widget):
    pass

class RecipeApp(App):
    def build(self):
        sm = ScreenManager()
        Builder.load_file('styles/backgrounds.kv')
        main_screen = MainScreen(name='main')
        recipe_widget = Recipe()
        main_screen.add_widget(recipe_widget)
        sm.add_widget(main_screen)
        return sm

class MainScreen(Screen):
    pass


if __name__ == '__main__':
    RecipeApp().run()