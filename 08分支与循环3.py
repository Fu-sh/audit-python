favourite = "张云娇"
for i in favourite:
    print(i,end=" ")
dead = ["侯小双","钱立","张伦峰","朱俊鹏","杨景怡"]
for T in dead:
    print(T,len(T))
range(5)
print( range(5) )
for N in range(0,5):
    print(N)
for B in range(0,20,2):
    print(B)    
for C in range(10):
    if C%2!=0:
        print(C)
        continue
    C+=2
    print(C)