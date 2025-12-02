from kivy.app import App
from kivy.uix.widget import Widget


class Recipe(Widget):
    pass

class RecipeApp(App):
    def build(self):
        return Recipe()


if __name__ == '__main__':
    RecipeApp().run()