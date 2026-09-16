from flask import render_template
from flask_login import current_user
from app import create_app
from app.forms import SnippetForm
from app.models import Snippets

app = create_app()


@app.route("/")
def index():

    # form needed for creating snippets. remember that we need to pass this and put it as:
    # {{ form.hidden_tag() }} so there are no problems on the form requests.
    form = SnippetForm()
    snippets = []

    # we obtain the snippets of the user if it's authenticated. we first filter_by, then we order by snippet_id descending, so in theory the last created-
    # snippets will be shown first, as the highest key values will be shown first (as the db has the snippet_id as auto incrementing.)
    if(current_user.is_authenticated):
        snippets = Snippets.query.filter_by(user_id = current_user.user_id).order_by(Snippets.snippet_id.desc()).all()

    return render_template("index.html", snippets = snippets, form = form)

if __name__ == '__main__':
    app.run(debug=True)