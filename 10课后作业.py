# 0.我选择同名列表覆盖
member = ["小甲鱼","黑夜","迷途","怡静","秋舞斜阳"]
member = ["小甲鱼",88,"黑夜",90,"迷途",85,"怡静",90,"秋舞斜阳",88]
print(member)
# 1.for打印member每个内容(加载不出图片内容，我就做最简单的了)
for i in member:
    print(i)
# 2.老问题啊论坛图片出不来,我只能自己乱整两个了
for i in member:
    print(i,end=" ")
print(*member,sep=" ")
# 3.偷懒嘿嘿