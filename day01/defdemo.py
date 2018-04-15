#
#
# def power(x,n=2):
#
#     s = 1
#     while n>0:
#         n = n-1
#         s = s*x
#     return s
# #
# # print(power(5))
#
#
# def add_end(L=None):
#     if L is None:
#         L =[]
#     L.append("END")
#     return L
#
#
#
# print(add_end([1,2,3]))
# print(add_end(['x','y','z']))
# print(add_end())
# print(add_end())
# print(add_end())


# def calc(*num):
#     sum = 0
#     for n in num:
#         sum = sum +n * n
#     return sum
#
# nums = [1,2,3]
#
# print(calc(*nums))


# def person(name,age,*,city='beijing',job):
#
#
#
#     print(name,age,city,job)
#
#
#
#
# person('zhangsan',30,job='Techs')


# def f1(a,b,c=0,*args,**kw):
#     print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
#

# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#
#
# print(f1(1,2))
# print(f1(1,2,c=3))
# print(f1(1,2,3,'a','b'))
#
# print(f1(1,2,3,'a','b','c',d=11))


# args = (1,2,3,4,5)
# kw = {'d':99,'x':44}
#
# print(f1(*args,**kw))

#
# def fact(n):
#
#   return fact_iter(n,1)
#
# def fact_iter(num,product):
#
#     if num == 1:
#         return product
#     return fact_iter(num-1,num*product)
#
#
# print(fact_iter(2,120))
#
# L = ['A','B','C']
#
# print(L[0:3])
#
# print(L[-1:])
#
#
# L = []
#
# for x in range(1,11):
#     L.append(x * x)
#
# print(L)
#
# T = [x*x for x in range(1,11)]
#
# print(T)
#
# L = [x*x for x in range(1,11) if x%2 ==0]
#
# print(L)
#
# L = [m + n for m in 'ABC' for n in 'XYZ']
#
# print(L)
#
# from collections import Iterable
#
# print(isinstance('abc',Iterable))

# for i,value in enumerate(['A','B','C']):
#
#     print(i,value)
#


# print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))

import  functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('tt')
def now():
    print('2015-01-01')


now()

