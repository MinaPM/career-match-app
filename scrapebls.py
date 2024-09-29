from bs4 import BeautifulSoup
import requests
import json

'''json_string = json.dumps(data)
print(type(json_string))
print(json_string)'''

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
            #print(description)

    
            