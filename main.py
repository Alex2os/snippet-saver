from flask import render_template
from flask_login import current_user
from app import create_app
from app.forms import CreateSnippetForm
from app.models import Snippets

app = create_app()


@app.route("/")
def index():

    # form needed for creating snippets. remember that we need to pass this and put it as:
    # {{ form.hidden_tag() }} so there are no problems on the form requests.
    form = CreateSnippetForm()
    snippets = []

    if(current_user.is_authenticated):
        snippets = Snippets.query.filter_by(user_id = current_user.user_id).all()

    return render_template("index.html", snippets = snippets, form = form)

if __name__ == '__main__':
    app.run(debug=True)