from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc


# Макет страницы "О проекте"
layout = dbc.Container([
    dbc.Row([
        html.Div([
            html.H1("О проекте"),
            html.P("Этот проект предназначен для анализа университетов по различным критериям, включая мировой рейтинг, академическую репутацию, цитирования и др."),
            html.P("Для просмотра исходного кода проекта, посетите наш репозиторий на GitHub:"),
            html.A("GitHub репозиторий", href="https://github.com/your_username/your_repository"),
            html.Hr(style={'color': 'black'}),
        ], style={'textAlign': 'center'})
    ]),
])

def display_page():
        return layout
