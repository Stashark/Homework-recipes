import pprint  # Для красивого вывода


def parse_recipes(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            stripped_line = line.strip()

            if not stripped_line:
                continue

            dish_name = stripped_line
            num_ingredients = int(f.readline().strip())
            ingredients = []
            '''
            Я узнала, что В Python символ _ часто используется
            как соглашение о наименовании переменных-пустышек (dummy variables),
            которые нужны лишь для синтаксической структуры цикла или конструкции,
            но сами по себе значения не имеют. 
            Надеюсь ничего страшного, что я это использовала здесь.
            '''
            for _ in range(num_ingredients):
                ingr_line = f.readline().strip()
                parts = ingr_line.split('|')

                ingredient = {
                    'ingredient_name': parts[0].strip(),
                    'quantity': int(parts[1].strip()),
                    'measure': parts[2].strip()
                }
                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients

    return cook_book

def shop_list_by_dishes(cook_book, dishes, person_count):
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



if __name__ == "__main__":
    cook_book = parse_recipes('recipes.txt')
    selected_dishes = ['Омлет', 'Запеченный картофель']
    person_count = 2
    final_shop_list = shop_list_by_dishes(cook_book, selected_dishes, person_count)

    pprint.pprint(final_shop_list)