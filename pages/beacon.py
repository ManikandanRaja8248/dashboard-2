from email.mime import base
import json
from urllib import response
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL, MATCH
from dash.exceptions import PreventUpdate
import requests
import dash_bootstrap_components as dbc
from app import app
import requests
import json

baseUrl = "http://52.74.198.240:60009"
entity = "/beacon"

def getBeacons():
    url = baseUrl+entity
    response = requests.get(url)
    data = response.content.decode()
    return data

data = json.loads(getBeacons())

layout = html.Div(className="current-status-container",children=[
    html.Div(className="heading",children=[""]),
    
        html.Div(className ="status-table-heading",children=[
         html.Div(className="table-column",children=["Beacon ID"]),
         html.Div(className="table-column",children=["License Plate Number"]),
         html.Div(className="table-column",children=["Zone"]),
        #  html.Div(className="table-column",children=["Moving Status"]),
         html.Div(className="table-column",children=["Battery Level"]),
    ]) ,

    html.Div(className="beacon-container",children=[
         html.Div(children=[
         html.Div(className ="becon-table-row",children=[
         html.Div(className="table-column",children=[data[0]["beacon_id"]]),
         html.Div(className="table-column",children=[data[0]["license_plate_number"]]),
         html.Div(className="table-column",children=[data[0]["zone"]]),
        #  html.Div(className="table-column",children=["movingStatus"]),
         html.Div(className="table-column battery-div",children=[
             html.I(className="bi bi-battery-full"),
             html.Div(children=[data[0]["battery_level"]]),
             ]),
    ]) 
    ],className="becon-table")for i in range (10)  
    ])
   
    
]
   
)