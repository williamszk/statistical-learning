from dash import Dash, html, dcc
from src.components.ids import NATION_DROPDOWN


def render(app: Dash) -> html.Div:

    all_nations = ["South Korea", "China", "Canada"]

    return html.Div(
        children=[
            html.H6("Nation"),
            dcc.Dropdown(
                id=NATION_DROPDOWN,
                options=[{"label": nation, "value": nation}
                         for nation in all_nations],
                value=all_nations,
                multi=True
            )

        ]

    )
