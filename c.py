# A program to convert temperature readings in Fahrenheit to Celcius using the from c = (5/9) * (F-32) where c is celcius and F is  Fahrenheit


#Create a variable to hold the temperature in Fahrenhet
# temperature = float(input("Enter the temperature in Fahrenheit: "))
# Created a function that converts the temperature in Fahrenheit to Celcius 
def tempConverter(temperature_in_fahrenheit):
    temperature_in_celcius = (5/9) * (temperature_in_fahrenheit - 32)
    print("The temperature is", temperature_in_celcius, "degrees celcius")

# tempConverter(temperature)







#Testing the program with 68, 150, 212, 0, -22, -200
list_of_temperatures_in_fahrenheit = [68, 150, 212, 0, -22, -200]
for i in list_of_temperatures_in_fahrenheit:
    tempConverter(i)



