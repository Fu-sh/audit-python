# 分数评分
temp = int(input("请输入您的分数"))
if (temp>100) or (temp<0):
    print("请输入正确成绩")
elif temp >= 90:
    print("A") 
elif 90 > temp >= 80:
    print("B")
elif 80 > temp >= 60:
    print("C") 
else:
    print("D")
# 用三元操作符重写一段代码
x,y,z = 6,5,4
small = x if x < y else y
small = small if small < z else z
print(small)
