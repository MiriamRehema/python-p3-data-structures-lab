spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
   names = []
   for food in spicy_foods:
        names.append(food["name"])
   return names


def get_spiciest_foods(spicy_foods):
    spiciest_foods=[]
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    
    return spiciest_foods


    pass

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    
    for food in spiciest_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

    pass

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    
    if num_foods == 0:
        return 0
    
    average = total_heat_level / num_foods
    return int(average)
    pass

#def create_spicy_food(spicy_foods, spicy_food):
def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods

new_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(updated_spicy_foods)
  