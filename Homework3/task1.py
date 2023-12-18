# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]


original_list = [1, 2, 3, 1, 2]
print(original_list)
unique_dublicate_list = list({item for item in original_list if original_list.count(item) > 1})
print(unique_dublicate_list)
