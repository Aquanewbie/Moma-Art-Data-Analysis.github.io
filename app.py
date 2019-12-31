from flask import Flask, render_template

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("landing.html", mars=mars)

@app.route("/Vis1")
def Vis1():
    return render_template("visualization1.html", mars=mars)

@app.route("/Vis2")
def Vis2():
    return render_template("visualization2.html", mars=mars)

@app.route("/Vis3")
def Vis3():
    return render_template("visualization3.html", mars=mars)

@app.route("/Vis4")
def Vis4():
    return render_template("visualization3.html", mars=mars)

@app.route("/comparisons")
def comparisons():
    return render_template("comparisons.html", mars=mars)

@app.route("/data")
def data():
    return render_template("data.html", mars=mars)

if __name__ == "__main__":
    app.run()