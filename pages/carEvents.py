from dash import html, dcc, Input, Output
from app import app
import requests
import json
from server.server import getCarEvents


# data = [
#     {
#         "license_plate_number": "TN03N4503",
#         "event": "Stopped moving",
#         "zone": "Zone A",
#         "timestamp": "2022-11-03T11:46:51"
#     },

#     {
#         "license_plate_number": "UP16CM6904",
#         "event": "Stopped moving",
#         "zone": "Zone B",
#         "timestamp": "2022-11-03T11:25:37"
#     }

# ]


@app.callback(Output('car-event-content','children'),
              Input("interval-component","n_intervals"))
def autoUpdatingPage(n):
    data = getCarEvents()
    return html.Div(children=[
        html.Div(children=[
                html.Div(className="car-event-data", 
                         children=[html.Div(className="data-field", children=[data[i]['license_plate_number']]),
                                   html.Div(className="data-field", children=[data[i]['event']]),
                                   html.Div(className="data-field", children=[data[i]['zone']]),
                                   html.Div(className="data-field", children=[data[i]['timestamp']]), 
                ]),
                
            ])for i in range(len(data))
        
    ])


def getCarEventsLayout():
    return html.Div(className="car-events-container", children=[
        
        html.Div(className="event-container", children=[
            html.Div(className="car-event-heading", children=[html.Div(className="event-field", children=["Car"]),
                                                          html.Div(
                className="event-field", children=["Event"]),
                html.Div(className="event-field", children=["Zone"]),
                html.Div(className="event-field", children=["Timestamp"]), 
                ]),
            html.Div(id="car-event-content",className="car-event-content",children=[
            
        ])
        ]),

        
         dcc.Interval(
            id='interval-component',
            interval=3*1000 # in milliseconds
        
        )

    ])


