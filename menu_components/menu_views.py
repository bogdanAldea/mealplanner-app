class MenuValues:
    DEFAULT = 0
    MEALPLANNER = 1
    EDIT = 2
    NEW_MEALPLAN = 3
    SHOW_RECIPES = 4
    ADD_RECIPE = 5
    ADD_CATEGORY = 6
    ADD_INGREDIENT = 7
    BACK = 8
    EXIT = 9
    STOCK = 10

    MAIN_MENU_OPTIONS = [MEALPLANNER, EDIT, EXIT]
    MEALPLANNER_OPTIONS = [NEW_MEALPLAN, SHOW_RECIPES, BACK]
    EDIT_OPTIONS = [ADD_CATEGORY, ADD_CATEGORY, ADD_INGREDIENT, STOCK, BACK]


class MenuTexts:
    MAIN_MENU = """
======  MENIU PRINCIPAL =======
===     [1] Meal planner    ===
===     [2] Editari         ===
===     [9] Iesire          ===
===============================
OPTIUNE >>> """

    MEALPLANNER_MENU = """
======  MEALPLANNER  ==================
===     [3] Creaza meal plan nou    ===
===     [4] Afiseaza retete         ===
===     [8] Meniu principal         ===
=======================================
OPTIUNE >>> """

    EDIT_MENU = """
======  EDITARI  ==================
===     [5] Reteta noua         ===
===     [6] Categorie noua      ===
===     [7] Ingredient nou      ===
===     [8] Meniu principal     ===
===     [10] Editare Stoc       ===
===================================  
OPTIUNE >>> """