# 🚀 BMI Calculator with User Input

def bmi_calculator(name, weight, height):
    # Convert height from cm to meters
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)

    print(f"\n{name}'s BMI is: {round(bmi, 2)}")

    if bmi > 25:
        return f"{name} is overweight 😬"
    elif bmi < 18.5:
        return f"{name} is underweight 😟"
    else:
        return f"{name} has a healthy weight 💪"

# 📝 How many people do you want to check?
num_people = int(input("How many people do you want to check? "))

for i in range(num_people):
    print(f"\n--- Person {i+1} ---")
    name = input("Enter name: ")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in cm: "))

    result = bmi_calculator(name, weight, height)
    print(result)
