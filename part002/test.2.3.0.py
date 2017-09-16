# encoding: utf-8
# 2.3.1 字符串方法
filename = 'budget.csv     '
print(filename)

filename = filename.strip()
print(filename)

filename = filename.upper()
print(filename)

# 2.3.2 数值方法
print(42 ** 22)

print('zhang' + 'kai')

print(['zhang', 'kai'] + ['cui', 'lin'] +  ['cookie'])

# 2.3.3 列表方法
dog_names = []
dog_names.append('Joker')
dog_names.append('Simon')
dog_names.append('Walter')
print(dog_names)

dog_names.remove('Walter')
print(dog_names)


# 2.3.4 字典方法
animal_counts = {}
animal_counts['horses'] = 1
print(animal_counts)

animal_counts['dogs'] = 10
print(animal_counts)

keys = animal_counts.keys()
print(keys)

