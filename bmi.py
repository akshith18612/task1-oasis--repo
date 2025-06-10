height=float(input("enter your height:"))
weight=float(input("enter your weight:"))
BMI=round(weight/height**2)
if BMI<16.0:
    print("you are under weight(severe thinness) ")
elif BMI>=16.0 and BMI<=16.9:
    print("you are under weight(moderate thinness) ")
elif BMI>=17.0 and BMI<=18.4 :
    print("you are under weight(mild thinness) ")
elif BMI>=18.5 and BMI<=24.9 :
    print("you are in noraml range")
elif BMI>=25.0 and BMI<=29.9 :
    print("you are overweight(pre-obese) ")
elif BMI>=30.0 and BMI<=34.9 :
    print("you are  in obese case-1 ")
elif BMI>=35.0 and BMI<=39.9 :
    print("you are  in obese case-2 ")
elif BMI>=40.0 :
    print("you are in obese case-3 ")
