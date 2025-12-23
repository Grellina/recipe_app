from recipes import meringue_roll
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.button import Button

class RecipeScreen(Screen):
    label_text = StringProperty('')
    recipe = ObjectProperty(None)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.meringue_roll = meringue_roll.MeringueRoll(**kwargs)


    def recalculate(self, **kwargs):
        result = self.meringue_roll.recalculate_ingredients(**kwargs)
        if self.label_text:
            self.label_text.text = str(result)
            return result

    def on_recipe(self, *_):
        self.build_actions()

    def build_actions(self):
        '''Генерация кнопок ингредиентов'''
        box = self.ids.actions_box
        box.clear_widgets()

        for name, ingredient in self.recipe.ingredients_dict.items():
            btn = Button(text=self.recipe.ingredients_dict[name])
            btn.bind(on_release=lambda _, ingredient=name : self.run_action('recalculate_ingredients', ingredient))   #n - ингредиент
            box.add_widget(btn)

    def run_action(self, action, ingredient):
        value = self.ids.factor.text
        method = getattr(self.recipe, action)
        result = method(**{ingredient: value})
        self.ids.result.text = str(result)
        return result

