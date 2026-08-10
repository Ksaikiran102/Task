from  choicefun import *
def fun(choice):
    if choice==1:
        print("-----------ROCK PAPER SCCISSOR GAME------------")
        game()
    elif choice==2:
        print("-----------STORY GENERATOR------------")
        story()
    elif choice ==3:
        print("-----------OTP Generator to emails------------")
        otpgmail()
    elif choice==4:
        print("-----------BMI Calculator------------")
        n=int(input("Enter numer:"))
        result={"name":[],
                    "Bmi":[]}
        for i in range(n):
                name=input("Enter name:")
                w= int(input("Enter weight:"))
                h = float(input("enter height:"))
                bmi(name,h,w,result)
        print(result)
        bmi(name,w,h,result)
    else:
        print("choice correct option")
while True:
    print("\n Choose  option")
    print("1.ROCK PAPER SCCISSOR GAME")
    print("2.STORY GENERATOR")
    print("3.OTP Generator to emails")
    print("4.BMI Calculator")
    choice=int(input("Enter Choice:"))
    if choice==0:
        print("Thank You")
        break
    if choice<0 or choice>4:
        print("Invaild")
        continue
    while True:
        fun(choice)
        print()
        print("1. Continue same Option")
        print("2. Back to Options")
        print("3. Exit")
        Option = int(input("Enter option: "))
        if Option == 1:
            continue
        elif Option == 2:
            break
        elif Option == 3:
            print("Thank You")
            exit()
        else:
            print("Invalid Option")
