"""
We Want to Send Automated Email using python by adding attachment(file)
"""
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
#same include mail with subject code
list=["22311a05n3@cse.sreenidhi.edu.in","bandarichintu329@gmail.com","harishkavati01@gmail.com"]
for To in list:
    From='kasarlasaikiran002@gmail.com'
    Subject="Email Automation with attachment"
    app_password="sxlk uqbw yvgm zcqe"
    body="IN this project we will uderstand how python can be usefull in real world applications"
    attach ="simplemail.py"
    msg=MIMEMultipart()
    msg['From']=From
    msg["To"]=To
    msg["Subject"]=Subject
    msg.attach(MIMEText(body))
    part=MIMEBase('application','octet-stream')
    part.set_payload(open(attach,'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment ; filename="%s" '%(os.path.basename(attach))) 
    msg.attach(part)
    text=msg.as_string(part)
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(From,app_password)
    server.sendmail(From,To,text)
print("Success")
server.quit()
