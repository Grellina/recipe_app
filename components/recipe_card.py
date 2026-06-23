from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

class RecipeCard(BoxLayout):
    image = StringProperty("")
    title = StringProperty("")