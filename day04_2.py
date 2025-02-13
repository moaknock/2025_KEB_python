#Assignment
#v0.4) kwargs를 사용한 데코레이터 예제

# 로그 데코레이터 정의
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Function Name : {func.__name__}')
        print(f'Function Arguments: {args}')
        print(f'Function Key Arguments: {kwargs}')
        result = func(*args, **kwargs)  # 원래 함수 실행
        return result
    return wrapper  # () 제거 (호출X)

# 데코레이터 적용
@log_decorator
def greet(name, greeting="안녕하세요", age=0):
    return f"{greeting}, {name} ({age}세)"

# 함수 실행 및 출력
print(greet("인하"))
print(greet("Inha", "Hi"))
print(greet("Sub", "Hello"))
print(greet("JH", greeting="Hola"))
print(greet("IH", greeting="Konnichiwa", age=22))

