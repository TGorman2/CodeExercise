#! python3
# This python script will return the most popular recipe found from the spoonacular API using the user supplied
# ingredients.
import constants
import requests
import pprint
import base64


# get_recipe makes the call to the spoonacular API and sorts so the result based on "likes" for each recipe. The recipe
# that uses all the ingredients provided, with the highest number of likes, will be returned.
def get_recipe(ingredientList):
    params = {"ingredients": ingredientList, "ranking": 1, "apiKey": base64.b64decode(constants.SPOON_KEY)}
    resp = requests.get(constants.SPOONACULAR_URL, params)
    recipes = resp.json()
    recipes = sorted(recipes, key=lambda recipe: recipe['likes'], reverse=True)
    # Return the most popular recipe that uses all the provided ingredients
    return recipes[0]


# list_missing_ingredients prints out the all the ingredients the user is missing for the given recipe
def list_missing_ingredients(recipe):
    print("These are the ingredients you are missing for this recipe:")
    for i in range(len(recipe["missedIngredients"])):
        # Print of the simple name of the missing ingredients
        pprint.pprint(recipe["missedIngredients"][i]["originalName"])


# get_ingredients_from_user will prompt the user for ingredients and give them an example of how to enter them.
def get_ingredients_from_user():
    print("Please enter a comma separated list of the ingredients you have")
    print("Example: apples, sugar, flour, cinnamon")
    userInput = input()

    # Validate input function needed

    # Get recipe
    recipe = get_recipe(userInput)

    # List missing ingredients
    list_missing_ingredients(recipe)

    # print out full recipe
    pprint.pprint(recipe)


def main():
    get_ingredients_from_user()


if __name__ == "__main__":
    main()
