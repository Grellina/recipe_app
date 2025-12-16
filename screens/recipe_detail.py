from recipes import meringue_roll
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition


class RecipeScreen(Screen):
    label_text = StringProperty('')
    recipe_input = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.meringue_roll = meringue_roll.MeringueRoll(**kwargs)


    def recalculate(self, **kwargs):
        result = self.meringue_roll.recalculate_ingredients(**kwargs)
        if self.recipe_input:
            self.recipe_input.text = str(result)