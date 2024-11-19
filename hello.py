from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')

#def index():
#	return "<h2>Hello World</h2>"

def index():
	first_name = "PeterPan"
	stuff = "This is <strong>bold</strong>"
	fav_pizza = ["Salami", "Knoblauch", "Tuna", 423]
	return render_template("index.html", first_name=first_name,
		stuff=stuff,
		fav_pizza=fav_pizza)

@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404


