import requests
API_URL = "http://3.86.34.32:5000"

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

insert_job({"name":"owuefhouweh"})
