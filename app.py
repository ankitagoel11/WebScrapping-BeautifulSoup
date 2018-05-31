from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo

import mission_to_mars

app = Flask(__name__)

mongo = PyMongo(app)


@app.route('/')
def index():

    mongo.db.collection.remove( { } )
    mars_datasets = mongo.db.collection.find()

    data = mission_to_mars.title_scrape()
    imagelink = mission_to_mars.image_link()
    tweet_response = mission_to_mars.tweet_response()
    table_content = mission_to_mars.table_data()
    

    data_entry = {
        "title" : data['title'],
        "para" : data['paragraph'],
        'image' : imagelink['src'],
        'tweet_response' : tweet_response['today'],
        'table' : table_content
        
    }

    mongo.db.collection.update(
        {},
        data_entry,
        upsert=True
    )   

    return render_template('index.html', mars_datasets =  mars_datasets, table = table_content)



if __name__ == "__main__":
    app.run(debug=True)
