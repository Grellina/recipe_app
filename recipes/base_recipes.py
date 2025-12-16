from abc import ABC, abstractmethod



class RecipeBase(ABC):
    def __init__(self, name=None, **kwargs):
        self.base_ingredients = {}
        self.base_ingredients_list = []
        self.current_ingredients = {}
        self.ingredients = {}

    @abstractmethod
    def get_base_ingredients(self):
        return self.base_ingredients