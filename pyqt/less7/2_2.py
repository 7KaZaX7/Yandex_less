from collections import defaultdict

# Создаем словарь для группировки файлов по расширению и хранения их объема
file_groups = defaultdict(list)

# Считываем данные из файла input.txt
with open('input.txt', 'r') as file:
    for line in file:
        file_info = line.strip().split()
        if len(file_info) == 2:
            file_name, file_size = file_info[0], file_info[1]
            file_groups[file_name.split('.')[-1]].append((file_name, file_size))

# Открываем файл output.txt для записи результатов
with open('output.txt', 'w') as output_file:
    # Проходим по каждой группе файлов
    for ext, files in file_groups.items():
        total_size = 0
        files.sort(key=lambda x: x[0])  # Сортируем файлы внутри группы по имени
        output_file.write(f"{ext}\n")
        for file_name, file_size in files:
            output_file.write(f"{file_name} {file_size}\n")
            size_unit = file_size[-2:]  # Получаем единицу измерения
