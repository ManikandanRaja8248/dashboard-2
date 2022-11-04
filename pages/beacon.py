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
from server.server import getBeacons


@app.callback(Output("beacon-container", "children"),
              Input("interval-component", "n_intervals"))
def updateBeaconPage(n):
    data = getBeacons()
    return html.Div(className="beacon-container", children=[
        html.Div(children=[
            html.Div(className="becon-table-row", children=[
                html.Div(className="table-column",
                         children=[data[i]["beacon_id"]]),
                html.Div(className="table-column",
                         children=[data[i]["license_plate_number"]]),
                html.Div(className="table-column", children=[data[i]["zone"]]),
                #  html.Div(className="table-column",children=["movingStatus"]),
                html.Div(className="table-column battery-div", children=[
                 html.I(className="bi bi-battery-full"),
                 html.Div(children=[data[i]["battery_level"]]),
                 ]),
            ])
        ], className="becon-table")for i in range(len(data))
    ]),


def getBeaconLayout():

    return html.Div(className="current-status-container", children=[
        html.Div(className="heading", children=[""]),

        html.Div(className="status-table-heading", children=[
            html.Div(className="table-column", children=["Beacon ID"]),
            html.Div(className="table-column",
                     children=["License Plate Number"]),
            html.Div(className="table-column", children=["Zone"]),
            #  html.Div(className="table-column",children=["Moving Status"]),
            html.Div(className="table-column", children=["Battery Level"]),
        ]),
        html.Div(id="beacon-container"),
        dcc.Interval(
            id='interval-component',
            interval=3*1000  # in milliseconds
        )


    ]

    )


