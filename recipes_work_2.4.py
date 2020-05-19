cook_book = {}

def read_recipes():
    number = ['1','2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9', '0']

    with open('recipes.txt', encoding='utf8') as recipes:
        for line in recipes:
            lines = line.rstrip()
            lines_clear = lines.split(' | ')

            if lines_clear[0] in number: #сохраняем количество ингр. в переменной
                number_ingredients = int(lines_clear[0])

            if len(lines_clear) == 1 and len(lines_clear[0]) > 1: #назначение названия блюда ключом во временном и финальном словаре
                temp_dict = {}
                name_cook = lines_clear[0]
                temp_dict[name_cook] = []
                cook_book[name_cook] = None
                score = 0 #счетчик ингр.
                temp_list = []

            elif len(lines_clear) > 2: # работа с ингридиентами
                demp_very_dict = {'ingredient_name': lines_clear[0], 'quantity': lines_clear[1], 'measure': lines_clear[2] }
                temp_list.append(demp_very_dict)
                score += 1
                if score == number_ingredients: #если счетчик и кол-во ингр. совпадают
                    temp_dict[name_cook] = temp_list
                    #temp_dict сохроняет каждое отдельное блюдо в отдельный словарь, ниже решение этой проблемы
                    for final_key, final_value in temp_dict.items():
                        if final_key:
                            cook_book[final_key] = final_value
    print(f'Задание №1 {cook_book}')


read_recipes()



def get_shop_list_by_dishes(dishes, person_count):

    dict_cook = {}
    for name_cook, ingr_cook in cook_book.items():
        if name_cook in dishes:
            for ingredients in ingr_cook:
                dict_cook[(list(ingredients.values())[0])] =\
                    {'measure': (list(ingredients.values())[2]),
                     'quantity': int((list(ingredients.values())[1]))*person_count }
    print(f'Задание №2 {dict_cook}')


get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2)