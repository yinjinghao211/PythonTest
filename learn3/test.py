
import sys
import random
print(sys.getsizeof(10))

print(sys.getsizeof(1.1))

# python中没有长整形，统一用int类型来取代
# sys.getsizeof(10L)

# 数据的大小
print(sys.getsizeof(2+10j))

print(sys.getsizeof(True))

print(sys.maxsize)

# 查看数据类型
print(type(1+1j))

# 强制类型转换
print(float(10))

# 虚数
print(complex(10))

# 随机生成浮点数
print(10 * random.random())

print(random.uniform(1, 10))

# 生成整数
print(random.randint(0, 99))

# 从制定范围内，在指定基数递增的集合中获取一个随机数
print(random.randrange(0, 100, 3))

# 从序列中获取一个随机元素
print(random.choice('sadasda213123'))

# 将一个列表中的元素打乱
item = [2, 1, 3, 1, 4, 1]
print(random.shuffle(item))
print(item)

# 从制定序列中随机获取指定长度的片段
print(random.sample(item, 3))


