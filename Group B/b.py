#program to calculate the sum of first n odd integers 

num = int(input("Enter the number you want to calculate its first odd integers: "))
sum = 1
count = 0
temp = 1
while( count < num-1):
    temp += 2
    sum += temp
    count +=1



print("The Sum of the first", num, "odd integers is", sum)