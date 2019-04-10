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
def home():
    data = db.allergens.find()
    result = '<ul>'
    for record in data:
        result = result + '<li>' + record['allergen_name'] + '</li>'
    result = result + '</ul>'
    return result


# run application
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)
