
const edit_snippet_name = document.getElementById("edit_snippet_name");
const edit_snippet_language = document.getElementById("edit_snippet_language");
const edit_snippet_code = document.getElementById("edit_snippet_code");
const edit_snippet_description = document.getElementById("edit_snippet_description");

const edit_snippet_form = document.getElementById("edit_snippet_form");

const edit_snippet_button_cancel = document.getElementById("edit_snippet_button_cancel");

edit_snippet_button_cancel.addEventListener("click", async () => {
    edit_snippet_form.classList.add("hidden")
})

document.querySelectorAll(".snippet_card_button.edit").forEach(button => {
    button.addEventListener("click", async () => {

        edit_snippet_name.value = button.dataset.snippet_name;
        edit_snippet_language.value = button.dataset.snippet_language;
        edit_snippet_code.value = button.dataset.snippet_code;
        edit_snippet_description.value = button.dataset.snippet_description;

        edit_snippet_form.classList.remove("hidden");

        // we also assign the snippet form action here. as our route requires it to handle the snippet_id (and it's out of the for that contains the snippet values-
        // like id, name, etc.) then we do it here to..
        edit_snippet_form.action = `/snippets/${button.dataset.snippet_id}/edit`;

    })
})