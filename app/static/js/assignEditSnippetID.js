
const edit_snippet_form = document.getElementById("edit_snippet_form");

document.querySelectorAll(".snippet_card_button.edit").forEach(button => {
    button.addEventListener("click", () =>{
        console.log("clicked");
        edit_snippet_form.action = `/snippets/${button.dataset.snippet_id}/edit`;
    })
})