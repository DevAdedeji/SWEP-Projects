#QUESTION 1
#A program that print HELLO! at the beginning of a line

print("HELLO!")


#QUESTION 2
#A program that request for name from a user and welcome them

#we assign the user input to the variable name
name = str(input("Whats your name?"))

#The print statement will skip two lines then print out the two statement
print("\n\nWelcome " + name + "\nLET'S BE FRIENDS!")


#QUESTION 3
#A program to convert temperature readings in Fahrenheit to Celcius using the from c = (5/9) * (F-32) where c is celcius and F is  Fahrenheit

#we assign the user input which is in fahrenheit and assign it to a variable  
# temperature_in_fahrenheit = float(input("Temperature in Fahrenheit: "))

# temperature_in_celcius = (5/9) * (temperature_in_fahrenheit - 32)

# print("The temperature is", temperature_in_celcius, "degrees celcius")


#Testing the program with 68, 150, 212, 0, -22, -200
list_of_temperatures_in_fahrenheit = [68, 150, 212, 0, -22, -200]
for i in list_of_temperatures_in_fahrenheit:
    temperature_in_celcius = (5/9) * (i - 32)
    print("The temperature is", temperature_in_celcius, "degrees celcius", "for", str(i)+ " degrees fahrenheit")



#QUESTION 4

#A program to calculate the amount of money in dollars in a piggy bank
#Note: The amount follow the order of [half dollars, quarters, dimes, nickels, pennies]

# dollar_halfDollars = float(input("Enter the number of half dollars: "))
# dollar_halfDollars = dollar_halfDollars / 2


# dollar_quarters = float(input("Enter the number of half quarters: "))
# dollar_quarters = dollar_quarters / 4


# dollar_dimes = float(input("Enter the number of half dimes: "))
# dollar_dimes = dollar_dimes / 10


# dollar_nickels = float(input("Enter the number of half nickels: "))
# dollar_nickels = dollar_nickels / 20


# dollar_pennies = float(input("Enter the number of half pennies: "))
# dollar_pennies = dollar_pennies / 100


#Created an emptly list that will contain all the money
money_in_piggybank = [11, 7, 3, 12, 17]

dollar_halfDollars = money_in_piggybank[0] / 2
dollar_quarters = money_in_piggybank[1] / 4
dollar_dimes = money_in_piggybank[2] / 10
dollar_nickels = money_in_piggybank[3] / 20
dollar_pennies = money_in_piggybank[4] / 100

total_amount = dollar_halfDollars + dollar_quarters + dollar_dimes + dollar_nickels + dollar_pennies 

print("The total amount in dollars is $" + str(total_amount))



#QUESTION 5

#A program to calculate the volume and area of a sphere 
#formula for volume is (4*pi*r^3)/3
#formula for area is 4*pi*r^2

# radius = float(input("Enter the value of radius: "))

# volume_of_sphere = (4 * (22/7) * (radius ** 3)) / 3
# area_of_sphere = 4 * (22/7) * (radius ** 2)

# print("The volume of the sphere is", volume_of_sphere)
# print("The area of the sphere is", area_of_sphere)

list_of_radius = [1,6,12.2, 0.2]

for i in list_of_radius:
    volume_of_sphere = (4 * (22/7) * (i ** 3)) / 3
    area_of_sphere = 4 * (22/7) * (i ** 2)
    print("When the radius is", i)
    print("The volume of the sphere is", volume_of_sphere)
    print("The area of the sphere is", area_of_sphere, "\n")

