import sys
import os
from recipes import meringue_roll

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_meringue_roll():
    roll = meringue_roll.MeringueRoll(egg_white=200)
    roll.recalculate_ingredients(egg_white=200)
    assert roll.ingredients == {'egg_white': 200, 'sugar': 263.2, 'starch': 26.3}
    return roll


