list1=[1,2,3,4,5,6,7,8]
list2=[5678] #存在多个元素时,仅对比第一个元素,若第一个元素对比成立，则视为比较成立。
print(list1<list2)
list1 *= 5 #列表也可以用运算符操作，两个列表也可以相加，有类似extend的效果，但无法添加新元素.
print(list1)
list1.count(1)# 用于查询对应列表中对应元素出现的次数
list1.index(1) # 用于查询对应列表中对应元素出现的位置
list1.index(2,0,6) # 用于检索对应区间内对应元素出现的位置
list1.reverse() # 翻转对应列表中的元素的位置，末尾变为开头
print(list1)
list1.sort() # 对列表中的元素进行排序，默认从小到大，可用func等更改排序，或者如下所示
print(list1)
list1.sort(reverse=True)
print(list1)
list5 = list1[:]
print(list5)