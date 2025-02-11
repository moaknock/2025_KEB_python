#dan = input("Input dan: ")

#dan = int(input("Input dan: "))
#for i in range(1,10,1):
#    print(f"{dan}*{i} = {dan * i}")
#print(2**10) #1024
#print(16**0.5) # 4.0
#n = int(input("Input number : "))
#is_prime = True

# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램을 작성
# v1.3) **  대신 pow 함수

def is_prime(number) -> bool:
    """
    A function that determines whether a prime number is present
    and returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if number >= 2:
        for i in range(2, int(number**0.5) + 1):          #n**0.5 => n의 0.5제곱
            if number % i == 0:
                return False
    else:
        return False
    return True

# main
help(is_prime)

number = int(input ("Input number: "))

if is_prime(number):
    print(f"{number} is prime number")
else:
    print(f"{number} is NOT prime number")