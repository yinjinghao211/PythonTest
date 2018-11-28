# 元组直接赋值
dict1 = {"ip": "127.0.0.1", "id": "123456"}
# dict方法    元组列表或列表元组
dict2 = dict([("ip", "127.0.0.1"), ("id", "123456")])
# 赋值表达式
dict3 = dict(x=1, y=2)
dict4 = dict(**dict1)
print(dict3)
print(dict4)
# fromkeys方法    创建一个默认字典，字典中元素具有相同的值
dict5 = {}.fromkeys(('x', 'y'), -1)
dict6 = {}.fromkeys(('foo', 'bar'))
print(dict5, dict6)
print(type(dict1))

# 访问字典
print(dict1["ip"])
# 修改字典
dict1["ip"] = "127.0.0.2"
print(dict1["ip"])

# 访问
for key in dict1:
    print("dict[%s] = %s" % (key, dict1[key]))

# 删除条目并弹出对应value值
dict2.pop("ip")
# 删除最顶端元素
dict2.popitem()
# 清空所有条目
dict2.clear()
print(dict2)

# 字典的嵌套
dict11 = {"adds": {"ip": "127.0.0.1", "id": "123456"}, "it": "123456"}
# 嵌套访问  ---  键索引
print(dict11["adds"]["ip"])

dict11.update({"it": "515312"})
dict11.setdefault("is", "111110")
print(dict11.get("id", 100))
print(dict11)
print(dict11.items(), dict11.keys(), dict11.values())
