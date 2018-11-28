# 迭代器遍历

# 3.8开始已经停止使用
# from collections import Iterable
# 判断元素是否可以被迭代
# print(isinstance("12213", Iterable))
myIter = iter("hallowed")
for c in myIter:
    print(c)

newList = [x + 1 for x in range(10)]

print(newList)

# 加入条件判断
newList2 = [x + 1 for x in range(10) if x > 5]

print(newList2)

# 创建矩阵
newList3 = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]

print(newList3)

# 给定一个字符串返回每个字符对应的单词和长度
str1 = "sad asf hf ef das"
# split方法将字符串以空格分割成多个字符，存储在列表中
stuff = [[world, len(world)] for world in str1.split()]

print(stuff)