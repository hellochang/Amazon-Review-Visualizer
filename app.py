import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
from flask import Flask
<<<<<<< HEAD
data = pd.read_csv("analyzed.csv")

=======
# TO-DO
## Change "product" to "type" in analyzed.csv
## Date doesn't work yet
data = pd.read_csv("analyzed.csv")
>>>>>>> a99dd0568f25483183eca8d065dc97bba991ff55
#print(data)
#data = data.query("product == 'Nike Womens Reax Run 5 Running Shoes'")
data["date"] = pd.to_datetime(data["date"], format="%d %b %Y")
data.sort_values("date", inplace=True)
#print(data)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)
app.title = "Review Analytics: Draw insights from your reviews!"
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="⭐⭐⭐⭐⭐", className="header-emoji"),
                html.H1(
<<<<<<< HEAD
                    children="Analyzed Product Reviews", className="header-title"
                ),
                html.P(
                    children="Interactive shows the customer sentiment over time"
                    " and the rating over time of your product"
                    " during your your desired time interval based on Amazon reviews.",
=======
                    children="Product Reviews", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of avocado prices"
                    " and the number of avocados sold in the US"
                    " between 2015 and 2018",
>>>>>>> a99dd0568f25483183eca8d065dc97bba991ff55
                    className="header-description",
                ),
            ],
            className="header",
        ),
        
                html.Div(
            children=[
                # html.Div(
                #     children=[
                #         html.Div(children="Region", className="menu-title"),
                #         dcc.Dropdown(
                #             id="region-filter",
                #             options=[
                #                 {"label": region, "value": region}
                #                 for region in np.sort(data.region.unique())
                #             ],
                #             value="Albany",
                #             clearable=False,
                #             className="dropdown",
                #         ),
                #     ]
                # ),
                html.Div(
                    children=[
                        html.Div(children="Type", className="menu-title"),
                        dcc.Dropdown(
                            id="type-filter",
                            options=[
                                {"label": product_type, "value": product_type}
                                for product_type in data.type.unique()
                            ],
                            value="organic",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                            ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.date.min().date(),
                            max_date_allowed=data.date.max().date(),
                            start_date=data.date.min().date(),
                            end_date=data.date.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
                
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="sentiment-over-time-graph",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["date"],
                                    "y": data["sentiment_score"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
<<<<<<< HEAD
                                    "text": "Customer Sentiment over time",
=======
                                    "text": "Average Price of Avocados",
>>>>>>> a99dd0568f25483183eca8d065dc97bba991ff55
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
<<<<<<< HEAD
=======
                                    #"tickprefix": "$",
>>>>>>> a99dd0568f25483183eca8d065dc97bba991ff55
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="rating-over-time-graph",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["date"],
                                    "y": data["rating"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
<<<<<<< HEAD
                                    "text": "Product Rating over Time",
=======
                                    "text": "Avocados Sold",
>>>>>>> a99dd0568f25483183eca8d065dc97bba991ff55
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)


@app.callback(
    [
        Output('sentiment-over-time-graph','figure'), 
        Output("rating-over-time-graph", "figure")
        ],
    [
        Input ('product-amazon-review-link', 'value'),
        #Input("region-filter", "value"),
        Input("type-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
        ],
)


def update_charts(region, product_type, start_date, end_date):
    mask = (
        (data.type == product_type)
        & (data.date >= start_date)
        & (data.date <= end_date)
    )
    filtered_data = data.loc[mask, :]
    sentiment_over_time_graph_figure = {
        "data": [
            {
                "x": filtered_data["date"],
                "y": filtered_data["sentiment-score"],
                "type": "lines",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Average Price of Avocados",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    rating_over_time_graph_figure = {
        "data": [
            {
                "x": filtered_data["date"],
                "y": filtered_data["rating"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Avocados Sold", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return sentiment_over_time_graph_figure, rating_over_time_graph_figure

if __name__ == "__main__":
    app.run_server(debug=True)