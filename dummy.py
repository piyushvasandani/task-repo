import subprocess
from datetime import datetime, timedelta
from datetime import date
from datetime import timedelta
today = date.today()
d1 = today.strftime("%m-%d-%Y")
print(d1)
import re
import sys
import random
import crypt
import smtplib
user=sys.argv[1]
str1="Password expires"
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
print(str)
str = datetime.strptime(str, "%b %d %Y") #string to date
end = str - timedelta(days=5) # date - days
end =end.date()
print(end)

