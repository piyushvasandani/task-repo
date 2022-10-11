import re
import sys
import random
import crypt
import smtplib
import subprocess
from datetime import datetime, timedelta
from datetime import date
from datetime import timedelta
today = date.today()
today_date = today.strftime("%Y-%m-%d")
user=sys.argv[1]
def mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("vasandanipiyush@gmail.com", "apcsccphtjkvmnax")
    s.sendmail("vasandanipiyush@gmail.com", "piyush.vasandani@easygov.co.in", message)

p1=subprocess.run(['sudo','chage','-l',user],capture_output=True, text=True)
str=p1.stdout
for line in str.splitlines():
    if(re.search("Password expires",line)):
            str=line
            break
result=str.find(':')
result+=2
str=str[result:]
str=str.replace(",","")
str = datetime.strptime(str, "%b %d %Y") #string to date
end = str - timedelta(days=5) # date - days
end =end.date()
end=end.strftime('%Y-%m-%d')

end1=str - timedelta(days=4)
end1= end1.date()
end1=end1.strftime('%Y-%m-%d')

end2 = str - timedelta(days=3) # date - days
end2 =end2.date()
end2=end2.strftime('%Y-%m-%d')



if today_date==end or today_date==end1 :
    message = "kindly change your password"
    mail(message) 
    print("mail sent for warning")
elif today_date==end2:
    message="your password has been changed"
    NumberCase="0123456789"
    UpperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LowerCase="abcdefghijklmnopqrstuvwxyz"
    SpecialCase="#@$%^&*=!"
    type1=''.join(random.choice(NumberCase) for i in range(4))
    type2=''.join(random.choice(UpperCase) for i in range(4))
    type3=''.join(random.choice(LowerCase) for i in range(4))
    type4=''.join(random.choice(SpecialCase) for i in range(4))
    newpasswd=type1+type2+type3+type4
    newpasswd=''.join(random.sample(newpasswd,len(newpasswd)))
    enc_passwd=crypt.crypt(newpasswd,"22")
    try:
        subprocess.run(['usermod','-p',enc_passwd,user])
        message = f"Greeting of the day {user},your password has been changed and your new password is {newpasswd} \n kindly use this password for future work"
        mail(message)
        print("password updated successfully and mail sent")
    except:
        print("error some error occured")
        sys.exit()
