from .base_recipes import RecipeBase

class Cheesecake(RecipeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id ='cheesecake'

    def get_base_ingredients(self):
        return self.base_ingredients_list
