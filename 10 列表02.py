best=["家人","朋友","爱人"]
print(best)   
best.append("钱财") #在列表末尾添加一个元素
print(best,len(best))
best.extend(["工作"]) #在列表末尾添加一个列表中的元素
print(best,len(best))
best.insert(0,"还有自己啊傻瓜") #在列表的指定位置插入一个元素，第一个参数是位置，第二个参数是元素
print(best,len(best))
best[0]
print(best[0])
best.remove("工作") #从列表中删除第一个匹配的元素，如果没有找到该元素，则会引发 ValueError 异常。
print(best,len(best))
del best[4] #根据索引删除列表中的元素
print(best,len(best))
best.pop() #删除列表中的最后一个元素，并返回该元素的值 
print(best.pop()) #删除列表中的最后一个元素，并返回该元素的值
best[0:3] #切片，返回列表中指定范围的元素，返回一个新的列表
best2 = best[0:3] #切片，返回列表中指定范围的元素，返回一个新的列表
print(best2)