import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

# Seed data for initial dev purposes prior to DB connection
data = {
    'allergens': ['milk', 'eggs', 'soy'],
    'cuisines': ['american', 'british', 'chinese', 'italian'],
    'users': ['testuser'],
    'recipies': [],
    'ingredients': ['flour', 'eggs', 'butter', 'sugar', 'tomato', 'cheese']
}


@app.route('/')
def index():
    return render_template('base.html')


# run application
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
