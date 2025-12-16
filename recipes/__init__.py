import pkgutil
import importlib
from .base_recipes import RecipeBase


def load_recipes():
    recipes = {}

    for _, module_name, _ in pkgutil.iter_modules(__path__):
        if module_name == 'base_recipes':
            continue
        module = importlib.import_module(f'{__name__}.{module_name}')

        for attr in module.__dict__.values():
            if isinstance(attr, type) and issubclass(attr, RecipeBase) and attr is not RecipeBase:
                recipe = attr()
                recipes[recipe.id] = recipe
    return recipes