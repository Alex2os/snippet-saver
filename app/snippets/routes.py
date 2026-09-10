from flask import Blueprint, request, redirect, render_template

snippets = Blueprint("snippets", __name__)

@snippets.route("/snippets/new", methods = ["POST"])
def new_snippet():
    if (request.method == "POST"):
        name = request.form["snippet_name"]
        language = request.form["snippet_language"]
        snippet_code = request.form["snippet_code"]
        description = request.form.get("snippet_description") # we use form.get for this field, as this can be null. so using form.get returns a null value instead of possibly giving an error.

        print("new snippet request received correctly. printing request data:")
        print("snippet_name: ", name, "snippet_language: ", language, "snippet_code: ", snippet_code, "snippet_description (can be null): ", description)

        return redirect("/") # we can do a redirect after adding a new snippet. this is useful, as returning nothing will cause an error.