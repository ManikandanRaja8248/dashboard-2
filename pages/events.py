from dash import html, dcc, Input, Output
from app import app
import requests
import json
from server.server import getAllCars



baseUrl = "http://52.74.198.240:60009"

# @app.callback(Output("event-data-field-container","children"),
#                Input("interval-component","n_intervals"))
# def autoUpdate(n):
#      return getAllCars()


@app.callback(Output("event-data", "children"),
              Input("event-dropdown", "value"),
              Input("interval-component","n_intervals")
              )
def displayEvents(value,n):
    carList = getAllCars()
    if value in carList:
        entity = f"/events/{value}"
        url = baseUrl+entity
        response = requests.get(url)
        data = response.content.decode()
        events = json.loads(data)

        return html.Div(className="event-data-field-container",id = "event-data-field-container", children=[
            html.Div(className="event-status", children=[html.Div(className="data-field", children=[events[i]['timestamp']]),
                                                         html.Div(
                className="data-field", children=[events[i]['zone']]),
                html.Div(className="data-field", children=[events[i]['event']])
            ])for i in range(len(events))

        ])


def getEventsLayout():
    carList =getAllCars()
    return html.Div(className="events-container", children=[
        dcc.Dropdown(id="event-dropdown",
                     options = carList,
                    #  value=carList[0], 
                     className="car-model-dropdown",
                     style={
                             'text-decoration': 'none',
                            #  'width': '32vw',
                            #  'height':'3vh',
                            #  "background-color": "transparent",
                            #  'color': 'red',
                             'text-align': 'left'}
                     ),
        html.Div(className="event-container", children=[
            html.Div(className="event-heading", children=[html.Div(className="event-field", children=["Timestamp"]),
                                                          html.Div(
                className="event-field", children=["Zone"]),
                html.Div(className="event-field", children=["Event"]), ]),
            html.Div(id="event-data")
        ]),

        html.Div(id="event-content"),
         dcc.Interval(
            id='interval-component',
            interval=3*1000 # in milliseconds
        
        )

    ])


# layout = getEventsLayout()
