#with open('book.txt', encoding='utf-8') as f:
    # lines = f.readline()
    
    # cook_book= {}

    
# 
def my_cook_book():
    with open('cook.txt', encoding='utf-8') as file:
        file = file.readline()
        cook_book = {}
        for line in file.read().split('\n\n'):
            name, _, *args = line.split('\n')
            cook_li = []
        for arg in args:
            ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
            cook_li.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = cook_li
        print (cook_book)