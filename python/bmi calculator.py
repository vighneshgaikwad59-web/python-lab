


# Step 1 - Get input
weight = float(input("Enter your weight (kg): "))
height_cm = float(input("Enter your height (cm): "))

# Step 2 - Convert cm to m
height_m = height_cm / 100

print("Weight:", weight, "kg")
print("Height:", height_m, "m")

# Step 3 - BMI Formula
bmi = weight / (height_m ** 2)
bmi = round(bmi, 2)

print(f"Your BMI is: {bmi}")

# BMI Category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")


# Function Version
def calculate_bmi(weight, height_cm):
    if weight <= 0 or height_cm <= 0:
        print("Invalid input")
        return

    height_m = height_cm / 100
    bmi = round(weight / (height_m ** 2), 2)

    if bmi < 18.5:
        cat = "Underweight"
    elif bmi < 25:
        cat = "Normal weight"
    elif bmi < 30:
        cat = "Overweight"
    else:
        cat = "Obese"

    print(f"BMI: {bmi} - {cat}")
    return bmi


print(calculate_bmi(70, 175))