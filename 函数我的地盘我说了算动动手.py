# 第0题
def 回文联(str):
    str = str.lower() #将字符串全部转换为小写
    str = str.replace(" ","") #去掉字符串中的空格
    str1 = str[::-1] #[start:stop:step] start与stop为零,从始至终，步长为-1反转字符串.
    if str == str1:
        return ("是回文联")
    else:
        return ("不是回文联")
str = str(input("请输入你要判断的句子:"))
print(回文联(str))
# 第1题
def 数量检测(s):
    英文字母个数 = 0
    空格个数 = 0
    数字个数 = 0
    其他字符个数 = 0
    for i in s:
        if i.isalpha():
            英文字母个数 += 1
        elif i.isdigit():
            数字个数 += 1
        elif i.isspace():
            空格个数 += 1
        else:
            其他字符个数 += 1
    print(f"英文个数为{英文字母个数},数字个数为{数字个数},空格个数为{空格个数},其他字符个数{其他字符个数}")
    return
s = input("请输入:",)
print(数量检测(s))
# 第2题
#了解了局部变量用完就会被删掉,全局变量稳定(可以在函数里用global修改全局变量)。知道了如果不return函数就是白忙活