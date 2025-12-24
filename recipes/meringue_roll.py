from copy import deepcopy
from recipes.base_recipes import RecipeBase



class MeringueRoll(RecipeBase):

    actions = [
        {
            'id': 'recalculate_ingredients',
            'title': 'перерасчёт ингредиентов',
            'method': 'recalculate_ingredients',
        }
    ]

    def __init__(self, name=None,**kwargs):
        super().__init__(**kwargs)
        self.base_ingredients = {'egg_white': 190, 'sugar': 250, 'starch': 25}
        self.ingredients_list = ['egg_white', 'sugar', 'starch']
        self.ingredients_dict = {'egg_white':'белки', 'sugar':'сахар', 'starch': 'крахмал'}
        self.current_ingredients = {**kwargs}
        self.ingredients = {}
        self.id = 'meringue_roll'
        self.name = 'Меренговый рулет'



    def __str__(self):
        if not self.ingredients:
            return self.base_ingredients
        else:
            return (f'необходимые ингредиенты: белки = {self.ingredients["egg_white"]} г. \n'
                    f'сахар = {self.ingredients["sugar"]} г. \n '
                    f'крахмал = {self.ingredients["starch"]} г. \n ')


    def get_base_ingredients(self):

        return (f'белки = {self.base_ingredients["egg_white"]} г. \n'
                f'сахар = {self.base_ingredients["sugar"]} г. \n'
                f'крахмал = {self.base_ingredients["starch"]} г. \n ')

