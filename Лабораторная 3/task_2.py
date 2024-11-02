def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на участники
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общих участников
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Находим общих участников с разделителем "|"
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(common_participants)  # Вывод: ['Петров', 'Сидоров']

# Проверяем работу функции с разделителем ","
participants_first_group_csv = "Иванов,Петров,Сидоров"
participants_second_group_csv = "Петров,Сидоров,Смирнов"

common_participants_csv = find_common_participants(participants_first_group_csv, participants_second_group_csv)
print(common_participants_csv)  # Вывод: ['Петров', 'Сидоров']
