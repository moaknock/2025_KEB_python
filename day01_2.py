#dan = input("Input dan: ")

#dan = int(input("Input dan: "))
#for i in range(1,10,1):
#    print(f"{dan}*{i} = {dan * i}")
#print(2**10) #1024
#print(16**0.5) # 4.0
#n = int(input("Input number : "))
#is_prime = True
def is_prime(num) -> bool:
    """
    The Function that returns True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
    #count = 0
    # for i in range(2, n):
        for i in range(2,int(n**0.5)+1):
             if num % i == 0:
                return False
        #is_prime = False #count = count + 1
        #break
        # print(i, end=' ')
    else:
        return False
    return True
    #is_prime = False

#if count == 0:
if is_prime:
    print("f{n} is prime number")
else:
    print("f{n} is NOT prime number!")


#for dan in range(2,10,1): #2단부터 시작, 10 앞 까지 실행, 1씩 추가
#    for i in range(1,10,1):
#       print(f"{dan}*{i} = {dan * i}")

help(is_prime)
n = int(input("Input number : "))