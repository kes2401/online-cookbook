import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo, pymongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

# mongo = PyMongo(app) ----REMOVE???

client = pymongo.MongoClient(os.getenv('MONGO_URI'))
db = client.cookbook


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def home():
    return render_template('login.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route('/recipelist')
def recipelist():
    recipes = db.recipes.find()
    return render_template('recipelist.html', recipes=recipes)
    
@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

@app.route('/add_recipe')
def add_recipe():
    cuisines = db.cuisines.find()
    ingredients = db.ingredients.find()
    allergens = db.allergens.find()
    return render_template('add_recipe.html', cuisines=cuisines, ingredients=ingredients, allergens=allergens)
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    
    # orangise method steps from form and build new ordered array containing them
    step_keys = []
    method_steps = []
    for stepkey in request.form.to_dict():
        if 'step' in stepkey:
            step_keys.append(stepkey)
    for i in range(1, len(step_keys) + 1):
        method_steps.append(request.form.get('step-' + str(i)))
    
    # organise ingredients from form and build new 2D containing qty-ingredient pairs
    ingredients_arr = []
    qty_arr = []
    ing_arr = []
    for ing_key in request.form.to_dict():
        if 'ingredient-qty-' in ing_key:
            qty_arr.append(ing_key)
        if 'ingredient-name-' in ing_key:
            ing_arr.append(ing_key)
    for i in range(1, len(qty_arr) + 1):
        qty = request.form.get('ingredient-qty-' + str(i))
        ing = request.form.get('ingredient-name-' + str(i))
        ingredients_arr.append([qty, ing])
    
    # find selected allergens and form new array containing them
    allergens = db.allergens.find()
    allergen_arr = []
    for allergen in list(allergens):
        for key in request.form.to_dict():
            if key == allergen['allergen_name']:
                allergen_arr.append(key)
    
    # create new database document and insert it to database
    new_recipe = {}
    new_recipe['recipe_name'] = request.form.get('recipe_name')
    new_recipe['ingredients'] = ingredients_arr
    new_recipe['method'] = method_steps
    new_recipe['allergens'] = allergen_arr
    new_recipe['views'] = 0
    new_recipe['upvotes'] = 0
    new_recipe['author'] = 'my own Author ID'
    new_recipe['cuisine'] = request.form.get('cuisine') # --- switch to cuisine database object ID ???
    new_recipe['image_url'] = request.form.get('image_url')
    db.recipes.insert_one(new_recipe)
    
    return redirect(url_for('recipelist'))

# run application
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
