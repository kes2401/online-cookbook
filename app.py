import os
from flask import Flask, render_template, url_for, redirect
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

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')
    
@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

@app.route('/add_recipe')
def add_recipe():
    cuisines = db.cuisines.find()
    ingredients = db.ingredients.find()
    return render_template('add_recipe.html', cuisines=cuisines, ingredients=ingredients)
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    # insert to database
    
    return redirect(url_for('recipes'))

# run application
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
