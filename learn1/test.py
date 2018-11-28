def test_func():
    print("call test func")
# 被first函数import进去之后会执行下个函数
# 出现了test的pyc文件，是一个字节码文件，提高加载速度，被其他文件引用
if __name__ == "test":
    print("call test")

# pyo文件，-O选型生成优化编译字节码文件