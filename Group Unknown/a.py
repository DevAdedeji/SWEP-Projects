num_list = []
for i in range(1,21):
    num = int(input("Enter number"+str(i) +": "))
    num_list.append(num)

#Sort the numbers in ascending order
num_list.sort()
print("The number in ascending order: ")
print(num_list)

#Sort the number in descending order
num_list.sort(reverse=True)
print("The number in descending order: ")
print(num_list)









