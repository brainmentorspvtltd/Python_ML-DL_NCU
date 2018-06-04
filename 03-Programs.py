# Fib Series - 0 1 1 2 3 5 8 13 21

##a = 1
##b = 0
##
##while b < 100:
##    print(b, end=' ')
##    a,b = b, a+b

a = 17

for i in range(2,a):
    if a % i == 0:
        break
else:
    print("Prime Number")









