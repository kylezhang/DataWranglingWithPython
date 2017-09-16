# encoding: utf-8
# 工具函数：type, dir, help

# 2.4.1 type 查看对象的类型
filename = 'budget.csv'
print(type(filename))

code = 1234
print(type(code))

dogs_list = ['dog1', 'dog2']
print(type(dogs_list))

animal_dic = {}
print(type(animal_dic))


# 2.4.2 dir 返回对象的所有方法与属性
animals_str = 'cat, dog, horses'
print(dir(animals_str))

animals_str_to_list = animals_str.split(',')
print(animals_str_to_list)

print(dir(animals_str_to_list))

print(dir(1))
print(dir(1.0))


# 2.4.3 help 返回对象的帮助文档
print(help(animals_str.split))