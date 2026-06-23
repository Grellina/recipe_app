from recipes.base_recipes import RecipeBase


class MochiFilling(RecipeBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = 'mochi_dough'
        self.name = 'Тесто для моти'
        self.base_ingredients = {'sticky rice flour': 88, 'starch': 5, 'powdered sugar': 35, 'juice': 100, 'water': 45, 'vegetable oil': 12}
        self.ingredients_list = ['sticky rice flour', 'starch', 'powdered sugar', 'juice', 'water', 'vegetable oil']
        self.ingredients_dict = {'sticky rice flour': 'клейкая рисовая мука', 'starch': 'кукурузный крахмал', 'powdered sugar':'сахарная пудра',
                                 'juice': 'сок', 'water': 'вода', 'vegetable oil': 'растительное масло'}
        self.current_ingredients = {**kwargs}
        self.ingredients = {}



    def get_base_ingredients(self):
        return (f'необходимые ингредиенты: клейкая рисовая мука = {self.base_ingredients["sticky rice flour"]} г. \n'
                f'кукурузный крахмал = {self.base_ingredients["starch"]} г. \n '
                f'сахарная пудра = {self.base_ingredients["powdered sugar"]} г. \n '
                f'сок = {self.base_ingredients["juice"]} г. \n '
                f'вода = {self.base_ingredients["water"]} г. \n '
                f'растительное масло = {self.base_ingredients["vegetable oil"]} г. \n'
                )


    def __str__(self):
        if not self.ingredients:
            return self.base_ingredients
        else:
            return (f'необходимые ингредиенты: клейкая рисовая мука = {self.ingredients["sticky rice flour"]} г. \n'
                    f'кукурузный крахмал = {self.ingredients["starch"]} г. \n '
                    f'сахарная пудра = {self.ingredients["powdered sugar"]} г. \n '
                    f'сок = {self.ingredients["juice"]} г. \n '
                    f'вода = {self.ingredients["water"]} г. \n '
                    f'растительное масло = {self.ingredients["vegetable oil"]} г. \n '
                    )