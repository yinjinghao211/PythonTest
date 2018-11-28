# 冒泡排序

import random

list_data = []
for i in range(10):
    list_data.append(random.randint(0, 20))
print(list_data)

list_len = len(list_data) - 1

for i in range(10):
    sort_over = True
    for j in range(list_len - i):
        if list_data[j] > list_data[j + 1]:
            tmp = list_data[j]
            list_data[j] = list_data[j + 1]
            list_data[j + 1] = tmp
            sort_over = False
    if sort_over:
        break
print(list_data)
