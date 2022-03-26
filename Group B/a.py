import math
num = int(input("Enter the number: "))
#Program to check if the number is a prime number
def isPrimeNumber(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if(num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number") 

#program to check if the number is a fibonacci number
#Aprogram that retuns true if x is a perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    #n is a fibonacci if one of 5*n*n+4 or 5*n*n-4 or both is a perfect square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

for i in range(0, num+1):
    isPrimeNumber(num)
    if(isFibonacci(num) == True):
        print(num, "is a fibonacci number")
    else:
        print(num, "is not a fibonacci number")
    num -= 1

