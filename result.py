import smtplib, urllib.request, time, base64, requests, os, shutil, datetime
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

x=0
filename="Result.pdf"
url="http://www.mumresults.in/S18/"
c=input("Enter the course ID: ")
url=url+c+".pdf"
print("\nResult Url= "+url+"\n Time: ",end="")
from selenium import webdriver
while x is 0:
    try:
        r=urllib.request.urlopen(url)
        x=1
        print(str(datetime.datetime.now())[:22],end="")
    except Exception:
        print(str(datetime.datetime.now())[:22],end="")
        time.sleep(0.5)
        print('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b',end="",flush=True)
driver = webdriver.Chrome()
driver.get(url)

file = requests.get(url, stream=True)
with open("result.pdf", 'wb') as location:
    shutil.copyfileobj(file.raw, location)
sender = <YourEmail>
reciever = ['tusharadi25@outlook.com']
msg = MIMEMultipart()
msg['From'],msg['To'] = sender,COMMASPACE.join(reciever)
msg['Date'],msg['Subject'] = formatdate(localtime=True),"Result is out at "+str(datetime.datetime.now())[:19]
msg.attach(MIMEText("This mail is automatically generated, check "+url))
f='result.pdf'
with open(f, "rb") as fil:
    part = MIMEApplication(
        fil.read(),
        Name=basename(f)
    )
part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
msg.attach(part)

if x is 1:
    print("\nResult is out")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender,pswd)
    for r in reciever:
        server.sendmail(sender, r, msg.as_string())
        print("Email sent to "+r)
    server.close()
