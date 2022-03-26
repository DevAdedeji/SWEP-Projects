# A program that accepts two currencies from users and convert the second currencies amount to the equivalent of the first currencies

#Function to convert the second currency to pounds
def convertPounds(first_currency, second_currency, second_currency_amount):  
    if second_currency.lower() == 'dollars' or second_currency.lower() == 'dollar':
        amount = (second_currency_amount / 1.4) * 0.65
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'guilders' or second_currency.lower() == 'guilder':
        amount = (second_currency_amount / 1.7) * 0.65
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'french francs' or second_currency.lower() == 'french franc':
        amount = (second_currency_amount / 5.3) * 0.65
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'marks' or second_currency.lower() == 'mark':
        amount = (second_currency_amount / 1.5) * 0.65
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'liras' or second_currency.lower() == 'lira':
        amount = (second_currency_amount / 1570) * 0.65
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'yens' or second_currency.lower() == 'yen':
        amount = (second_currency_amount / 98) * 0.65
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'pesos':
        amount = (second_currency_amount / 3.4) * 0.65
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'swiss francs' or second_currency.lower() == 'swiss franc':
        amount = (second_currency_amount / 1.3) * 0.65
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    else:
        print(f'{second_currency_amount} {second_currency}')

#Function to convert the second currency to Canadian Dollar
def convertDollar(first_currency, second_currency, second_currency_amount):  
    if second_currency.lower() == 'pounds' or second_currency.lower() == 'pound':
        amount = (second_currency_amount / 0.65) * 1.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'guilders' or second_currency.lower() == 'guilder':
        amount = (second_currency_amount / 1.7) * 1.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'french francs' or second_currency.lower() == 'french franc':
        amount = (second_currency_amount / 5.3) * 1.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'marks' or second_currency.lower() == 'mark':
        amount = (second_currency_amount / 1.5) * 1.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'liras' or second_currency.lower() == 'lira':
        amount = (second_currency_amount / 1570) * 1.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'yens' or second_currency.lower() == 'yen':
        amount = (second_currency_amount / 98) * 1.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'pesos':
        amount = (second_currency_amount / 3.4) * 1.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'swiss francs' or second_currency.lower() == 'swiss franc':
        amount = (second_currency_amount / 1.3) * 1.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    else:
        print(f'{second_currency_amount} {second_currency}')

#Function to convert the second currency to Dutch Guilder
def convertGuilder(first_currency, second_currency, second_currency_amount):  
    if second_currency.lower() == 'pounds' or second_currency.lower() == 'pound':
        amount = (second_currency_amount / 0.65) * 1.7
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'dollars' or second_currency.lower() == 'dollar':
        amount = (second_currency_amount / 1.4) * 1.7
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'french francs' or second_currency.lower() == 'french franc':
        amount = (second_currency_amount / 5.3) * 1.7
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'marks' or second_currency.lower() == 'mark':
        amount = (second_currency_amount / 1.5) * 1.7
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'liras' or second_currency.lower() == 'lira':
        amount = (second_currency_amount / 1570) * 1.7
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'yens' or second_currency.lower() == 'yen':
        amount = (second_currency_amount / 98) * 1.7
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'pesos':
        amount = (second_currency_amount / 3.4) * 1.7
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'swiss francs' or second_currency.lower() == 'swiss franc':
        amount = (second_currency_amount / 1.3) * 1.7
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    else:
        print(f'{second_currency_amount} {second_currency}')

#Function to convert the second currency to French Franc
def convertFrenchFranc(first_currency, second_currency, second_currency_amount):  
    if second_currency.lower() == 'pounds' or second_currency.lower() == 'pound':
        amount = (second_currency_amount / 0.65) * 5.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'dollars' or second_currency.lower() == 'dollar':
        amount = (second_currency_amount / 1.4) * 5.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'guilders' or second_currency.lower() == 'guilder':
        amount = (second_currency_amount / 1.7) * 5.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'marks' or second_currency.lower() == 'mark':
        amount = (second_currency_amount / 1.5) * 5.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'liras' or second_currency.lower() == 'lira':
        amount = (second_currency_amount / 1570) * 5.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'yens' or second_currency.lower() == 'yen':
        amount = (second_currency_amount / 98) * 5.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'pesos':
        amount = (second_currency_amount / 3.4) * 5.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'swiss francs' or second_currency.lower() == 'swiss franc':
        amount = (second_currency_amount / 1.3) * 5.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    else:
        print(f'{second_currency_amount} {second_currency}')

#Function to convert the second currency to German Marks
def convertMark(first_currency, second_currency, second_currency_amount):  
    if second_currency.lower() == 'pounds' or second_currency.lower() == 'pound':
        amount = (second_currency_amount / 0.65) * 1.5
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'dollars' or second_currency.lower() == 'dollar':
        amount = (second_currency_amount / 1.4) * 1.5
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'french francs' or second_currency.lower() == 'french franc':
        amount = (second_currency_amount / 1.5) * 1.5
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'guilders' or second_currency.lower() == 'guilder':
        amount = (second_currency_amount / 1.7) * 1.5
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'liras' or second_currency.lower() == 'lira':
        amount = (second_currency_amount / 1570) * 1.5
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'yens' or second_currency.lower() == 'yen':
        amount = (second_currency_amount / 98) * 1.5
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'pesos':
        amount = (second_currency_amount / 3.4) * 1.5
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'swiss francs' or second_currency.lower() == 'swiss franc':
        amount = (second_currency_amount / 1.3) * 1.5
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    else:
        print(f'{second_currency_amount} {second_currency}')

#Function to convert the second currency to Italian Lira
def convertLira(first_currency, second_currency, second_currency_amount):  
    if second_currency.lower() == 'pounds' or second_currency.lower() == 'pound':
        amount = (second_currency_amount / 0.65) * 1570
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'dollars' or second_currency.lower() == 'dollar':
        amount = (second_currency_amount / 1.4) * 1570
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'guilders' or second_currency.lower() == 'guilder':
        amount = (second_currency_amount / 1.7) * 1570
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'marks' or second_currency.lower() == 'mark':
        amount = (second_currency_amount / 1.5) * 1570
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'french francs' or second_currency.lower() == 'french franc':
        amount = (second_currency_amount / 5.3) * 1570
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'yens' or second_currency.lower() == 'yen':
        amount = (second_currency_amount / 98) * 1570
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'pesos':
        amount = (second_currency_amount / 3.4) * 1570
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'swiss francs' or second_currency.lower() == 'swiss franc':
        amount = (second_currency_amount / 1.3) * 1570
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    else:
        print(f'{second_currency_amount} {second_currency}')

#Function to convert the second currency to Japanese Yen
def convertYen(first_currency, second_currency, second_currency_amount):  
    if second_currency.lower() == 'pounds' or second_currency.lower() == 'pound':
        amount = (second_currency_amount / 0.65) * 98
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'dollars' or second_currency.lower() == 'dollar':
        amount = (second_currency_amount / 1.4) * 98
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'guilders' or second_currency.lower() == 'guilder':
        amount = (second_currency_amount / 1.7) * 98
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'marks' or second_currency.lower() == 'mark':
        amount = (second_currency_amount / 1.5) * 98
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'french francs' or second_currency.lower() == 'french franc':
        amount = (second_currency_amount / 5.3) * 98
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'liras' or second_currency.lower() == 'lira':
        amount = (second_currency_amount / 1570) * 98
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'pesos':
        amount = (second_currency_amount / 3.4) * 98
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'swiss francs' or second_currency.lower() == 'swiss franc':
        amount = (second_currency_amount / 1.3) * 98
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    else:
        print(f'{second_currency_amount} {second_currency}')

#Function to convert the second currency to Mexican Pesos
def convertPesos(first_currency, second_currency, second_currency_amount):  
    if second_currency.lower() == 'pounds' or second_currency.lower() == 'pound':
        amount = (second_currency_amount / 0.65) * 3.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'dollars' or second_currency.lower() == 'dollar':
        amount = (second_currency_amount / 1.4) * 3.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'guilders' or second_currency.lower() == 'guilder':
        amount = (second_currency_amount / 1.7) * 3.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'marks' or second_currency.lower() == 'mark':
        amount = (second_currency_amount / 1.5) * 3.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'french francs' or second_currency.lower() == 'french franc':
        amount = (second_currency_amount / 5.3) * 3.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'liras' or second_currency.lower() == 'lira':
        amount = (second_currency_amount / 1570) * 3.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'yens' or second_currency.lower() == 'yen':
        amount = (second_currency_amount / 98) * 3.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'swiss francs' or second_currency.lower() == 'swiss franc':
        amount = (second_currency_amount / 1.3) * 3.4
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    else:
        print(f'{second_currency_amount} {second_currency}')

#Function to convert the second currency to Swiss Francs
def convertSwissFrancs(first_currency, second_currency, second_currency_amount):  
    if second_currency.lower() == 'pounds' or second_currency.lower() == 'pound':
        amount = (second_currency_amount / 0.65) * 1.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'dollars' or second_currency.lower() == 'dollar':
        amount = (second_currency_amount / 1.4) * 1.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'guilders' or second_currency.lower() == 'guilder':
        amount = (second_currency_amount / 1.7) * 1.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'marks' or second_currency.lower() == 'mark':
        amount = (second_currency_amount / 1.5) * 1.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'french francs' or second_currency.lower() == 'french franc':
        amount = (second_currency_amount / 5.3) * 1.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'liras' or second_currency.lower() == 'lira':
        amount = (second_currency_amount / 1570) * 1.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'yens' or second_currency.lower() == 'yen':
        amount = (second_currency_amount / 98) * 1.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    elif second_currency.lower() == 'pesos':
        amount = (second_currency_amount / 3.4) * 1.3
        print(f'The amount of {second_currency_amount} in {first_currency} is {amount} {first_currency}')
    else:
        print(f'{second_currency_amount} {second_currency}')


def converter():
    first_currency = input("Enter the name of the first currency: ")
    second_currency = input("Enter the name of the second currency: ")
    second_currency_amount = float(input(f'Enter the amount of {second_currency}: '))
    if first_currency.lower() == 'pound' or first_currency.lower() == 'pounds':
        convertPounds(first_currency, second_currency, second_currency_amount)
    elif first_currency.lower() == 'dollar' or first_currency.lower() == 'dollars':
        convertDollar(first_currency, second_currency, second_currency_amount)
    elif first_currency.lower() == 'guilder' or first_currency.lower() == 'guilders':
        convertGuilder(first_currency, second_currency, second_currency_amount)
    elif first_currency.lower() == 'french franc' or first_currency.lower() == 'french francs':
        convertFrenchFranc(first_currency, second_currency, second_currency_amount)
    elif first_currency.lower() == 'mark' or first_currency.lower() == 'marks':
        convertMark(first_currency, second_currency, second_currency_amount)
    elif first_currency.lower() == 'lira' or first_currency.lower() == 'liras':
        convertLira(first_currency, second_currency, second_currency_amount)
    elif first_currency.lower() == 'yen' or first_currency.lower() == 'yens':
        convertYen(first_currency, second_currency, second_currency_amount)
    elif first_currency.lower() == 'pesos' or first_currency.lower() == 'peso':
        convertPesos(first_currency, second_currency, second_currency_amount)
    elif first_currency.lower() == 'swiss franc' or first_currency.lower() == 'swiss francs':
        convertSwissFrancs(first_currency, second_currency, second_currency_amount)
    else:
        print("Cant be converted")

run = input("Do you want to run the converter (Enter true/false)?: ")

while run.lower() != 'false':
    converter()
    run = input("Do you want to run the converter (Enter true/false)?: ")

