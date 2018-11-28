import random

# 判断闰年

year = int(input("inter year:"))
x = 2014
if (x % 4 == 0 and x % 400 == 0 and x % 100 != 0):
    print(True)
elif(year % 4 == 0 and year % 400 == 0 and year % 100 != 0):
    print(True)
else:
    print(False)

# 0-15 之间的随机数转使用二进制的字符串表示

x = random.randint(0, 15)
i = 0
s = ""

while(i < 4):
    if(x >> i & 0x01):      # 判断这一位是否是1
        s = "1" + s
    else:
        s = "0" + s
    i = i + 1

print(s)