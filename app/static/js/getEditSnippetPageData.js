
const edit_snippet_name = document.getElementById("edit_snippet_name");
const edit_snippet_language = document.getElementById("edit_snippet_language");
const edit_snippet_code = document.getElementById("edit_snippet_code");
const edit_snippet_description = document.getElementById("edit_snippet_description");

const edit_snippet_modal = document.getElementById("edit_snippet_modal");

const edit_snippet_button_cancel = document.getElementById("edit_snippet_button_cancel");

edit_snippet_button_cancel.addEventListener("click", async () => {
    edit_snippet_modal.classList.add("hidden")
})

document.querySelectorAll(".snippet_card_button.edit").forEach(button => {
    button.addEventListener("click", async () => {

        edit_snippet_name.value = button.dataset.snippet_name;
        edit_snippet_language.value = button.dataset.snippet_language;
        edit_snippet_code.value = button.dataset.snippet_code;
        edit_snippet_description.value = button.dataset.snippet_description;

        edit_snippet_modal.classList.remove("hidden")

    })
})