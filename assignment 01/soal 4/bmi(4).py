
weight = float(input('What is your weight? (Kg) '))
height = float(input('What is your height? (Mtr) '))
if height > 0 and weight > 0 :
        bmi = weight/(height*height)

        if bmi <= 18.5:
            print('Your BMI is', bmi, 'and you are underweight')

        elif 18.5 < bmi < 25:
            print('Your BMI is', bmi,'and you are normal')

        elif 25 < bmi < 30:
            print('your BMI is', bmi,' and you are overweight')

        elif bmi > 30:
            print('Your BMI is', bmi,'and you are obese')
else :
        print ("error :weight and  height should  be  positive numbers ")
     