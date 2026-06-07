temp = input("请输入你的分数：")
score = int(temp)
if score < 0 or score > 100:
        print("输入错误！")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")
    
