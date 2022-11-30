import requests 
import json 
import os 

def hello_world(): 
    data = requests.get("https://raw.githubusercontent.com/ISIS2503/ISIS2503-Microservices-AppDjango/master/data/temperatura.json",
    headers={"Accept":"application/json"})
    print(data.json())
    json_data = data.json()
    requ = requests.post("http://35.198.37.110:8080/createmeasurements/", json=json_data, headers={'Content-type': 'application/json', "charset": "utf-8"}) 
    print(requ.text)
    return "The function was successfully executed"

hello_world()