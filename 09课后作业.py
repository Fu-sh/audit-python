# 可输入三次密码，若输入中含*，不计入次数
key = 19780418
count = 0
while True:
    temp = input("请输入密码")
    if "*" in temp:
        print("检测到索引，本次不计入次数")
        continue
    if int(temp) == key:
        print("密码正确")
        break
    else:
        print("密码错误")
        count += 1
    if count >= 3:
        print("次数耗尽，账户已冻结")
        break    
    