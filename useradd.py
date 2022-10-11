import subprocess
import sys
import crypt
import smtplib
import random
user=sys.argv[1]
def mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("vasandanipiyush@gmail.com", "apcsccphtjkvmnax")
    s.sendmail("vasandanipiyush@gmail.com", "piyush.vasandani@easygov.co.in", message)
    s.quit()
def useradd(user):
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
        subprocess.run(['useradd','-p',enc_passwd,user])
        subprocess.run(['chage','-M','90',user])
        message = f"Greeting of the day {user},your password to login is  {newpasswd} \n kindly use this password for future work"
        mail(message)
        print("User added successfuly ,password has been sended on user's email")
        
    except:
        print("some error occured")
        sys.exit(1)
useradd(user)
