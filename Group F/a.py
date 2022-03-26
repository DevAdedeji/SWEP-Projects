#A program that will genrate a tble of compound interest factors fp = (1 + i/100)^n

nums = [4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 11, 12,15]
year = int(input("How many years? "))

for i in nums:
    fp = (1 + i/100)**year
    print(f'The compound interest factor is {fp} for {i}% in {year}')