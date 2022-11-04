from email import contentmanager
import requests
import json


baseUrl = " http://3.6.195.213:60009"


# Get all Beacons
def getBeacons():
    endPoint = "/beacon"
    url = baseUrl+endPoint
    response = requests.get(url)
    contents = response.content.decode()
    data= json.loads(contents)
    return data
# print("at server file",getBeacons())

#Get all carList(Lisence Number)

def getAllCars():
    endPoint = "/dashboard/get_all_cars"
    url = baseUrl+endPoint
    response = requests.get(url)
    contents = response.content.decode()
    data= json.loads(contents)
    return data


def getCarEvents():
    endPoint = "/dashboard/events_main"
    url = baseUrl+endPoint
    response = requests.get(url)
    contents = response.content.decode()
    data= json.loads(contents)
    return data
# print("at server file",getAllCars())




