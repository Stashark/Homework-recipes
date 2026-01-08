import pprint  #для красивого вывода


with open('recipes.txt', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

cook_book = {}
i = 0
while i < len(lines):
    if not lines[i]:
        i += 1
        continue

    dish_name = lines[i]
    num_ingredients = int(lines[i + 1])

    ingredients = []
    for j in range(i + 2, i + 2 + num_ingredients):
        parts = lines[j].split(' | ')
        ingredient = {
            'ingredient_name': parts[0],
            'quantity': int(parts[1]),
            'measure': parts[2]
        }
        ingredients.append(ingredient)


    cook_book[dish_name] = ingredients
    i += 2 + num_ingredients


pprint.pprint(cook_book)