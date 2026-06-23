from recipes.base_recipes import RecipeBase


class MochiFilling(RecipeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = 'mochi_filling'
        self.name = 'Начинка моти'
        self.base_ingredients = {'fruit_filling': 90, 'pectin_NH': 2, 'white_chocolate': 55, 'sugar': 15, 'milk': 45, 'cream_33': 175, 'gelatin': 8, 'water': 45, 'portions': 12}
        self.ingredients_list = ['fruit_filling', 'pectin_NH', 'white_chocolate', 'sugar', 'milk', 'cream_33', 'gelatin', 'water', 'portions']
        self.ingredients_dict = {'fruit_filling': 'фруктовая начинка', 'pectin_NH': 'пектин NH', 'white_chocolate': 'белый шоколад', 'sugar' :'сахар', 'milk': 'молоко',
                                  'cream_33': 'сливки 33 %', 'gelatin': 'желатин', 'water': 'вода', 'portions': 'кол-во порций'}
        self.current_ingredients = {**kwargs}
        self.ingredients = {}



    def __str__(self):
        if not self.ingredients:
            return self.base_ingredients
        else:
            return (f'необходимые ингредиенты: фруктовая начинка = {self.ingredients["fruit_filling"]} г. \n'
                    f'пектин NH = {self.ingredients["pectin_NH"]} г. \n '
                    f'белый шоколад = {self.ingredients["white_chocolate"]} г. \n '
                    f'сахар = {self.ingredients["sugar"]} г. \n '
                    f'молоко = {self.ingredients["milk"]} г. \n '
                    f'сливки 33 % = {self.ingredients["cream_33"]} г. \n '
                    f'желатин = {self.ingredients["gelatin"]} г. \n '
                    f'вода = {self.ingredients["water"]} г. \n '
                    f'кол-во порций = {self.ingredients["portions"]} \n ')


    def get_base_ingredients(self):

        return (f'фруктовая начинка = {self.base_ingredients["fruit_filling"]} г. \n'
                f'пектин NH = {self.base_ingredients["pectin_NH"]} г. \n'
                f'белый шоколад = {self.base_ingredients["white_chocolate"]} г. \n '
                f'сахар = {self.base_ingredients["sugar"]} г. \n'
                f'молоко = {self.base_ingredients["milk"]} г. \n '
                f'сливки 33% = {self.base_ingredients["cream_33"]} г. \n '
                f'желатин = {self.base_ingredients["gelatin"]} г. \n '
                f'вода = {self.base_ingredients["water"]} г. \n '
                f'кол-во порций = {self.base_ingredients["portions"]} \n ')