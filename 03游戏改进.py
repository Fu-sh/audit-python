import random
number=random.randint(1,10)
count=0
while True:
    guess=int(input("请输入一个数字："))
    if guess==number:
        print("恭喜你，猜对了！奖励你可以重新运行程序玩一次")
        break
    elif guess<number:
        print("你猜的数字太小了，请再试一次。")
    else:
        print("你猜的数字太大了，请再试一次。")
    count+=1
    if count>=3:
        print("很遗憾，你已经猜了三次了，游戏结束！")
        break

