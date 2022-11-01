from dash import html,dcc,Input,Output
from app import app
import requests
import json


baseUrl = "http://52.74.198.240:60009"


def getAllCars():
    entity = "/dashboard/get_all_cars"
    url = baseUrl+entity
    response = requests.get(url)
    data = response.content.decode()
    return data
carList = json.loads(getAllCars())

@app.callback(Output("event-data","children"),
              Input("event-dropdown","value"),
              )
def displayEvents(value):
    if value in carList:
        entity = f"/events/{value}"
        url = baseUrl+entity
        response = requests.get(url)
        data = response.content.decode()
        events = json.loads(data)
    
        return html.Div(className="event-data-field-container",children=[
            html.Div(className = "event-status",children=[html.Div(className="data-field",children=[events[i]['timestamp']]),
                                            html.Div(className="data-field",children=[events[i]['gateway_id']]),
                                            html.Div(className="data-field",children=[events[i]['event']])
                                            ])for i in range(len(events))

        ])
layout =html.Div(className="events-container",children=[
    dcc.Dropdown(id = "event-dropdown",
        options=carList,
        value=carList[0],className="model-dropdown"
    ),
    html.Div(className="event-container",children=[
        html.Div(className= "event-heading",children=[html.Div(className="event-field",children=["Timestamp"]),
                                            html.Div(className="event-field",children=["Zone"]),
                                            html.Div(className="event-field",children=["Event"]),]),
        html.Div(id ="event-data")
        ]),
    
    html.Div(id = "event-content")
    
])