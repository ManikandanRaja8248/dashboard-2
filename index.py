from dash import html,dcc,Input,Output
# Connect to main app.py file
from app import app
from app import server
from pages import beacon, events

app.layout=html.Div([
     dcc.Location(id='url', refresh=True),
      html.Div([
          html.Div(className="nav-link",children=[
            dcc.Link([
            html.P(children= ["Beacon"])
          ],href='/pages/beacon'),
           dcc.Link([
            html.P(children= ["Event"])
          ],href='/pages/events'),
              
        ]),
          html.Div(children=[
              html.Img(src="/assets/vicara.png",className="vicara-logo")
              
          ])
          
          
      ],className='nav-bar'),
    
     html.Div(id='page-content', children=[],className="page-content")
    
],className='main-container')
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/pages/currentStatus':
        return beacon.layout
    if pathname == "/pages/events":
        return events.layout
    else:
        return beacon.layout


if __name__ == '__main__':
    app.run_server(debug=True,threaded=True)