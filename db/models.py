from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from db.base import Base


class Recipe(Base):
    __tablename__ = 'recipes'

    key = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    ingredients = relationship(
        'Ingredient',
        secondary='recipe_ingredients',
        back_populates='recipes',
    )
    steps = Column(Text)


    def __repr__(self):
        return f'<Recipe {self.title}'



class Ingredients(Base):
    __tablename__ = 'ingredients'
    key = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    recipes = relationship(
        'Recipe',
        secondary='recipe_ingredients',
        back_populates='ingredients',
    )


    def __repr__(self):
        return f'<Ingredient {self.name}'


class RecipeIngredients(Base):
    '''промежуточная таблица'''
    __tablename__ = 'recipe_ingredients'

    recipe_id = Column(Integer, ForeignKey('recipes.key'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.key'), primary_key=True)
    amount = Column(Float)
    unit = Column(String(50))