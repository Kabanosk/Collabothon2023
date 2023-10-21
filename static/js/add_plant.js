
document.addEventListener("DOMContentLoaded", function () {

    const file_input = document.querySelector("#img_input")
    const name_input = document.querySelector("#name_input")
    const output = document.querySelector("#img_output")
    let imagesArray = []

    file_input.addEventListener("change", () => {
        const file = file_input.files
        imagesArray.push(file[0])
        document.getElementById('img_output').innerHTML = imagesArray[0].name
    })

    name_input.addEventListener("change", () => {
        console.log("chuj");
        if(imagesArray[0].name != "" && name_input.value != "")
        {
            document.getElementById("submit_button").style.display = "block";
        }
        else
        {
            document.getElementById("submit_button").style.display = "none ";
        }
    })

    const displayFormButton = document.querySelector("#display_form_button");
    const addPlantInputWrapper = document.querySelector("#add_plant_input_wrapper");
    
    displayFormButton.addEventListener("click", () => {
        event.preventDefault();
        if (addPlantInputWrapper.style.display !== "none") {
            addPlantInputWrapper.style.display = "none";
        } else {
            addPlantInputWrapper.style.display = "block";
        }
    });

})