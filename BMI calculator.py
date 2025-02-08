height = float(input("Enter your height in cm:"))
weight = float(input("Enter you weight in kg:"))
BMI = weight / (height/100)**2
print(" Your MBI is :",BMI)
if BMI <= 18.4:
    print(" You are under weight")
elif BMI <= 24.9150:
    print("You are healthy")
elif BMI <= 29.5:
    print("You are over weight") 
elif BMI <= 34.5:
    print(" You are severly over wweight") 
elif BMI <= 39.9:
    print("You are obese")
else:
    print("you are severly obese.")    