# encoding: utf-8
# 数据容器
# 数据点

# 常见的容器：变量，列表，字典

# 2.2.1变量

filename = 'budget.csv'
print(filename)

# 2.2.2 列表, 具有某种共同关系的一组值。
shopping_list = ['milk', 'lettuce', 'eggs']
print(shopping_list)

cats =2
dogs = 5
horses =1

animal_counts = [cats, dogs, horses]
print(animal_counts)

# 列表可以嵌套

cat_names = ['Walter', 'Ra']
dog_names = ['Joker', 'Simon']

animal_names = [cat_names, dog_names]
print(animal_names)

# 2.2.3 字典 key value 键值对

animal_counts_dic = {'cats': 2, 'dogs': 5, 'horses': 1}
print(animal_counts_dic)
print(animal_counts_dic['cats'])
