import models
import settings


class MealplannerModel(models.recipe_model.RecipeModel,
                       models.components_model.ComponentModel,
                       models.inventory_model.InventoryModel):

    def __init__(self):
        models.recipe_model.RecipeModel.__init__(self, settings.RECIPE_JSON_PATH)
        models.components_model.ComponentModel.__init__(self, settings.INGREDIENTS_JSON_PATH)
        models.inventory_model.InventoryModel.__init__(self, settings.INVENTORY_JSON_PATH)
