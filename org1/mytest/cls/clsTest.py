# （Object）表示该类从哪个类继承下来的，Object类是所有类都会继承的类。
class Cls(object):
    def __new__(clazz):
        print("new %s" % clazz)
        return object.__new__(clazz)

    def __init__(self):
        # 加下划线就不能外部访问了
        self.__a = 0
        self.a = 0
        self.b = 1
        self.c = set([])
        self.name = "小1"

    def __str__(self):
        return "a->" + str(self.a) + "; b->" + str(self.b) + "; set->" + str(self.c) + "; name->" + self.name


c1 = Cls()
c2 = Cls()
Cls.name = "小张"
c3 = Cls()
c1.a += 100
# c1.__a = 0 # 报错
c2.a += 99
c3.c.add("aaa")

print(c1)
print(c2)
print(c3)

print("用例2 *" * 12)


class Cls(object):
    a = 0
    b = 1
    c = set([])
    name = "小2 outer"

    def __init__(self):
        # 加下划线就不能外部访问了
        self.__a = 0
        self.a = 0
        self.b = 1
        self.c = set([])
        self.name = "小2"

    def add(self, a: int, b: int) -> int:
        return a + b

    # 定义一个静态方法 addStatic，不显式设置返回值，默认返回None
    @staticmethod
    def addStatic(a: int, b: int):
        return a + b

    def __str__(self):
        return "a->" + str(self.a) + "; b->" + str(self.b) + "; set->" + str(self.c) + "; name->" + self.name


c1 = Cls()
c2 = Cls()
c3 = Cls()
c1.a += 100
c1.a += 100
c2.a += 99
c3.c.add("aaa")
# 通过类名访问类变量，不会改变实例变量的值，实际改的是 小2 outer
Cls.name = "小王"
print("Cls.name:" + Cls.name)
c3.name = "xiaoming"
print(c1)
print(c2)
print(c3)
# TypeError: add() takes 2 positional arguments but 3 were given
# 应改为 def add(self, a: int, b: int) -> int:
result = c3.add(3, 5)
print("result:" + str(result))

result = c3.addStatic(3, 5)
print("static result:" + str(result))
