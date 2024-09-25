#Determining the BMI category
#Taking the inputs from the user
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
#calculating the BMI
Bmi = weight/(height*height)

if Bmi >= 30:
    print("Obesity")
elif Bmi >25 and Bmi <= 29:
    print("Overweight")
elif Bmi <=25 and Bmi >18.5:
    print("Normal")
else:
    print("Underweight")

#Which country belongs to which city

Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city = input("Enter a city name: ")

#checking weather the city in our list

if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")

#checking weather the two cities are in same country
firstcity = input("Enter the first city: ")
secondcity = input("Enter the second city: ")


if firstcity in Australia and secondcity in Australia:
    print("Both cities are in Australia")
elif firstcity in UAE and secondcity in UAE:
    print("Both cities are in UAE")
elif firstcity in India and secondcity in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")