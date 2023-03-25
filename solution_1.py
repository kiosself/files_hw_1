def parse_reciepe(source):
    with open(source, 'rt', encoding='UTF-8') as file:
        dishes = {}
        for line in file:
            dish_name = line.strip()
            ing_count = int(file.readline())
            ingridients = []
            for _ in range(ing_count):
                ing_name, quantity, measure = file.readline().strip().split(' | ')
                ingridients.append({
                    'ingredient name': ing_name,
                    'quantity': quantity,
                    'measure':measure
                })
            file.readline()
            dishes[dish_name] = ingridients
    return dishes

