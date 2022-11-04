import os
import shutil
import smtplib
import psutil
​
def fun(message):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("rahulgangwar95363@gmail.com", "tttviguefqjlgxab")
    s.sendmail("rahulgangwar95363@gmail.com", "piyush.vasandani@easygov.co.in", message)
    s.quit()
​
​
path = '/'
memory = shutil.disk_usage(path)
total=memory.total
available=memory.free
used=memory.used
count=(used/total)*100
if count>90:
    message1="Greeting of the day \n WARNING \n your Disk usage is more than 90%"
    fun(message1)
elif count>80:
    message2="Greeting of the day \n ALERT \n your Disk usage is more than 80%"
    fun(message2)
cpu_util=psutil.cpu_percent(4)
if cpu_util>90:
    message3="Greeting of the day \n WARNING \n your CPU usage is more than 90%"
    fun(message3)
elif cpu_util>80:
    message4="Greeting of the day \n ALERT \n your CPU usage is more than 80%"
    fun(message4)
