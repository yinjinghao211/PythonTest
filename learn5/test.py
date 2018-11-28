
a = zip("1,2,3,4,5", (3, 4, 5), [3, 5, 6])
print(a.__next__())
print(a.__next__())

b = [1, 3, 5, 6]
c = ["sd", "sad"]
print(id(b))
b.extend(c)
print(b)
print(id(b))
b.append(c)
print(b)

print(id(b))

# extend和append的区别
# extend将他的参数视为list，extend的行为是把两个list接到一起，append是将他的参数视为element，作为一个整体添加上去的
# List里可以有任意的数据类型
