"""
MAIN MODULE
"""
import controllers


def create_recipe():
    component_tool = controllers.component_selector.ComponentSelector()
    ingredient_tool = controllers.ingredient_selector.IngredientSelector()

    action = controllers.recipe_creator.RecipeCreator(component_tool, ingredient_tool)
    new_recipe_object = action.create()

    action.save_recipe_data(new_recipe_object)


def add_new_ingredient():
    action = controllers.ingredient_creator.CreateIngredient()
    inventory = controllers.inventory_manager.InventoryManager()

    new_ingredient_object = action.create_new()
    inventory.sort_ingredient(new_ingredient_object)

    # SAVE COMPONENT DATA
    action.save_component_data()

    # UPDATE / SAVE INVENTORY DATA
    inventory.save_inventory_data()


def inventory_manager():
    action = controllers.inventory_manager.InventoryManager()
    action.update_quantities()

    action.save_inventory_data()


def mealplanner():
    action = controllers.mealplanner.ShoppingList()
    shopping_cart = action.generate_shopping_list_ready()


class Config:
    mealplanner_menu = "Mealplanner"
    recipe_menu = "Recipes"
    new_ingredient_menu = "Add new ingredient"
    inventories_menu = "Inventory"

    MAIN_MENU = {
        mealplanner_menu: mealplanner,
        recipe_menu: create_recipe,
        new_ingredient_menu: add_new_ingredient,
        inventories_menu: inventory_manager
    }


def main():

    # MAIN CONTROLLER
    controller = controllers.controller.Controller()

    # CONFIG ACTIONS
    config_items: list = list(Config.MAIN_MENU.keys())
    config_menu: dict = Config.MAIN_MENU

    while True:

        # RENDER MAIN MENU SCREEN
        screen = controller.views.main_screen.MainScreen(config_items)
        screen.render_screen()

        user_request = input("\nSelect action >>> ")
        if user_request in ["q", "Q"]:
            break

        else:
            action_request = config_items[int(user_request)-1]
            action_trigger = config_menu.get(action_request)
            action_trigger()


if __name__ == '__main__':
    main()


