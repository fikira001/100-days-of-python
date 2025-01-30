print("Welcome to tip calculator !!!!")

bill = float(input("Enter Total Bill: $"))

tip = float(input("Tip in Percentage 12, 13, 14, or 15: "))

people = float(input("How many people are splitting the bill: "))

#Tip Amount to be added to the main bill
tip_percent = (bill*tip)/100

total =  bill + tip_percent

#What each person will while splitting the bill 
person = round (total/people,2)

print (f"Each person should pay ${person}")