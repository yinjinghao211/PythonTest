x = 2

y = 3

# x的地址
print(id(x))
# y的地址
print(id(y))

x = 3
# 可以看到x和y共同占用一个地址单元
print(id(x))
print(id(y))

# 增量赋值，多重赋值，多元赋值

x = 2
print(x)
x += 2
print(x)

x = y = 10

print(x, y)

x, y = 7, 8
print(x, y)

a = 10;print(a)
if a == 10:
    print(a)

str1 = "\'"
print(str1)

str2 = "\""

print(str2)
# 表示Ascll码字符
str3 = "this is a : \x61"

print(str3)

print(ord('a'))
# 换行符
str4 = "abc\ndef"
print(str4)

# 替换了前三个字符
str5 = "aaaa\rasd"
print(str5)

# 制表符
str6 = "saas\tsda"
print(str6)
# 转义字符
str7 = "sda\vss"
print(str7)

x **= x
print(x)

x = x % 2
print(x)

x = x // 2
print(x)


