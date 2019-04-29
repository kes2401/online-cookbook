document.addEventListener('DOMContentLoaded', function() {
    
    // Initialise the mobile sidenav
    let sidenav = document.querySelectorAll('.sidenav');
    let sidenavInstance = M.Sidenav.init(sidenav);
    
    // Initialise form select options
    let selects = document.querySelectorAll('select');
    let selectInstances = M.FormSelect.init(selects);
    
    // gather ingredients from server page render
    let ingredients = [];
    for (let i = 1; i < selects[1].length; i++) {
        ingredients.push(selects[1][i].innerHTML)
    }
    
    // Add button functionality to add additional ingredients
    let ingredientCount = $('.ingredient').length + 1;
    $('.add-ingredient-btn').click(function() {
        let newIngredient = document.createElement('div');
        newIngredient.className = 'ingredient';
        let htmlString = 
            `<div class="input-field col s4">
                <input id="quantity" name="ingredient-qty-${ingredientCount}" type="text" class="validate" autocomplete="off" required>
                <label for="quantity">Quantity</label>
            </div>
            <div class="input-field col s8">
                <select id="ingredient" name="ingredient-name-${ingredientCount}" required>
                    <option value="" disabled selected>Select Ingredient</option>`;
        for (let i = 0; i < ingredients.length; i++) {
            htmlString += `<option value="${ingredients[i]}">${ingredients[i]}</option>`
        }
        htmlString += `</select>
            </div>`;
        newIngredient.innerHTML = htmlString;
        $('.ingredients').append(newIngredient);
        ingredientCount++;
        
        // re-initialise selects on the page
        selects = document.querySelectorAll('select');
        selectInstances = M.FormSelect.init(selects);
    })
    
    // Add button functionality to remove last ingredient
    $('.remove-ingredient-btn').click(function() {
        $('.ingredient').last().remove();
        if (ingredientCount >= 2) {
            ingredientCount--;    
        }
    })
    
    // Add button functionality to add new step in method
    let stepCount = $('.step').length + 1;
    $('.add-step-btn').click(function() {
        let htmlString = `<li class="step">
                            <input name="step-${stepCount}" type="text" class="validate" autocomplete="off" required>
                          </li>`;
        $('#steps-list').append(htmlString);
        stepCount++;
    });
    
    // Add button functionality to remove last step in method
    $('.remove-step-btn').click(function() {
        $('.step').last().remove();
        if (stepCount >= 2) {
            stepCount--;    
        }
    })
});

