def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines), ''.join(lines)


def process_files(filenames):
    files_info = []
    for filename in filenames:
        line_count, content = read_file(filename)
        files_info.append((line_count, filename, content))
    return sorted(files_info)


def write_result_to_file(output_filename, data):
    with open(output_filename, 'w', encoding='utf-8') as out_file:
        for count, filename, content in data:
            out_file.write(f"{filename}\n")
            out_file.write(f"{count}\n")
            out_file.write(content + "\n")



if __name__ == "__main__":
    filenames = ['1.txt', '2.txt', '3.txt']
    result_data = process_files(filenames)
    write_result_to_file('result.txt', result_data)
    print("Итоговый файл 'result.txt' успешно создан!")