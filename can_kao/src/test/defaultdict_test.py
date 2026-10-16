from collections import defaultdict

# 创建一个空的 defaultdict
d = defaultdict(int)  # 默认值为 int 类型，即默认值为 0

# 访问不存在的键，会返回默认值
print(d['key1'])  # 输出: 0

# 可以直接对不存在的键赋值
d['key2'] = 5
print(d['key2'])  # 输出: 5

# 可以使用任意可调用对象作为默认工厂函数
d = defaultdict(list)  # 默认值为一个空列表
d['list1'].append(1)
print(d['list1'])  # 输出: [1]

# 可以使用 lambda 函数定义复杂的默认值逻辑
d = defaultdict(lambda: 'default value')
print(d['key3'])  # 输出: 'default value'

# 默认值可以是任何对象，包括其他集合类型
d = defaultdict(set)
d['set1'].add(1)
print(d['set1'])  # 输出: {1}

"""
特点和优势
避免 KeyError 异常：默认值避免了在常规字典中访问不存在的键时可能引发的异常。
更简洁的代码：不需要在访问字典前检查键是否存在或者设置默认值。
适用性广泛：可以根据需要定义各种类型的默认值，包括函数、列表、集合等。
defaultdict 在处理需要默认值的场景下非常有用，特别是在处理计数、分组和缓存等问题时，可以显著简化代码逻辑和提高代码的可读性和可维护性。
"""