import time
import csv
from plyer import notification
import pyttsx3
import csv

with open("today.csv","r") as file:
    todayreader = csv.reader(file)
    next(todayreader)
        
    info = next(todayreader)

    title = info[0]
    message = info[1]

    notification.notify(
        title = title,
        message = message,
        timeout = 25
    )

    print("Notification runs.")


    text_speech = pyttsx3.init()
    text_speech.say(message)
    text_speech.runAndWait()

def delete(filename):

    file = open(filename,'r')
    csvreader = csv.reader(file)

    rewrite = []

    header = next(csvreader)
    next(csvreader)

    for row in csvreader:
        rewrite.append(row)


    with open(filename,'w',newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerows(rewrite)

delete('record.csv')
delete('today.csv')

