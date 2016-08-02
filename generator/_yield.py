# coding=utf-8



def yie():
    a = range(10)
    for i in a:
        yield i

    return

gen = yie()

# print type(gen)
# print next(gen)
# print gen.next()
# print gen.next()
# gen.close()
# print gen.next()



def gen():
    for i in range(10):
        X = yield i
        print X

g = gen()

# print next(g)
# print next(g)
# print next(g)

# print g.send(77)
# print next(g)

def gen():
    yield 23
    yield 3
    yield 2

l = gen()

# print list(gen())



def consumer():
    n = 0
    print 'init consumer'
    while True:
        n = yield n
        if not n:
            return
        n -= 1
        print u'消费1，剩余 %d' % n

def produce(c):
    n = 0
    next(c)
    while n < 6:
        n += 2
        print u'生产2， 共有 %d' % n
        n = c.send(n)
        print '确认还剩： %d' % n

    c.close()


c = consumer()
produce(c)

