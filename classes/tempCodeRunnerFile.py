
class MyClass():
    pass


class MySubClass(MyClass):
    pass


class MySubSubClass(MySubClass):
    pass


print(isinstance(MySubClass(), MySubSubClass))
