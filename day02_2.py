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

    i = 2  # while문에서 사용할 변수 초기화
    while i <= int(pow(number, 0.5)):  # pow() 함수 사용
        if number % i == 0:
            return False
        i += 1  # 다음 숫자로 증가

    return True


# 구간 소수 출력 함수
def print_prime_range(start, end):
    """
    Prints all prime numbers in the given range [start, end]
    :param start: starting number
    :param end: ending number
    """
    print(f"Prime numbers between {start} and {end}:")

    num = start  # 시작 숫자
    while num <= end:  # num이 end 이하일 때 반복
        if is_prime(num):  # 소수인지 확인
            print(num, end=" ")  # 한 줄로 출력
        num += 1  # 다음 숫자로 증가

    print()  # 줄 바꿈


# main
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print_prime_range(start, end)

