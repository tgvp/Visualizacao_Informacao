import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv('../data/dataset.csv')

# Create Dash application
app = dash.Dash(__name__)

# Essas somente possuem valores nulos
irrelevant_columns = ['morada', 'distrito', 'descricao']
irrelevant_histogram = ['id_rel', 'id_cliente', 'id_colaborador', 'id_tarefa', 'id_equipa']

# Define layout
app.layout = html.Div(
    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'height': '100vh'},
    children=[
        html.Div(
            style={'width': '60%'},
            children=[
                html.H1('Plots da Análise Exploratória de Dados'),
                dcc.Dropdown(
                    id='dropdown',
                    options=[{'label': col, 'value': col} for col in df.columns if col not in irrelevant_columns + irrelevant_histogram],
                    value=None
                ),
                dcc.Graph(id='histogram'),
                html.Div(id='describe-info')
            ]
        )
    ]
)

# Define callback functions
@app.callback(
    dash.dependencies.Output('histogram', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def update_histogram(selected_column):
    if selected_column is None:
        # Return a blank figure with text
        blank_fig = go.Figure()
        blank_fig.add_annotation(
            text='Selecione uma coluna para visualizar...',
            xref='paper', yref='paper',
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=16)
        )
        return blank_fig
    else:
        counts = df[selected_column].value_counts()
        counts = counts.sort_index()  # Sort by x

        fig = px.bar(counts, x=counts.index, y=counts.values, color=counts.values, 
                     color_continuous_scale='Plasma', labels={'x': selected_column, 'y': 'Quantity'})

        fig.update_layout(
            title_text='Plot de ' + selected_column,
            xaxis_title_text=selected_column,
            yaxis_title_text='Quantidade',
            #bargap=0.2,
            #bargroupgap=0.1
        )

        return fig


@app.callback(
    dash.dependencies.Output('describe-info', 'children'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def update_describe_info(selected_column):
    column_description = df[selected_column].describe().reset_index()
    column_description = column_description.rename(columns={'index': 'Statistic'})
    table = html.Table(
        [html.Tr([html.Th(col) for col in column_description.columns])] +
        [html.Tr([html.Td(val) for val in row]) for row in column_description.values]
    )
    return table

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
