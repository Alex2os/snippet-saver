
// we can select all the buttons with the class snippet card button and copy, to apply them that whenever they're clicked, we copy the code snippet to -
// the user's clipboard. to access the code that has to be copied, we can specify this in the data of the button (see the button in index.html),
// using the same format of {{}} to specify variables inside html code. this is very useful when we want to pass data to either here in js or the routes.
document.querySelectorAll(".snippet_card_button.copy").forEach(button => {
    button.addEventListener("click", async () => {
        const code_to_copy = button.dataset.snippet_code

        await navigator.clipboard.writeText(code_to_copy);

        console.log("code copied.")
    })
})