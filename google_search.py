import csv
import re
import string
import nltk
from nltk.corpus import stopwords
import random
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
import os.path

class google_search:
    def __init__(self,string):
        self.word = string

    def checkfile(self,str):
        if os.path.isfile('search.csv'):
            file = open('search.csv','r')
            csvreader = csv.reader(file)
            header = next(csvreader)

            for row in csvreader:
                if len(row)!=0:
                    if row[0] == self.word:
                        if row[1] == str:
                            file.close()
                            return False
                  
            
        return True      

    def write_file(self,info,type):

        if not os.path.isfile('search.csv'):
            file = open('search.csv','w',newline="")
            csvwriter = csv.writer(file)
            csvwriter.writerow(['word','string','type'])
            file.close()
            
        file = open('search.csv','a',newline="")
        csvwriter = csv.writer(file)
        csvwriter.writerow([self.word,info,type])

    def uses_search(self):
        URL = "https://www.google.com/search?q="+self.word+"uses"

        r = requests.get(URL)

        soup = BeautifulSoup(r.content,'html5lib')
        data = soup.find_all('span',attrs = {'class' : 'atOwb UMOHqf'})
        tips = []
        for b in data:
            tips.append(b.text)


        for str in tips:
            if str == "People also ask":
                return "none","uses"

            elif self.checkfile(str):
                return str,"uses"

        return "none","uses"

    def benefits_search(self):
        URL = "https://www.google.com/search?q="+self.word+"benefits"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content,'html5lib')
        data = soup.find_all('li',attrs = {'class' : 'MSiauf'})


        for b in data:
            if self.checkfile(b.text):
                return b.text,"benefits"
        return "none","benefits"

    def meaning_search(self):
        URL = "https://www.google.com/search?q="+self.word+"meaning"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content,'html5lib')
        data = soup.find_all('div',attrs = {'class':'MSiauf'})

        for b in data:
            if self.checkfile(b.text) or b==data[-1]:
                 return b.text,"meaning"
           

    def main_search(self):

        tip = self.benefits_search()
        if tip[0] !="none":
            self.write_file(tip[0],tip[1])
            return tip[0]
            
        tip = self.uses_search()
        if tip[0] != "none":
            self.write_file(tip[0],tip[1])
            return tip[0]
        
        
        
        tip = self.meaning_search()
        if self.checkfile(tip[0]) == True:
            self.write_file(tip[0],tip[1])
        return tip[0]


stopword_english = stopwords.words('english')

def today():
    with open('record.csv','r') as file:
        csvreader = csv.reader(file)
        next(csvreader)

        if not os.path.exists('today.csv'):
            header= ["title","message"]
            file =  open("today.csv","w", newline="")
            csvwriter= csv.writer(file)
            csvwriter.writerow(header)
            print('today is created')
        else:
            file = open('today.csv','a',newline="")
            csvwriter = csv.writer(file)
            print('today is opened')

        for row in csvreader:
            final = re.sub(r'^RT[\s]+','',row[2])
            final = re.sub(r'https?://[^\s\n\r]+','',final)
            final = re.sub(r'#','',final)
            
            #print(final)
            final2 = word_tokenize(final)

            #print(final2)
        
            final_clean = []
            for word in final2:
                if(word not in stopword_english and word not in string.punctuation):
                    final_clean.append(word)
            
            #print(final_clean)
            rand = 0
            rand = random.randint(0,len(final_clean)-1)
            #print(rand)
            
            #print(final_clean[rand])
            googlesearch = google_search(final_clean[rand])
            
            csvwriter.writerow([row[2],googlesearch.main_search()])
        
        file.close()



            



