import pathlib
import components.ingredients as ingredients


# SETTING BASE DIRECTORY PATH
BASEDIR = pathlib.Path(__file__).parents[0]

# SETTING RECIPES FILE PATH FROM BASEDIR
RECIPE_JSON_PATH = BASEDIR / 'recipes.json'

# SETTING INVENTORY FILE PATH WITH FROM BASEDIR
INGREDIENTS_JSON_PATH = BASEDIR / 'ingredients.json'

# SETTING COMPONENTS FILE PATH FROM BASEDIR
INVENTORY_JSON_PATH = BASEDIR / 'inventory.json'

# INSTALLED/CREATED CLASSES FOR TYPES OF FOOD
INSTALLED = {
    "Meat":         ingredients.Meat,
    "Vegetable":    ingredients.Vegetable,
    "Dairy":        ingredients.Dairy,
    "Fruit":        ingredients.Fruit,
    "Flour":        ingredients.Flour,
    "Seasoning":    ingredients.Seasoning,
    "Other":        ingredients.Other
}