import subprocess
import smtplib
import sys
try:
    p1=subprocess.run(['systemctl','status','nginx'],capture_output=True, text=True)
    str=p1.stdout
    result=str.find('running')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("vasandanipiyush@gmail.com", "apcsccphtjkvmnax")
    message = "nginx is not well kindly check"
    message1="Everything is fine"
    if result==-1:
        s.sendmail("vasandanipiyush@gmail.com", "piyush.vasandani@easygov.co.in", message)
    else:
        s.sendmail("vasandanipiyush@gmail.com", "piyush.vasandani@easygov.co.in", message1)
except:
    print("some error occured")
    sys.exit(1)
