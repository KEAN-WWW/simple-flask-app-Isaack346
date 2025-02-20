from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello CPS3500!"

@app.route('/new_page')
def new_page():
    return "This is a New Page!"

@app.route('/user/<name>')  # New dynamic route
def user(name):
    return render_template("index.html", username=name)  # Passes `name` to HTML

if __name__ == "__main__":
    app.run(debug=True)

