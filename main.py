from solution_1 import parse_reciepe
from solution_2 import get_shop_list_by_dishes
from solution_3 import stack_files
from pprint import pprint
#задание 1
#pprint(parse_reciepe('reciepes.txt'), sort_dicts=False)
#задание 2
#pprint(get_shop_list_by_dishes(parse_reciepe('reciepes.txt'), ['Запеченный картофель', 'Омлет'], 2))
#задание 3, выгрузка в result_file.txt
stack_files()