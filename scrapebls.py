from bs4 import BeautifulSoup
import requests
import json

def print_message(message, showKeys=False):
    if showKeys:
        for key, value in message.items():
            print(key + ":", value)
    else:
        for value in message.values():
            print(value)

def insert_job(data):
        response = requests.post(API_URL+"/add_job", json=data)
        message = response.json()
        print_message(message)

API_URL = "http://3.86.34.32:5000"
r = requests.get("https://www.4cornerresources.com/job-descriptions/")
if(r.status_code == 200):
    print("success")
    soup = BeautifulSoup(r.text, "html.parser")
    lists = soup.find("div", class_ = 'site-inner')
    li = lists.find_all("li")
    description = ""
    for i in range(27,len(li)):
        r = requests.get(li[i].find('a').get('href'))
        if(r.status_code == 200):
            desc = []
            soup = BeautifulSoup(r.text, "html.parser")
            title = next(soup.find("h1").children).strip()
            print(title)
            paragraph = soup.find("div", class_="wp-block-column is-layout-flow wp-block-column-is-layout-flow").find_all("p")
            desc+=paragraph
            accordion = soup.find_all("div", class_="c-accordion__content")
            for acc in accordion:
                desc += acc.find_all("li")
            for d in desc:
                description += d.get_text()
            insert_job({title: description})
    
    

   

    
            