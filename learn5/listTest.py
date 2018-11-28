# 给定一个列表，统计列表中元素的个数

list1 = [1, 2, 3, 4, 5, 6]
list2 = ["zhangsan", [89, 90, 95], [92, 93, 96]]

a = list1.__len__()

count = len(list2)
print(isinstance(list2[0], list))

score_len = 0
i = 0
while i < count:
    if isinstance(list2[i], list):
        score_len += list2[i].__len__()
        i += 1
    else:
        score_len += 1
        i += 1

print(score_len)

# 使用列表实现堆栈结构

stack = []


def stack_push():
    val = input("push val:")
    stack.append(val)


def stack_pop():
    if len(stack) > 0:
        stack.pop(stack[0])


def stack_show():
    print(stack)


while True:
    cmd = input("enter cmd:")
    if cmd == "p":
        stack_push()
    elif cmd == "o":
        stack_pop()
    elif cmd == "s":
        stack_show()
    else:
        pass
