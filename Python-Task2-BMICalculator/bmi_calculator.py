print("BMI Calculator")

weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

height_m = height_cm / 100

bmi = weight / (height_m * height_m)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")
