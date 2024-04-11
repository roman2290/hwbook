import pprint
with open('book.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            ingredient, quantity, measure = recepie
            ingredients.append({'ingredient_name': ingredient, 'quantitys': quantity, 'measures': measure})
        file.readline()
        cook_book[recepie_name] = ingredients
pprint.pprint(cook_book)

def get_shop_list_by_dishes(person_count, *dishes):
    for dish in cook_book:
        if dish == dishes:
            quantity = quantity * person_count
            print (dishes)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

d ={}
name = '2.txt'
with open(name, 'r', encoding='utf-8') as f:
    d[name] = [x for x in f.read().splitlines() if x]
with open('result.txt', 'w', encoding='utf-8') as file: 
    for key, value in sorted(d.items(), key=lambda x: len([x[1]])):  
        file.write(key + '\n')
        file.write(str(len(value))+ '\n')
        file.write('\n' .join(value))
        file.write('\n')
        
d = {}
name = '1.txt'
with open(name, 'r', encoding='utf-8') as f:
    d[name] = [x for x in f.read().splitlines() if x]
with open('result.txt', 'a', encoding='utf-8') as file:
    for key, value in sorted(d.items(), key=lambda x: len([[1]])):
        line_new = list()
        count = 0 
        for new_list in range(1, 3):
            i = d[name] 
            line_new.append(new_list)
        for line in line_new:
            if line:
                count += 1       
        file.write(key + '\n')
        file.write(str(count) + '\n')
        file.write('\n'.join(value[:2]))
    