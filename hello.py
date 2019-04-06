##for j in range(3):
##    for i in range(3):
##        print('*',end='')
##     

##for i in  range(1,4):
##    for j in range (i):
##        print('*',end='')
##
##    print()

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j)+'    ',end='')
    print()
