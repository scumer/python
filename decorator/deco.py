# coding=utf-8
from __future__ import unicode_literals
from functools import update_wrapper, wraps, partial




print u'##无参数装饰器'
def deco(func):
    print func
    return func
@deco
def foo():pass
# foo()
# foo=deco(foo)

# ex 检查函数有没有说明文档
# def deco_functionNeedDoc(func):
#     if func.__doc__ == None :
#         print func, "has no __doc__, it's a bad habit."
#     else:
#         print func, ':', func.__doc__, '.'
#     return func
#
# @deco_functionNeedDoc
# def f():
#     print 'f() Do something'
# @deco_functionNeedDoc
# def g():
#     'I have a __doc__'
#     print 'g() Do something'
#
# f()
# g()

print u'##有参数装饰器'
def decomaker(arg):
    '通常对arg会有一定的要求'
    """由于有参数的decorator函数在调用时只会使用应用时的参数
       而不接收被装饰的函数做为参数，所以必须在其内部再创建
       一个函数
    """
    def newDeco(func):  #定义一个新的decorator函数
        print func, arg
        return func
    return newDeco

@decomaker("args")
def foo(var):pass
foo(1)


# 对带参数的函数进行装饰
print '*[EX3]*'
def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    print 'crossdomain'

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            print 'wrapped_function'
            print f, args, kwargs
            # return 'return wrapped_function'
            return f(*args, **kwargs)

        f.provide_automatic_options = False

        return update_wrapper(wrapped_function, f)
        # return wrapped_function
    return decorator


@crossdomain(origin='*')
def fun(funvar):
    """
    :param funvar:
    :return:
    """
    print 'fun'
    return 2


print fun('XXXX')
# print fun.__doc__
# print crossdomain(origin='*')(fun)('XXXXX')


print '*[deco template]*'
def deconame(*dargs, **dkwargs):
    # <code>
    def decorator(f):
        def wrapped_function(*args, **kwargs):
            # <code>
            ret = f(*args, **kwargs)
            # <op ret>
            # return ret
            return f(*args, **kwargs)
        # <code> ex:fun assign attr
        return update_wrapper(wrapped_function, f)

    return decorator


@deconame('deco args')
def fun(var):
    return 'return fun'

def deconame_ex(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        return f(*args, **kwargs)
    return decorator

@deconame_ex
def fun_ex():
    return 'Go'

print fun_ex()