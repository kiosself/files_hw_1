def stack_files():
    f = open('1.txt', 'rt', encoding='utf-8')
    file_1 = ''
    file_1_range = len(f.readlines())
    f.seek(0)
    for _ in range(file_1_range):
        file_1 += f.readline()
    f.close()

    f = open('2.txt', 'rt', encoding='utf-8')
    file_2 = ''
    file_2_range = len(f.readlines())
    f.seek(0)
    for _ in range(file_2_range):
        file_2 += f.readline().strip()
    f.close()

    f = open('3.txt', 'rt', encoding='utf-8')
    file_3 = ''
    file_3_range = len(f.readlines())
    f.seek(0)
    for _ in range(file_3_range):
        file_3 += f.readline()
    f.close()

    first = {'name': '1.txt', 'length': file_1_range, 'file': file_1}
    second = {'name': '2.txt', 'length': file_2_range, 'file': file_2}
    third = {'name': '3.txt', 'length': file_3_range, 'file': file_3}
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

