def 萌芽(*a,base = 3):
    if base == 5:
        c = sum(a) * 5 #把数据加起来乘以5
    else:
        c = sum(a) * base #把数据加起来乘以3
    return c
萌芽(1,3,5,9)
print(萌芽(1,3,5,9)) # base默认为3,所以输出为54
萌芽(1,5,4,8,base = 5)
print(萌芽(1,5,4,8,base = 5)) #base为5,所以输出为90
for i in range(100,1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i) # 输出一个水仙数
def 小作业(主str,子str):
    length = len(主str)
    count = 0
    主str = 主str.lower()
    子str = 子str.lower()
    if 子str not in 主str:
        print("子串不在主串中")
    else:
        for i in range(length-1):
            if 主str[i] == 子str[0]:
                if 主str[i+1] == 子str[1]:
                    count += 1
    print("子串在主串中出现的次数为:",count)
小作业("You are very important to me, I really like you, if possible, I really really hope we have a future, but if you just can't like me, then I can only wish you happiness.","yo" )