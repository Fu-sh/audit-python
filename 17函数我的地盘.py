def 计算(price,rate):
    final_price = price * rate #局部函数,如果尝试在函数内定义全局函数，会生成一个同名局部函数
    return final_price

old_price = float(input("请输入原价:")) #这里是全局变量,作用区域更大,更广
discount_rate = float(input("请输入折扣率:"))
new_price = 计算(old_price,discount_rate)#局部函数在此处运行之后便会删除 
print("折扣后的价格是:",new_price)
