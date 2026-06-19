密码 = str(input("请输入你的密码:"))
有数字 = any(c.isdigit() for c in 密码)
有字母 = any(c.isalpha() for c in 密码)
有特殊 = any(not c.isalnum() for c in 密码)
种类数 = sum([有数字,有字母,有特殊])
if (密码.isdigit() or 密码.isalpha()) and len(密码) <= 8:
    print("密码安全程度为低")
elif 种类数 == 2 and (8 <= len(密码) < 16):
    print("密码安全程度为中")
elif 种类数 == 3 and len(密码) >= 16 and 密码[0].isalpha():
    print("密码安全程度为高")
else:
    print("密码已经在三界之外,不在五行之中")