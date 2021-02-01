import pathlib
import components as components


BASEDIR = pathlib.Path(__file__).parents[0]

RECIPES_JSON_PATH = BASEDIR / "recipes.json"
COMPONENTS_JSON_PATH = BASEDIR / "components.json"

INSTALLED = \
    {
        "Meat": components.component.Meat,
        "Dairy": components.component.Dairy,
        "Vegetable": components.component.Vegetable,
        "Flour": components.component.Flour,
        "Fruit": components.component.Fruit,
        "Other": components.component.Other,
        "Custom": components.component.Custom
    }