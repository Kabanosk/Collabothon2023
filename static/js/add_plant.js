
document.addEventListener("DOMContentLoaded", function () {

    const file_input = document.querySelector("#img_input")
    const name_input = document.querySelector("#name_input")
    let imagesArray = []

    // Get all elements with the class "plant_input"
    const plant_inputs = document.querySelectorAll(".plant_input");

    // Add a change event listener to each input element
    plant_inputs.forEach((element) => {
        element.addEventListener("change", () => {
            const all_inputs_set = [...plant_inputs].every((input) => input.value.trim() !== "");

            if (all_inputs_set) {
                document.querySelector("#submit_button").style.display = "block";
                // document.querySelector("#submit_button").style.visibility = "visible";
                // document.querySelector("#submit_button").style.opacity = "1";
                
            } else {
                document.querySelector("#submit_button").style.display = "none";
                // document.querySelector("#submit_button").style.visibility = "hidden";
                // document.querySelector("#submit_button").style.opacity = "0";
            }
        });
    });

    const displayFormButton = document.querySelector("#display_form_button");
    const addPlantInputWrapper = document.querySelector("#add_plant_input_wrapper");
    
    displayFormButton.addEventListener("click", () => {
        event.preventDefault();
        if (addPlantInputWrapper.style.visibility !== "visible") {
            //addPlantInputWrapper.style.display = "none";
            addPlantInputWrapper.style.visibility = "visible";
            addPlantInputWrapper.style.opacity = "1";
        } else {
            //addPlantInputWrapper.style.display = "block";
            addPlantInputWrapper.style.visibility = "hidden";
            addPlantInputWrapper.style.opacity = "0";
        }
    });

})