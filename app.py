from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # find one document from our mongo db and return it.
    mars = mongo.db.mars.find_one()
    # pass that listing to render_template
    return render_template("index.html", mars=mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    mars = mongo.db.mars

    mars_data = scrape_mars.scrape_info()

    mars.update_one({}, {"$set": mars_data}, upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
