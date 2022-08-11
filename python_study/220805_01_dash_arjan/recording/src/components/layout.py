from dash import Dash, html
from src.components import nation_dropdown, barcharts
from src.components import ids


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    nation_dropdown.render(app),
                ],
            ),
            barcharts.render(app)
        ]
    )
