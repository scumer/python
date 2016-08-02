# coding=utf-8



class A():
    pass


class B(object):
    pass

class C(type):
    pass
# print dir(A)
# print dir(B)
# print dir(C)



class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1
    def __init__(self, ar):
        print ar
        print MyClass.a

# one = MyClass(1)
# two = MyClass(2)

# two.a = 3
# print one.a
# #3
# #one和two完全相同,可以用id(), ==, is检测
# print id(one)
# #29097904
# print id(two)
# #29097904
# print one == two
# #True
# print one is two
# #True


#方法4:也是方法1的升级（高级）版本,
#使用装饰器(decorator),
#这是一种更pythonic,更elegant的方法,
#单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的

def singleton(cls, *args, **kwargs):
    instances = {}
    print cls,args,kwargs

    def _singleton(*ar,**kw):
        print ar,kw
        if cls not in instances:
            instances[cls] = cls(*ar,**kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass4(object):
    a = 1
    def __init__(self, x=0):
        self.x = x
        print x

one = MyClass4(2)
# two = MyClass4()

# three = singleton(MyClass4)()

# two.a = 3
# print one.a
# #3
# print id(one)
# #29660784
# print id(two)
# print id(three)
# #29660784
# print one == two
# #True
# print one is two
# #True
# one.x = 1
# print one.x
# #1
# print two.x
# #1

