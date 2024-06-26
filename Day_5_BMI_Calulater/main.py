
height = float(input())

weight = int(input())


#Write your code below this line 👇
BMI = weight/(height * height)

if BMI<18.5 :
  print(f'Your BMI is {BMI}, you are underweight.')

elif BMI < 25.0 :
  print(f'Your BMI is {BMI}, you have a normal weight.')

elif BMI < 28.50752 :
  print(f'Your BMI is {BMI}, you are slightly overweight.')

elif BMI < 32.56189 :
  print(f'Your BMI is {BMI}, you are obese.')


elif BMI > 37.50000 :
  print(f'Your BMI is {BMI}, you are clinically obese.')

else:
   print('not valid input')