import time
import hashlib

salt = "salt"

currentTime = time.localtime()

def formatDay(day):
    if day < 10:
        return "0" + str(day)
    return str(day)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

date = days[currentTime.tm_wday] + ", " + formatDay(currentTime.tm_mday) + " " + months[currentTime.tm_mon - 1] + " " + str(currentTime.tm_year)

datehash = hashlib.md5(date.encode('utf-8')).hexdigest()

datehashsalt = salt + datehash

password = hashlib.md5(datehashsalt.encode('utf-8')).hexdigest()

print(password)
