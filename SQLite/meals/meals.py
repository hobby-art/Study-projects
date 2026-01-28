"""
This program creates two tables: meals and ingredients. If user write a meal, the program gives its ingredients.
If user writes an ingredient, the program gives all the meals, that use this ingredient.
If user writes a meal with ingredients (fried potatos:potatoes,salt,oil,onions), the meal with ingredients will be
added to their corresponding databases.
"""

import sqlite3, sys

# Connect to a database and create the tables.
food_db_connect = sqlite3.connect("food.db", isolation_level=None)
# food_db_connect.execute("CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT")
# food_db_connect.execute("CREATE TABLE IF NOT EXISTS ingredients (name TEXT, meal_id INTEGER, FOREIGN_KEY(meal_id) REFERENCES meals(rowid)) STRICT")


# Main function that checks the input from the terminal.
def main():
    if sys.argv[1] == "quit":
        print("Exiting.")
        sys.exit()
    elif sys.argv[1] == "meal":
        meal_check(sys.argv[2])
    elif sys.argv[1] == "ingredients":
        ingredient_check(sys.argv[2])
    elif sys.argv[1] == "add":
        add_meal(sys.argv[2])
    else:
        print("Unknown command.")


# Checks if database has the ingredient.
def ingredient_check(input_ingredient: str):
    result = food_db_connect.execute(
        "SELECT name FROM ingredients WHERE name = ?", [input_ingredient]
    ).fetchone()
    if result:
        get_meals(input_ingredient)
    else:
        print("No such ingredient.")


# Checks if database has the meal.
def meal_check(input_meal: str):
    result = food_db_connect.execute(
        "SELECT name FROM meals WHERE name = ?", [input_meal]
    ).fetchone()
    if result:
        get_ingredients(input_meal)
    else:
        print("No such meal.")


# If ingredient is in the database, print all the meals that have it.
def get_meals(input_ingredient: str):
    print("Meals that go with this ingredient:")
    for meal in food_db_connect.execute(
        "SELECT DISTINCT meals.name FROM meals JOIN ingredients ON meals.rowid = ingredients.meal_id WHERE ingredients.name = ?",
        [input_ingredient],
    ):
        print(meal[0])


# If the meal is in the database, print all its ingredients.
def get_ingredients(input_meal: str):
    print(f"The ingredients of {input_meal} are:")
    get_meal_rowid = food_db_connect.execute(
        "SELECT rowid FROM meals WHERE name = ?", [input_meal]
    ).fetchone()[0]
    ingredients = food_db_connect.execute(
        "SELECT name FROM ingredients WHERE meal_id = ?", [get_meal_rowid]
    ).fetchall()
    for ingredient in ingredients:
        print(ingredient[0])


# Adds the meal and its ingredients to the database.
def add_meal(added_meal: str):
    meal_title = added_meal.split(":")[0]
    row_id = food_db_connect.execute(
        "INSERT INTO meals VALUES (?)", [meal_title]
    ).lastrowid
    meal_ingredients = added_meal.split(":")[1]
    for ingredient in meal_ingredients.split(","):
        food_db_connect.execute(
            "INSERT INTO ingredients VALUES (?, ?)", [ingredient, row_id]
        )
    print(f"Added {meal_title}")


if __name__ == "__main__":
    main()
