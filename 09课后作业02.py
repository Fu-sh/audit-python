# 红黄球问题
for r in range(0,4):
    for y in range(0,4):
        g = 8 - r - y
        if 0 <= g <= 6: 
            print(f"红球{r}个，黄球{y}个，绿球{g}个")