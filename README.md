# Recipe APi Code Exercise 

This application takes in a comma separated list of ingredients and returns the highest rated recipe that uses the 
provided ingredients.

Simply run **recipes.py** in this repo and you will be greeted with:
```
Please enter a comma separated list of the ingredients you have
Example: apples, sugar, flour, cinnamon
```

After entering a valid list of ingredients you will see the most highly rated recipe for your given 
ingredients.

```
{'id': 801901,
 'image': 'https://spoonacular.com/recipeImages/801901-312x231.jpg',
 'imageType': 'jpg',
 'likes': 1090005,
 'missedIngredientCount': 2,
 'missedIngredients': [{'aisle': 'Milk, Eggs, Other Dairy',
                        'amount': 2.0,
                        'id': 1001,
                        'image': 'https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg',
                        'meta': [],
                        'metaInformation': [],
                        'name': 'butter',
                        'original': '2 tbsp butter',
                        'originalName': 'butter',
                        'originalString': '2 tbsp butter',
                        'unit': 'tbsp',
                        'unitLong': 'tablespoons',
                        'unitShort': 'Tbsp'},
                       {'aisle': 'Sweet Snacks',
                        'amount': 4.0,
 ...
```
If there was an issue with the ingredients passed in then you will be promoted to re-enter your ingredients.

```
No recipes were found for the given list of ingredients: 
Please try entering ingredients again:
--------------------

Please enter a comma separated list of the ingredients you have
Example: apples, sugar, flour, cinnamon
```
Make sure to pass in simple ingredients separated by commas  
