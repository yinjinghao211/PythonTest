
# 列表
list1 = [1, 3, 3, 4]
list2 = [2, 3, 4, 6]
# 元组
tuple1 = (1, 2, 3, 4)
tuple2 = (2, 3, 4, 5)
# 字符串
str1 = "sad"
# 分为正负索引
print(list1[0], list1[-1])
print(tuple1[1], tuple1[-1])
print(str1[0], str1[-1])

# 基本操作
print(1 in list1)
print(2 not in list1)
print(list1 + list2)
print(tuple2 + tuple1)
# 重复相加N次
print(tuple1*2)

# 切片操作
# 取区间内的值
print(list2[1:2])
# 每隔多少取元素
print(tuple2[0:4:2])

# 序列的内建函数
print(len(tuple2))
print(max(tuple2))
print(min(tuple2))
print(sum(tuple2))
# 以一个序列作为参数，返回一个逆序访问的迭代器
a = reversed(tuple1)
# 接受多个序列为参数，返回一个tuple列表
b = zip(tuple1, tuple2)
print(a.__next__())
print(a.__next__())
print(b.__next__())
print(b.__next__())
# 不是‘，’！！！！
print("%f" % 65.1)
print("%o" % 88)
print("%o" % 9)
print("%s" % [1, 2, 3, 4])
print("%s" % str((1, 2, 3, 5)))

print("%d %%" %(65))

print("%d %% %d" % (100, 100))

# 转义字符，与 r
print("\n")

print(r"\n")

x = "sdasd"

print(x.count("a", 0, 3))

print(x.capitalize())

a = u"以"

print(a, a.encode("utf-8"))