import json
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State, ALL, MATCH
from dash.exceptions import PreventUpdate
import requests
import dash_bootstrap_components as dbc
from app import app

data={
    "beaconID":"001",
    "licensePlateNumber":"2222",
    "zone":"zone A",
    "movingStatus":"ideal",
    "batteryLevel":"40%",   
}

layout = html.Div(className="current-status-container",children=[
    html.Div(className="heading",children=[""]),
    
        html.Div(className ="status-table-heading",children=[
         html.Div(className="table-column",children=["Beacon ID"]),
         html.Div(className="table-column",children=["License Plate Number"]),
         html.Div(className="table-column",children=["Zone"]),
         html.Div(className="table-column",children=["Moving Status"]),
         html.Div(className="table-column",children=["Battery Level"]),
    ]) ,

    html.Div(children=[
         html.Div(children=[
         html.Div(className ="becon-table-row",children=[
         html.Div(className="table-column",children=[data["beaconID"]]),
         html.Div(className="table-column",children=[data["licensePlateNumber"]]),
         html.Div(className="table-column",children=[data["zone"]]),
         html.Div(className="table-column",children=[data["movingStatus"]]),
         html.Div(className="table-column battery-div",children=[
             html.I(className="bi bi-battery-full"),
             html.Div(children=[data["batteryLevel"]]),
             ]),
    ]) 
    ],className="becon-table")for i in range (5)  
    ])
   
    
]
   
)