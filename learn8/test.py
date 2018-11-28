
# 找到列表中的最大元素

list1 = [1, 4, 6, 8, 34, 643]

i = 0
temp = 0
while i < len(list1):
    if temp < list1[i]:
        temp = list1[i]
    else:
        pass
    i = i + 1
print(temp)

# 实现阶乘

n = 10
i = n
s = 1
while i > 0:
    s *= i
    i = i - 1

print(s)

# for 语句的用法

list2 = range(10)
# 此语句会先判断列表是否为空，如果为空，则不会把列表的值付给val
for val in list2:
    print(val)

# 遍历序列
colors = ["green", "red", "white", "black"]

# 使用序列项迭代
for color in colors:
    print(color)
# 使用索引遍历
for index in range(len(colors)):
    print(colors[index])
# 使用序列和索引进行迭代
for index, color in enumerate(colors):
    print(index, color)

# 统计字符串中字符和数字的个数

i = 0
n = 0

while True:
    str1 = input("enter str : ")
    if str1 == "q":
        break
    for val in str1:
        if 'A' <= val <= 'Z' or 'a' <= val <= 'z':
            i = i + 1
        elif '0' <= val <= '9':
            n = n + 1

print("i = %d , n = %d " % (i, n))


