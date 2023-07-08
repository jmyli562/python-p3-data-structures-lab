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
    return [foods.get("name") for foods in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [foods for foods in spicy_foods if foods["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    return [
        print(
            f'{foods["name"]} ({foods["cuisine"]}) | Heat Level: {"🌶" * foods["heat_level"]}'
        )
        for foods in spicy_foods
    ]


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    new_list = [foods for foods in spicy_foods if cuisine == foods["cuisine"]]

    return new_list[0]


def print_spiciest_foods(spicy_foods):
    return [
        print(
            f'{foods["name"]} ({foods["cuisine"]}) | Heat Level: {"🌶" * foods["heat_level"]}'
        )
        for foods in spicy_foods
        if foods["heat_level"] > 5
    ]


def get_average_heat_level(spicy_foods):
    sum = 0
    avg = 0
    for food in spicy_foods:
        sum = sum + food["heat_level"]

    avg = sum / len(spicy_foods)

    return avg


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

    return spicy_foods
