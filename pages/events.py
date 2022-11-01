from dash import html,dcc,Input,Output
from app import app





data = {
    "model1":{"event":"one","timestamp":"29/10/2022","zone":"Zone A"},
    "model2":{"event":"two","timestamp":"30/10/2022","zone":"Zone B"},
    "model3":{"event":"three","timestamp":"31/10/2022","zone":"Zone C"},
}
modelList = list(data.keys())
print(modelList[0])


@app.callback(Output("event-data","children"),
              Input("event-dropdown","value"),
              )
def displayEvents(value):
    if value in data:
        return html.Div(className = "event-status",children=[html.Div(className="data-field",children=[data[value]["timestamp"]]),
                                            html.Div(className="data-field",children=[data[value]["zone"]]),
                                            html.Div(className="data-field",children=[data[value]["event"]]),]),

layout =html.Div(className="events-container",children=[
    dcc.Dropdown(id = "event-dropdown",
        options=modelList,
        value=modelList[0],className="model-dropdown"
    ),
    html.Div(className="event-container",children=[
        html.Div(className= "event-heading",children=[html.Div(className="event-field",children=["Timestamp"]),
                                            html.Div(className="event-field",children=["Zone"]),
                                            html.Div(className="event-field",children=["Event"]),]),
        html.Div(id ="event-data")
        ]),
    
    html.Div(id = "event-content")
    
])