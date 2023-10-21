import random 
import tkinter as tk


liam_meals = {
    "Malaysian Satay Supreme": ["Tofu", "Peanut Butter", "Capcicum", "Corn", "Beans"],
    "Chicken Salad Surprise": ["Chicken", "Kumara", "Capcicum", "Rocket"],
    "Lovely Quiche Lorraine": ["Eggs", "Capcicum", "Feta", "Pastry", "Sour Cream"],
    "Beef Burger Bonanza": ["Beef", "Buns", "Cheese"],
    "Thai Green Curry Galore": ["Thai Curry Paste", "Coconut Cream", "Broccoli", "Corn", "Peanuts"],
}

chi_meals = {
    "Asian Noodle Salad": ["Noodle", "Tofu"],
    "Buddha Bowls": ["Chickpeas", "Halloumi", "Capcicum", "Zucchini"],
    "Falafel Wraps": ["Falafel", "Halloumi"],
    "Poke Bowls": ["Tofu", "Edamame", "Ginger", "Wasabi"],
    "Mexican (Nut Mince/Jackfruit)": ["Nut Mince", "Jackfruit"],
    "Paneer Curry": ["Paneer", "Lentils", "Cauliflower"],
    "Peanut Stew": ["Tomatoes", "Peanuts"],
    "Fritters": ["Eggs", "Zucchini"],
    "Moroccan Tagine": ["Chickpeas", "Tomatoes", "Pumpkin"],
    "Vege Burgers": ["Kumara", "Black beans", "Beetroot"],
    "Pasta Verde": ["Pasta", "Basil", "Parmesan"],
    "Soup": ["Pumpkin"],
    "Kung Pao Tofu": ["Tofu", "Peanuts"],
}

# Combine the two lists into one
all_meals = liam_meals.copy()
all_meals.update(chi_meals)

selected_chef = "Any"  # Default chef
selected_ingredient = "Any"

def chef_meals(chef):
    if chef == "Liam":
        return liam_meals
    elif chef == "Chi":
        return chi_meals
    elif chef == "Any":
        return all_meals

def filter_by_ingredient(ingredient, meals):
    if ingredient == "Any":
        return meals
    filtered_meals = []
    for meal, ingredient_list in meals.items():
        if ingredient in ingredient_list:
            filtered_meals.append(meal)
    return filtered_meals

def pick_random_meal(chef, ingredient):
    available_meals = chef_meals(chef)
    available_meals = filter_by_ingredient(ingredient, available_meals)
    if available_meals:
        meal = random.choice(list(available_meals))
        result_label.config(text=f"Your meal is {meal}")
    else:
        result_label.config(text=f"No meals with {selected_ingredient}")

def pick_all_meal(chef, ingredient):
    available_meals = chef_meals(chef)
    available_meals = filter_by_ingredient(ingredient, available_meals)
    if available_meals:
        meals = ""
        for meal in available_meals:
            meals += f"{meal}\n"
        result_label.config(text=f"Your meals are \n {meals}")
    else:
        result_label.config(text=f"No meals with {selected_ingredient}")



def set_selected_chef(chef):
    global selected_chef
    selected_chef = chef

def set_selected_ingredient(ingredient):
    global selected_ingredient
    selected_ingredient = ingredient

def all_ingredients(selected_chef):
    ingredients = ["Any"]
    meals = chef_meals(selected_chef)
    for ingredient_list in meals.values():
        for ingredient in ingredient_list:
            if ingredient not in ingredients:
                ingredients.append(ingredient)
    return sorted(ingredients)

# Create a main window
root = tk.Tk()
root.title("Meal Picker")

# Create a label for the chef selection
chef_label = tk.Label(root, text="Pick your chef")
chef_label.grid(row=0, column=0, columnspan=2)

# Create radio buttons to select the chef
chef_var = tk.StringVar()
chef_var.set(selected_chef)  # Set the default chef

any_radio = tk.Radiobutton(root, text="Equality", variable=chef_var, value="Any", command=lambda: set_selected_chef("Any"))
any_radio.grid(row=1, column=0, sticky="w")

liam_radio = tk.Radiobutton(root, text="Liam", variable=chef_var, value="Liam", command=lambda: set_selected_chef("Liam"))
liam_radio.grid(row=1, column=1, sticky="w")

chi_radio = tk.Radiobutton(root, text="Chi", variable=chef_var, value="Chi", command=lambda: set_selected_chef("Chi"))
chi_radio.grid(row=2, column=0, columnspan=2, sticky="w")

# Create a label for the ingredient selection
ingredient_label = tk.Label(root, text="Pick your ingredient")
ingredient_label.grid(row=3, column=0, columnspan=2)

ingredient_var = tk.StringVar()
ingredient_var.set(selected_ingredient)

ingredients = all_ingredients(selected_chef)

# Create two columns for ingredient radio buttons
for i, ingredient in enumerate(ingredients):
    i_radio = tk.Radiobutton(root, text=f"{ingredient}", variable=ingredient_var, value=f"{ingredient}", command=lambda ingredient=ingredient: set_selected_ingredient(ingredient))
    i_radio.grid(row=4 + i // 2, column=i % 2, padx=10, pady=5, sticky="w")

# Create a button to pick a meal
pick_random_button = tk.Button(root, text="Pick a Random Meal", command=lambda: pick_random_meal(selected_chef, selected_ingredient))
pick_random_button.grid(row=5 + len(ingredients) // 2, column=0, columnspan=2)

# Create a button to pick a meal
pick_all_button = tk.Button(root, text="show Meals", command=lambda: pick_all_meal(selected_chef, selected_ingredient))
pick_all_button.grid(row=6 + len(ingredients) // 2, column=0, columnspan=2)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.grid(row=7 + len(ingredients) // 2, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()

