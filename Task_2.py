import pprint

# Загрузка данных из файла и создание cook_book
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

def shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book.get(dish, None)
        if ingredients is None:
            print(f"Блюдо '{dish}' нет в кулинарной книге.")
            continue

        for ingredient in ingredients:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count

            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list


selected_dishes = ['Омлет', 'Запеченный картофель']
person_count = 2
final_shop_list = shop_list_by_dishes(selected_dishes, person_count)
pprint.pprint(final_shop_list)