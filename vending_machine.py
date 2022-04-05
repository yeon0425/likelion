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
