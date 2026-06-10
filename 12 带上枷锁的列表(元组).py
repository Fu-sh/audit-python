tuple1 = (1,2,3,4,5,6,7) # 元组标志性符号为,号，当然如果你要一个空元组就只要()
print(tuple1[0])
print(type(tuple1)) #用于检测类型
tuple1 = tuple1[:6] + (8,) #创造一个新的元组来实现添加效果
print(tuple1)
del tuple1
print(tuple1) 