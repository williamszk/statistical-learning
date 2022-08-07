from dash import Dash, html
from src.components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP

def main() -> None:

    app = Dash(external_stylesheets=[BOOTSTRAP])

    app.title = "Medal dashboard"

    app.layout = create_layout(app)
    # html.Div()  

    app.run()




if __name__ == "__main__":
    main()