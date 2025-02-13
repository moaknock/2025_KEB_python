#Assignment
#v0.3) 2중 데코레이터 적용, 성능측정 데코레이터, 디스크림션 데코레이터를 팩토리얼 함수에 적용하시오.

import time

def description_decorator(func):
    def wrapper(*arg):
        print(func.__name__)
        print(func.__doc__)
        r = func(*arg)
        return r
    return wrapper # 함수를 호출하는게 아니어서 return wrapper뒤에 ()가 없어야함.

def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper

@time_decorator
@description_decorator
def factorial_repitition(n) -> int:
    """
    factorial function by loop
    :param n:
    :return: results of factorial operation
    """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

number = int(input())
print(f"{number}! = {factorial_repitition(number)}")
#t = time(time_decorator(factorial_repitition))
#(f"f{number}! = {t(number)}")



# number = int(input())
# ft = time_decorator(factorial_repitition)
# print(f"{number}! = {ft(number)}")
# number = int(input())
#     # s = time.time()
# print(f"{number}! = {factorial_repitition(number)}")
#     # e = time.time()
#     # print(e-s)