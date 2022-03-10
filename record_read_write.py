import csv 
import os
import pandas as pd
from current_time import currenttime
def check_change(events):
    flag = 0
    if os.path.isfile('record.csv'):
        
        if not events:
            return False
        for event in events:
            flag = 0
            file = open('record.csv','r')
            csvreader = csv.reader(file)
            next(csvreader)
            time = -1
            flag2 = 0
            if event['start']['dateTime']:
                time = event['start']['dateTime'] # extractng date info from event (which is stored as  a dictionary)
                

                time = time[11:16]
                time = time.split(':')

                time = time[0] + time [1]
                time = int(time)
                # print("Inn read : ",time)
            for row in csvreader:
                if event['summary'] == row[2] or time < currenttime():
                    flag = 1
                    
                flag2 = 1
            if flag == 0 :
                return True
        
        if flag == 1 and flag2 == 1:
            print("checking flag")
            return False
    else:
        return True

def checktime(timenow):
    if os.path.exists('record.csv'):
        with open('record.csv','r') as file:
            csvreader= csv.reader(file)
            next(csvreader)
            try:
                time= next(csvreader)[1] 
            except: 
                return False
            if int(time) == timenow:
                return True
            else:
                return False
    return False    

def write(events):
    header = ['Date','Time','Summary'] # creating a header for csv file

    print('write is called')
    with open('record.csv','w',newline="") as file:  #creating a record csv file
        csvwriter = csv.writer(file) # making a object to write on scv file
        csvwriter.writerow(header)  # #writing to csv file
         
        
         
        for event in events:
            if event['start']['dateTime']:
                time = event['start']['dateTime'] # extractng date info from event (which is stored as  a dictionary)
                date = time[:10]
                date = date.split('-')

                time = time[11:16]
                time = time.split(':')
                date = date[0] + date[1] + date[2]

                time = time[0] + time [1]
                date = int(date)
                time = int(time)
                
            elif event['start']['date']:
                date = event['start']['date']
                date = time[:10]
                date = date.split('-')
                date = date[0] + date[1] + date[2]
                time = 0
                    


            summary = event['summary'] # to extract summary from event 
            if time > currenttime():
                csvwriter.writerow([date,time,summary]) # writing a row
                print('record is written')
           

    # csvData = pd.read_csv("record.csv")
                                        
    # csvData.sort_values(csvData.columns[1], 
    #                         axis=0,
    #                         inplace=True)

    
    # csvData.to_csv('record.csv', index=False)

                    
                    
