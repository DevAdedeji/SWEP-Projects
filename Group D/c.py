test_list = [6.2, 12.3, 5.0, 18.8, 7.1, 12.8]
print("The original list is:" + str(test_list))
temp = 1
temp2 = float(temp**(1/len(test_list)))
result = float(temp2)
print("The geometric average of the list is: " + str(result))
#Calculating the arithmetic Average
count = 0
for i in test_list:
    count += i
arithmetic_avg = count / len(test_list)
print("The arithmetic average of " +str(test_list) + " is " +str(arithmetic_avg))
if( arithmetic_avg > result):
    print("The arithmetic average of " + str(test_list) + " is greater than the geometric average")
else:
    print("The geometric average of " + str(test_list) + " is greater than the arithmetic average")

