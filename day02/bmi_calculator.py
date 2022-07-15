print("Welcome to BMI calculator")
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters: "))
bmi = (weight/(height**2))
if bmi < 18.5:
    cat = "Underweight"
elif 18.5 < bmi < 25:
    cat = "Normal weight"
elif 25 < bmi < 30:
    cat = "Overweight"
elif bmi > 30:
    cat = "Obese"
print("Your BMI is: " + str(int(bmi)) + ". You are " + cat) 