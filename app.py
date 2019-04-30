import os
from bson.objectid import ObjectId
from flask import Flask, render_template, url_for, redirect, request, flash, session
from flask_pymongo import PyMongo, pymongo
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

# mongo = PyMongo(app) ----REMOVE???

client = pymongo.MongoClient(os.getenv('MONGO_URI'))
db = client.cookbook

placeholder_image = 'http://placehold.jp/48/dedede/adadad/400x400.jpg?text=Image%20Not%20Available'

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        # Retrieve users from database and check that username exists
        username_entered = request.form.get('username')
        this_user_in_db = db.users.find_one({'username': username_entered})
        if not this_user_in_db:
            flash('Username does not exist', 'error')
            return render_template('login.html')
        
        # once username exists in database confirm password entered and that both fields are populated
        password_entered = request.form.get('password')
        if not username_entered or not password_entered:
            flash('Please enter a valid username and password', 'error')
            return render_template('login.html')
        
        # check password against this username's user record in database
        if pbkdf2_sha256.verify(password_entered, this_user_in_db['password']):
            # once verified with user record in database, start a new session and redirect to main recipelist
            session['user'] = username_entered
            session['user_id'] = str(this_user_in_db['_id'])
            print(session['user'])
            print(session['user_id'])
            
            flash('You have successfully logged in', 'success')
            return redirect(url_for('recipelist'))
        else:
            # else if password does not match, flash error message
            flash('The password did not match the user profile', 'error')
            return render_template('login.html')
    
    return render_template('login.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        # Retrieve users from database and check if requested username already exists
        users_in_db = list(db.users.find())
        if len(users_in_db) > 0:
            for user in users_in_db:
                if user['username'] == request.form.get('username'):
                    flash('Username is already taken', 'error')
                    return render_template('signup.html')
        
        # Begin creating new_user dict for possible insertion to database
        new_user = {}
        new_user['username'] = request.form.get('username')
        new_user['email'] = request.form.get('email')
        # TODO - (future feature) add functionality to see if email address was already used, & build password recovery feature as required
        new_user['password'] = pbkdf2_sha256.hash(request.form.get('password'))
        new_user['password_reconfirm'] = pbkdf2_sha256.verify(request.form.get('password-reconfirm'), new_user['password'])
        
        # if password entered is not properly re-confirmed
        if not new_user['password_reconfirm']:
            flash('Passwords did not match', 'error')
            return render_template('signup.html')    
        
        # Once all required field are populated without error above, insert new user into database and redirect to login page
        if new_user['username'] and new_user['email'] and new_user['password']:
            new_user['recipes'] = []
            db.users.insert_one(new_user)
            flash('You have successfully signed up, you can now log in', 'success')
            return redirect(url_for('home'))

    return render_template('signup.html')

@app.route('/recipelist')
def recipelist():
    recipes = list(db.recipes.find())
    cuisines = list(db.cuisines.find())
    return render_template('recipelist.html', recipes=recipes, cuisines=cuisines)
    
@app.route('/recipe/<recipe_id>/')
def recipe(recipe_id):
    this_recipe = db.recipes.find_one({'_id': ObjectId(recipe_id)})
    allergens = list(db.allergens.find())
    return render_template('recipe.html', recipe=this_recipe, allergens=allergens)

@app.route('/add_recipe')
def add_recipe():
    cuisines = list(db.cuisines.find())
    ingredients = list(db.ingredients.find().sort('ingredient_name', pymongo.ASCENDING))
    allergens = list(db.allergens.find())
    return render_template('add_recipe.html', cuisines=cuisines, ingredients=ingredients, allergens=allergens)
    
@app.route('/edit_recipe/<recipe_id>/')
def edit_recipe(recipe_id):
    cuisines = list(db.cuisines.find())
    ingredients = list(db.ingredients.find().sort('ingredient_name', pymongo.ASCENDING))
    allergens = list(db.allergens.find())
    this_recipe = db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('edit_recipe.html', cuisines=cuisines, ingredients=ingredients, allergens=allergens, recipe=this_recipe)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    
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

    # create new document that will be used as the update dict to update database
    updated_recipe = {}
    updated_recipe['recipe_name'] = request.form.get('recipe_name')
    updated_recipe['ingredients'] = ingredients_arr
    updated_recipe['method'] = method_steps
    updated_recipe['allergens'] = allergen_arr
    updated_recipe['cuisine'] = request.form.get('cuisine') # --- switch to cuisine database object ID ???
    updated_recipe['image_url'] = request.form.get('image_url')
    db.recipes.update_one({'_id': ObjectId(recipe_id)}, {'$set': updated_recipe })
    
    return redirect(url_for('recipelist'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    db.recipes.delete_one({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipelist'))    

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