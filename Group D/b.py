# num_numbers = int(input("How many numbers? "))


# for i in range(1, num_numbers + 1):
#     num = float(input(f'Input the number{i}: '))
#     arr.append(num)


arr = [6.2, 12.3, 5.0, 18.8, 7.1, 12.8]
#Fucntion to find the cumulative product of a list of numbers
def product(list):
    p = 1
    for i in list:
        p *= i
    print("The cumulative product of the list is: " + str(p))

c = product(arr)