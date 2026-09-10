from flask import Flask, request, redirect, render_template

from app import create_app

app = create_app()


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

if __name__ == '__main__':
    app.run(debug=True)