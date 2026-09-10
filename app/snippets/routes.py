from flask import Blueprint, request, redirect, render_template
from app.forms import CreateSnippetForm
from app.models import Snippets
from flask_login import current_user, login_required
from app import db

snippets = Blueprint("snippets", __name__)

@snippets.route("/snippets/new", methods = ["POST"])
@login_required
def new_snippet():
    form = CreateSnippetForm()

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