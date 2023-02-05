from dash import Dash, html
from dash.html import Div, H1, P, A, Br

app = Dash()

app.layout = Div(
    [
        H1("World Happiness Dashboard"),
        P(
            [
                "This dashboard shows the happiness score.",
                Br(),
                A(
                    "World Happiness Report Data Source",
                    href="https://worldhappiness.report",
                    target="_blank",
                ),
            ]
        ),
    ]
)
# <div><h1>My Dashboard</h1></div>
# Div(H1("My Dashboard3"))

if __name__ == "__main__":
    app.run_server(debug=True)
