#0.06, 0.08, 0.08, 0.1, 0.1, 0.1, 0.12, 0.12, 0.12, 0.12 27.5, 13.4, 53.8, 29.2, 74.5, 87.0, 39.9, 47.7, 8.1, 63.2
#


# def getNumbers(f,x):
#     for i in range(1, num_numbers + 1):
#         num1 = float(input(f'Input the number{i} of the weighting factors: '))
#         if (num1 >= 1):
#             print("Weighting factor must be less than 1")
#             num1 = float(input(f'Input the number{i} of the weighting factors: '))
#         else:
#             pass
#         num2 = float(input(f'Input the corresponding value of x for the weighting factor: '))
#         f.append(num1)
#         x.append(num2)
#     print(f)
#     print(x)

#     if(sum(f) < 1 or sum(f) > 1):
#         print("The sum of the weighting factors must be equals to 1")
#         getNumbers(f,x)
#     else:
#         pass
f = [0.06, 0.08, 0.08, 0.1, 0.1, 0.1, 0.12, 0.12, 0.12, 0.12 ]
x =  [27.5, 13.4, 53.8, 29.2, 74.5, 87.0, 39.9, 47.7, 8.1, 63.2]

def weighted_average(f, x):
    return sum(x * y for x, y in zip(f, x)) 

print("The weighted average of the list is",weighted_average(f, x))


