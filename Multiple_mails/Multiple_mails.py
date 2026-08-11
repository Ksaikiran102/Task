#now in this case we will use email package where we can add subject to the mail and also
#we can give to address
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#give from adress,to adress and subject
From=input("Enter your mail:")
app_password=input("Enter your mail app password(16):")
l=list(map(str,input("Enter To mails into list:").split(",")))
for To in l:
    Subject="Email Automation"
    msg=MIMEMultipart()
    msg['From']=From
    msg['To']=To
    msg['Subject']=Subject
    body="Hello,Welocome to Email Automation"
    msg.attach(MIMEText(body))
    text=msg.as_string()
    #same as previous SMTP Usage we will follow
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(From,app_password)
    server.sendmail(From,To,text)
print("Success")
server.quit()
