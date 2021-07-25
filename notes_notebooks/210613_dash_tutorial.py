
# https://www.youtube.com/watch?v=hSPmj7mK6ng&t=181s&ab_channel=CharmingDataCharmingData

#%%
from dash_core_components.Location import Location
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output


#%%
app = dash.Dash(__name__)



#%%

df_00 = pd.read_csv("../data/intro_bees.csv")

df_00 = df_00.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()

df_00.reset_index(inplace=True)


#%%

app.layout = html.Div([

    html.H1("Web application dashboard with Dash", style={'text-align':'center'}),

    dcc.Dropdown(id="select_year",
        options=[
            {"label":"2015","value":2015},
            {"label":"2016","value":2016},
            {"label":"2017","value":2017},
            {"label":"2018","value":2018}
        ],
        value=2015,
        style={"width":"50%"}    
    ),
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id="my_bee_map",figure={})

])


#%%

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id="select_year", component_property='value')]

)
def update_graph(option_selected):
    # print(option_selected)
    # print(type(option_selected))

    container = html.H2(f"The year chosen was {option_selected}") 

    df_01 = df_00.copy()
    df_01 = df_01[df_01["Year"]==option_selected]
    df_01 = df_01[df_01["Affected by"]=="Varroa_mites"]

    fig = px.choropleth(
        data_frame=df_01,
        locationmode='USA-states',
        locations='state_code',
        scope="usa",
        color='Pct of Colonies Impacted',
        hover_data=["State","Pct of Colonies Impacted"],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )

    # fig = go.Figure(
    #     data = [
    #         go.Choropleth(
    #             locationmode='USA-states',
    #             locations=df_01["state_code"],
    #             z = df_01["Pct of Colonies Impacted"].astype(float),
    #             colorscale='Reds'
    #         )
    #     ]
    # )

    # fig.update_layout(
    #     title_text = "Bees affected by mites in the USA",
    #     title_xanchor = "center",
    #     title_font = dict(size=24),
    #     title_x = 0.5,
    #     geo = dict(scope='usa')

    # )

    return container, fig






#%%
if __name__ == '__main__':
    app.run_server(debug=True)

#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


