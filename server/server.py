from email import contentmanager
import requests
import json


baseUrl = "http://52.74.198.240:60009"


# Get all Beacons
def getBeacons():
    entity = "/beacon"
    url = baseUrl+entity
    response = requests.get(url)
    contents = response.content.decode()
    data= json.loads(contents)
    return data
# print("at server file",getBeacons())

#Get all carList(Lisence Number)

def getAllCars():
    entity = "/dashboard/get_all_cars"
    url = baseUrl+entity
    response = requests.get(url)
    contents = response.content.decode()
    data= json.loads(contents)
    return data

# print("at server file",getAllCars())




