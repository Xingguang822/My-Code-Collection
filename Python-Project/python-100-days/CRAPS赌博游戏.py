import random
money=1000
while money>0:
    print("你目前有",money,"元")
    while True:
        bet = int(input("请下注："))
        if 0<bet <= money:
            break
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print("第一次点数为", first_point)
    if first_point == 7 or first_point == 11:
        money += bet
        print("你赢得了", bet * 2, "元！")
    elif first_point == 2 or first_point == 3 or first_point == 12:
        money -= bet
        print("你输掉了", bet, "元！")
    else:
        while True:
            second_point = random.randrange(1, 7) + random.randrange(1, 7)
            print("第二次点数为", second_point)
            if second_point == 7:
                money -= bet
                print("你输掉了", bet, "元！")
                break
            elif second_point == first_point:
                money += bet
                print("你赢得了", bet * 2, "元！")
                break
print("game over!")

