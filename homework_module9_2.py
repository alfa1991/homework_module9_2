first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Первый результат: длины строк из first_strings, если длина строки не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Второй результат: пары слов одинаковой длины из first_strings и second_strings
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# Третий результат: словарь, где ключом является строка, а значением - её длина, если длина строки четная
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Примеры вывода
print(first_result)  # [10, 8, 8]
print(second_result) # [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
print(third_result)  # {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
