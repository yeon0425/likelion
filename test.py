# name="혜빈"
# age=23
# print("안녕하세요. 제 이름은 {}이고, {}살이에요.".format(name,age))
# print("안녕하세요. 제 이름은 %s이고, %d살이에요." %(name,age))

# grade = int(input("점수를 입력하세요: "))
# if (grade >= 90):
#     print("A학점입니다.")
# elif(grade >= 70):
#     print("B학점입니다.")
#     print("분발하세요!")
# else:
#     print("재수강에 당첨되었습니다")

# a=int(input("숫자 a를 입력해주세요 : "))
# b=int(input("숫자 b를 입력해주세요 : "))
# answer=int(input("a*b의 값은? : "))
# if (a*b == answer):
#     print("정답입니다!")
# else:
#     print("다시 한 번 생각해보세요.")

# color = ["red",'yellow','green']

# color.append("orange")
# color.insert(2,"grey")

# del color[1]
# x=color.pop()
# color.remove("red")
# print(color)
# print(x)

# likelion={"다윤":"컴공","도연":"컴공","혜빈":"사복"}
# x = likelion["혜빈"]
# print(x)



money= int(input("금액을 넣어주세요: "))
print("현재금액: %d 원" %money)
print("[ 이 화 네 음 료 수 ]")
ewha={"콜라":500, "커피":400, "사이다":300, "율무차":200}
goods=list(ewha.keys())
price=list(ewha.values())

while True:
    for i in range(1,5):
        print( str(i)+"."+goods[i-1]+" - "+str(price[i-1])+" 원")

    select=int(input("음료를 선택해주세요: "))-1
    exchange=money-price[select]

    if (exchange<0):
        print("금액이 부족합니다.")
        break
    elif (exchange==0):
        print("잔액은 0원입니다. 이용해주셔서 감사합니다.")
        break
    else:
        print("잔액은 %d 원입니다." %(exchange))
        money=exchange
        more=input("추가로 구매하시겠습니까? (Y/N)")
        if (more=="Y"):
            continue
        else:
            print("이용해주셔서 감사합니다.")
            break
