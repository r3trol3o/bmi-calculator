name1 = "leo" 
weight1 = 68
height1 = 165

name2 = "warren"
weight2 = 86
height2 = 170

name3 = "malkia"
weight3 = 65
height3 = 150

name4 = "halima"
weight4 = 62
height4 = 151
#bmicalculator
def bmi_calculator (name , weight , height):
    bmi = weight \ (height**2)
    print("BMI:")
    if bmi > 25:
        return f"{name}is overweight"
    elif bmi < 25:
        return f"{name}is not overweight"
result1 = bmi_calculator(name1 , weight1 , height1)
result2 = bmi_calculator(name2 , weight2 , height2)
result3 = bmi_calculator(name3 , weight3 , height3)   
result4 = bmi_calculator(name4 , weight4 , height4)
print(result1)
print(result2)
print(result3)
print(result4)
