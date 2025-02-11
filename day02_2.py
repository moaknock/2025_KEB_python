# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램을 작성
# v1.3) **  대신 pow 함수

def is_prime(number) -> bool:
    """
    A function that determines whether a number is prime.
    Returns True if the number is prime, otherwise returns False.
    :param number: integer number
    :return: boolean type
    """
    if number < 2:
        return False

    i = 2
    while i <= int(number ** 0.5):
        if number % i == 0:
            return False
        i += 1

    return True


# main
help(is_prime)

number = int(input("Input number: "))

if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is NOT a prime number")
