### Excercise 1.3 | BMI (approx. 2 hours)
#Write a program that will ask the user for his height (in cm) and body weight,
# and as a result will present his BMI and recommendations. Take a look at BMI definition in wikipedia.


height = float(input('Provide your height in cm: '))
body_weight= float(input('Provide your weight in kg: '))
BMI = body_weight / (height/100) **2

print (f'Your BMI is {BMI:.1f}')

if BMI < 16.0:
    print('Category: Underweight (Severe thinness)')
elif BMI >= 16.0 and BMI < 16.9:
    print('Category: Underweight (Moderate thinness)')
elif BMI >= 17.0 and BMI < 18.4:
    print('Category: Underweight (Mild thinness)')
elif BMI >= 18.5 and BMI < 24.9:
    print('Category: Normal range')
elif BMI >= 25.0 and BMI < 29.9:
    print('Category: Overweight (Pre-obese)')
elif BMI >= 30.0 and BMI < 34.9:
    print('Category: Obese (Class I)')
elif BMI >= 35.0 and BMI < 39.9:
    print('Category: Obese (Class II)')
elif BMI >= 40.0:
    print('Category: Obese (Class III)')


