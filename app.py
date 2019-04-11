import os
from flask import Flask, render_template, url_for
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


# run application
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
