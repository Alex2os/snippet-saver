from flask import Blueprint, request, redirect, render_template
from app.forms import SnippetForm
from app.models import Snippets
from flask_login import current_user, login_required
from app import db

snippets = Blueprint("snippets", __name__)

@snippets.route("/snippets/new", methods = ["POST"])
@login_required
def new_snippet():
    form = SnippetForm()

    if(form.validate_on_submit()):

        print("new_snippet form validated. creating snippet...")

        name = form.name.data
        language = form.language.data
        code = form.code.data
        description = form.description.data

        new_snippet = Snippets(snippet_name = name, snippet_language = language, snippet_code = code, snippet_description = description, user_id = current_user.user_id)
        db.session.add(new_snippet)
        db.session.commit()

        print("snippet created properly.")

        return redirect("/")

    print(form.errors)
    return "Form validation failed", 400

# when we create the route, we specify that it will receive a parameter. in this case it receives the snippet_id, with which we can work then here.
@snippets.route("/snippets/<int:snippet_id>/erase", methods = ["POST"])
@login_required
def erase_snippet(snippet_id):

    # we obtain the snippet and at the same time check if the user_id is the same as the current_user id.
    snippet = Snippets.query.filter_by(snippet_id = snippet_id, user_id = current_user.user_id).first()

    if(snippet):
        db.session.delete(snippet)
        db.session.commit()

        print("snippet erased successfully")

        return redirect("/")

    return "The snippet could not be erased.", 400

@snippets.route("/snippets/<int:snippet_id>/edit", methods = ["POST"])
@login_required
def edit_snippet(snippet_id):
    form = SnippetForm()

    if(form.validate_on_submit()):

        snippet = Snippets.query.filter_by(snippet_id = snippet_id, user_id = current_user.user_id).first()

        if(not snippet):
            return "The snippet does not exists", 400

        # we can just change the snippet values here and then commit, and this will work to update or edit the row inside the database.
        snippet.snippet_name = form.name.data
        snippet.snippet_language = form.language.data
        snippet.snippet_code = form.code.data
        snippet.snippet_description = form.description.data

        db.session.commit()

        print("snippet with id: ", snippet_id, "edited correctly.")

        return redirect("/")

    print(form.errors)
    return "Form validation failed", 404


# previous code for getting the new snippet data request. just for testing/learning
"""
        name = request.form["snippet_name"]
        language = request.form["snippet_language"]
        snippet_code = request.form["snippet_code"]
        description = request.form.get("snippet_description") # we use form.get for this field, as this can be null. so using form.get returns a null value instead of possibly giving an error.

        print("new snippet request received correctly. printing request data:")
        print("snippet_name: ", name, "snippet_language: ", language, "snippet_code: ", snippet_code, "snippet_description (can be null): ", description)

        return redirect("/") # we can do a redirect after adding a new snippet. this is useful, as returning nothing will cause an error.
"""