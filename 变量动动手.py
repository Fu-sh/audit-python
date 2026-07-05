def power(x,y):
    return x**+y
print(power(3,3))
def 最大公约数(a,b):
    while b != 0:
        a,b = b, a % b
    return a
print(最大公约数(47,12))
def 十进制转换二进制(num):
    if num == 0:
        return "0"
    elif num < 0:
        return "请输入一个非负整数"
    else:
        binary = ""
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        return binary
# 学习了怎么创造函数，怎么添加参数,怎么定义函数,以及函数很便利和DRY    
    
