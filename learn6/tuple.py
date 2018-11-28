# 要元组只包含一个元素，必须要有一个逗号，用于和普通分组操作区分

tuple1 = ("sad",)

tuple2 = ("what", "is", "python")

print(type(tuple2))

tuple3 = "what is python"
print(tuple3)

tuple4 = ([1, 3, 5, 8])

print(tuple4, type(tuple4))

child = [("age", "height"), [10, 20]]

child1 = list(child)
child2 = list(child1)

# 可以看到id都是不一样的
print(id(child), id(child1), id(child2))

child1[0] = ("age", "height", "weight")
child1[1].append(30)

print(child1)
# 可以看到不同地址的两个列表会改变！！！！
# 原因就是浅拷贝，浅拷贝中列表的各个元素中，元组的地址会变，但是列表的地址不变
print(child2)

# 深拷贝

import copy

tea = [("age", "height"), [10, 20]]

# 元组不可变，所以深拷贝时元组地址不变
tea1 = copy.deepcopy(tea)
