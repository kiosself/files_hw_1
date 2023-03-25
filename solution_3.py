def read_file(file_name):
    file = ''
    f = open(file_name, 'rt', encoding='utf-8')
    file_len = (len(f.readlines()))
    f.seek(0)
    for _ in range(file_len):
        file += f.readline().strip() + '\n'
    f.close()

    return file_len, file

def stack_files():

    len_1, file_1 = read_file('1.txt')
    len_2, file_2 = read_file('2.txt')
    len_3, file_3 = read_file('3.txt')

    first = {'name': '1.txt', 'length': len_1, 'file': file_1}
    second = {'name': '2.txt', 'length': len_2, 'file': file_2}
    third = {'name': '3.txt', 'length': len_3, 'file': file_3}
    all_texts = [first, second, third]

    for i in range(len(all_texts)-1):
        if all_texts[i]['length'] > all_texts[i+1]['length']:
            all_texts[i], all_texts[i+1] = all_texts[i+1], all_texts[i]

    f = open('result_file.txt', 'w', encoding='utf-8')
    for i in all_texts:
        for j in i.values():
            f.writelines(str(j)+'\n')
        f.writelines('\n')

    f.close()

