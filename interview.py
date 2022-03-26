
numbers = []


for i in range(1,1000001):
    #This will italize the third number in the series
    if(i % 3 == 0):
        i = f'<i>{i}</i>'
    #This will bold the third number in the series
    elif(i % 10 == 0):
        i = f'<b>{i}</b>'
    #This will check if the number is a prime number
    elif(i > 1):
        for j in range(2, int(i/2)+1):
            if (i % j == 0):
                pass
                break
        else:
            i = f'<u>{i}</u>'
            
    numbers.append(i)

print(numbers)