print("**BMI calculator welcomes you, kindly only enter numbers without units**")
weight = float(input("Enter your weight in kilograms (example: 45): "))
height = float(input("Enter your height in centimeters (example: 175): "))
age = int(input("Mention your age: ")) 

def bmi_cal(kg, cm, yrs):
    height_in_meters = cm / 100  
    bmi = kg / (height_in_meters ** 2) 
    print(f"For a {yrs} year old, your BMI is {bmi:.1f}")
    return bmi  

def category(bmi):
    " Analysing Health Category based on BMI. "
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal weight"
    elif 25 <= bmi < 30:
        return "overweight"
    else:
        return "obesity"


bmi_value = bmi_cal(weight, height, age)
health_status = category(bmi_value)
print("Health Category is:", health_status)
