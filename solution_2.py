def get_shop_list_by_dishes(dishes, dish_names, person_count):
    shop_list = {}
    for ingredients in dish_names:
        if ingredients in dishes:
            for i in dishes[ingredients]:
                i['quantity'] = int(i['quantity']) * person_count
                if i['ingredient name'] not in shop_list:
                    shop_list[i['ingredient name']] = {'measure':i['measure'], 'quantity': i['quantity']}
                else:
                    shop_list[i['quantity']] += i['quantity']
    return shop_list




