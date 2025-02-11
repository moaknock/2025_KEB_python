# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램을 작성123
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


def print_prime_range(start, end):
    """
    Prints all prime numbers in the given range [start, end]
    :param start: starting number
    :param end: ending number
    """
    print(f"Prime numbers between {start} and {end}:")

    num = start
    while num <= end:
        if is_prime(num):
            print(num, end=" ")
        num += 1

    print()


start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print_prime_range(start, end)

