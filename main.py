from flask import Flask, request, redirect, render_template
from flask_hot_reload import HotReload

app = Flask(__name__)

# we have to use the external dependency of flask_hot_reload so everytime we update a file the page updates automatically.
# this is just a template that the pip extension gives, and works just well for what we need.
hot_reload = HotReload(app, 
    includes=[
        'templates',  # template directory
        'static',     # static files directory
        '.'          # current directory
    ],
    excludes=[
        '__pycache__',
        'node_modules',
        '.git'
    ]
)

@app.route("/")
def index():

    snippets = [
        {
            "title": "Read JSON file",
            "language": "Python",
            "code": "json.load(file)"
        },
        {
            "title": "Center a div",
            "language": "CSS",
            "code": "display: flex;"
        },
        {
            "title": "Read JSON file",
            "language": "Python",
            "code": "json.load(file)"
        },
        {
            "title": "Center a div",
            "language": "CSS",
            "code": "display: flex;"
        }
    ]

    return render_template("index.html", snippets = snippets)

@app.route("/snippets/new", methods = ["POST"])
def new_snippet():
    if (request.method == "POST"):
        name = request.form["snippet_name"]
        language = request.form["snippet_language"]
        snippet_code = request.form["snippet_code"]
        description = request.form.get("snippet_description") # we use form.get for this field, as this can be null. so using form.get returns a null value instead of possibly giving an error.

        print("new snippet request received correctly. printing request data:")
        print("snippet_name: ", name, "snippet_language: ", language, "snippet_code: ", snippet_code, "snippet_description (can be null): ", description)

        return redirect("/") # we can do a redirect after adding a new snippet. this is useful, as returning nothing will cause an error.

@app.route("/login_page")
def login_page():
    return render_template("login_page.html")

@app.route("/register_page")
def register_page():
    return render_template("register_page.html")

if __name__ == '__main__':
    app.run(debug=True)