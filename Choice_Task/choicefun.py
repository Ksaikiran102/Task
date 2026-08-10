def story():
    import random
    

    characters = ["A brave knight", "A clever fox", "A curious girl", "A young wizard"]
    places = ["in a magical forest", "on a distant planet", "in an old castle", "near a hidden cave"]
    events = ["found a mysterious treasure", "fought a dragon", "discovered a secret door", "saved the village"]
    endings = ["and became a hero.", "and lived happily ever after.", "and learned a valuable lesson.", "and started a new adventure."]

    story = (
        random.choice(characters) + " "
        + random.choice(places) + " "
        + random.choice(events) + " "
        + random.choice(endings)
    )

    print("Generated Story:")
    print(story)
def otpgmail():
    from random import randint
    import smtplib
    import email
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    #give from adress,to adress and subject
    From=input("Enter mail Address:")
    #From='kasarlasaikiran002@gmail.com'
    To=input('Enter To Email address:')
    pas=input("Enter 12 letter password:")
    #To="22311a05n3@cse.sreenidhi.edu.in"
    Subject=input("Enter Subject:")
    #Subject="Email Automation"
    msg=MIMEMultipart()
    msg['From']=From
    msg['To']=To
    msg['Subject']=Subject
    b=randint(1000,9999)
    c=str(b)
    m=input("Enter purpose of OTP:")
    body=m+"is :"+c
    msg.attach(MIMEText(body))
    text=msg.as_string()
    #same as previous SMTP Usage we will follow
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(From,pas)
    server.sendmail(From,To,text)
    print("Success")
    otp=int(input("Enter 4 digit Otp:"))
    if(otp==b):
        print("Login Successfull")
    else:
        print("Please Enter vaild OTP")
    server.quit()
def bmi(name,w,h,result):
            if w>0 and h>0:
                bmi=(w)/((h)**2)
                result["name"].append(name)
                result["Bmi"].append(bmi)
                if bmi<18.5:
                    print(f"{name} is Underweight{bmi}")
                elif 18.5<=bmi<=24.9:
                    print(f"{name} is NormalWeight{bmi}")
                elif 25<=bmi<=29.9:
                    print(f"{name} is Overweigth {bmi}")
                elif bmi>=30:
                    print(f"{name} is Obesity {bmi}")
            else:
                print(f"{name} Enter only +ve values")
            return result
def game():
    import random
    while True:
        player1=input('Enter the choice:').lower()
        player2=random.choice(['Rock','paper','Scissors']).lower()
        print("player2 selection:",player2)
        if player1=='rock'and player2=='paper':
            print("Player2 wins")
            break
        elif player1=='paper' and player2=='rock':
            print("player1 Wins")
            break
        elif player1=='scissors' and player2=='paper':
            print("player1 Wins")
            break
        elif player1=='paper' and player2=='scissors':
            print("player2 Wins")
            break
        elif player1=='rock' and player2=="scissors":
            print("player1 Wins")
            break
        elif player1=='scissors' and player2=='rock':
            print("player2 Wins")
            break
        elif player1 not in ['rock','paper','scissors']:
            print("please! Enter correct choice player1")
        else:
            print("tie")
