from learn1 import test


def hello():
    print("print hello func")

# this is entry
if __name__ == "__main__":
    print("hello world")
    hello()
    test.test_func()
    print(test.__name__)
