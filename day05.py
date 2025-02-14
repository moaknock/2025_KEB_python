def fibonacci_recursion(n) -> int:
    """
    피보나치 수 계산함수(재귀함수 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

print(fibonacci_recursion(int(input())))
