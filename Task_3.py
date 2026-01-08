with open('1.txt', 'r', encoding='utf-8') as f_1:
    count_1 = len(f_1.readlines())

with open('1.txt', 'r', encoding='utf-8') as f_1:
    text_1 = f_1.read()

with open('2.txt', 'r', encoding='utf-8') as f_2:
    count_2 = len(f_2.readlines())

with open('2.txt', 'r', encoding='utf-8') as f_2:
    text_2 = f_2.read()

with open('3.txt', 'r', encoding='utf-8') as f_3:
    count_3 = len(f_3.readlines())

with open('3.txt', 'r', encoding='utf-8') as f_3:
    text_3 = f_3.read()

files_info = [(count_1, '1.txt', text_1), (count_2, '2.txt', text_2), (count_3, '3.txt', text_3)]
files_info.sort()

with open('result.txt', 'w', encoding='utf-8') as file_result:
    for count, filename, content in files_info:
        file_result.write(f"{filename}\n")
        file_result.write(f"{count}\n")
        file_result.write(content)

print("Итоговый файл 'result.txt' создан!")