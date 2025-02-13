#Assignment
#v0.1) 다음 코드에서 딕셔너리를 제거하고 리스트만 사용하여 동일하게 동작하도록 코드를 수정하시오.
# 리스트를 2개 만들어라 술 1개 안주 1개

import random

drinks = ["위스키", "와인", "소주", "고량주"]
foods = ["초콜릿", "삼겹살", "양꼬치", "낙곱새"]
price = [50000,30000,5000,7500]
amounts = [0 for i in range(len(drinks))]

drinks.append("사케")
foods.append("광어회")
price.append(25000)
amounts.append(0)
foods[0] = "피자"

# amounts = list()
# for i in range(len(drinks)):
#     amounts.append(0)
total_price = 0

def print_menu_total_price(n):
    global total_price
    print(f"{drinks[n]}에 어울리는 안주는 {foods[n]}입니다.")
    print(f"가격: {price[n]}")
    amounts[n] = amounts[n] + 1
    total_price = total_price + price[n]


# 메뉴 리스트 생성
menu_list = "다음 술 중에 고르시오.\n"
for i in range(len(drinks)):
    menu_list += f"{i+1}) {drinks[i]}\n"
menu_list += f"{len(drinks)+1}) 아무거나\n{len(drinks)+2}) 종료: "

while True:
    menu = input(menu_list)  # 메뉴 입력받기
    if menu.isdigit():  # 숫자인지 확인
        menu = int(menu)  # 정수형으로 변환

        if 1 <= menu <= len(drinks):
            print_menu_total_price(menu - 1)  # 선택한 술의 안주 출력
        elif menu == len(drinks) + 1:
            random_index = random.randint(0, len(drinks) - 1)
            print(f"{drinks[random_index]}에 어울리는 안주는 {foods[random_index]}입니다.")
        elif menu == len(drinks) + 2:
            print("다음에 또 오세요!")
            break

    for k in range(len(drinks)):
        if amounts[k] != 0:
            print(f" 주류명: {drinks[k]} 수량: {amounts[k]} 단가: {price[k]} 가격: {price[k] * amounts[k]}")
            print(f"총 금액: {total_price}원")
    # else:
    #     print("올바른 번호를 입력하세요.")



    # while True:
    #     menu = input(menu_list)
    #     if menu == '1':
    #        print_menu(int(menu)-1)
    #     elif menu == '2':
    #         print_menu(int(menu) - 1)
    #     elif menu == '3':
    #         print_menu(int(menu) - 1)
    #     elif menu == '4':
    #         print_menu(int(menu) - 1)
    #     elif menu == '5':
    #         print_menu(int(menu) - 1)
    #     elif menu == '6':
    #         random_index = random.randint(0,len(drinks)-1)
    #         print(f'{random_index}에 어울리는 안주는 {foods[random_index]} 입니다')
    #     elif menu == '7':
    #         print(f'다음에 또 오세요')
    #         break

# while True:
#     # 메뉴 출력
#     print("\n다음 술 중에 고르세요.")
#     for i in range(len(drinks)):
#         print(f"{i+1}) {drinks[i]}")
#
#     menu = input("6) 아무거나   7) 종료 : ")
#
#     if menu in["1","2","3","4","5"]:
#         idx = int(menu) - 1
#         print(f"{drinks[idx]}에 어울리는 안주는 {foods[idx]}입니다.")
#     elif menu == "6" :
#         idx = random.randint(0,len(drinks)-1)
#     elif menu == "7":
#         print("다음에 또 오세요")
#         break


# while True:
#     menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods_keys[0]}   2) {drinks_foods_keys[1]}   3) {drinks_foods_keys[2]}   4) {drinks_foods_keys[3]}   5) {drinks_foods_keys[4]}   6) 아무거나   7) 종료 : ')
#     if menu == '1':
#         print(f'{drinks_foods_keys[0]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[0]]} 입니다')
#     elif menu == '2':
#         print(f'{drinks_foods_keys[1]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[1]]} 입니다')
#     elif menu == '3':
#         print(f'{drinks_foods_keys[2]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[2]]} 입니다')
#     elif menu == '4':
#         print(f'{drinks_foods_keys[3]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[3]]} 입니다')
#     elif menu == '5':
#         print(f'{drinks_foods_keys[4]}에 어울리는 안주는 {drinks_foods[drinks_foods_keys[4]]} 입니다')
#     elif menu == '6':
#         random_drink = random.choice(drinks_foods_keys)
#         print(f'{random_drink}에 어울리는 안주는 {drinks_foods[random_drink]} 입니다')
#     elif menu == '7':
#         print(f'다음에 또 오세요')
#         break