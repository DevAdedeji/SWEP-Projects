#A program to calculate the amount of money in dollars in a piggy bank
#Note: The amount follow the order of [half dollars, quarters, dimes, nickels, pennies]
# halfDollars = float(input("Enter the number of half dollars: "))
# quarters = float(input("Enter the number of half quarters: "))
# dimes = float(input("Enter the number of half dimes: "))
# nickels = float(input("Enter the number of half nickels: "))
# pennies = float(input("Enter the number of half pennies: "))
def moneyDollar(dollar_halfDollars, dollar_quarters, dollar_dimes, dollar_nickels, dollar_pennies):
    dollar_halfDollars = dollar_halfDollars / 2
    dollar_quarters = dollar_quarters / 4
    dollar_dimes = dollar_dimes / 10
    dollar_nickels = dollar_nickels / 20
    dollar_pennies = dollar_pennies / 100
    #Calculating the total amount in Dollars
    total_amount = dollar_halfDollars + dollar_quarters + dollar_dimes + dollar_nickels + dollar_pennies 
    #Printing the toal amount
    print("The total amount in dollars is $" + str(total_amount))

# moneyDollar(halfDollars, quarters, dimes, nickels, pennies)

#Created an emptly list that will contain all the money
money_in_piggybank = [11, 7, 3, 12, 17]

moneyDollar(money_in_piggybank[0], money_in_piggybank[1], money_in_piggybank[2], money_in_piggybank[3],money_in_piggybank[4])

