import dash_summernote
from dash import *

app = Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.css'], external_scripts=['https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.js'])

app.layout = html.Div([
    dash_summernote.DashSummernote(
        id='summernote',
        value='my-value',
        toolbar=[
                    ["style", ["style"]],
                    ["font", ["bold", "underline", "clear"]],
                    ["fontname", ["fontname"]],
                    ["para", ["ul", "ol", "paragraph"]],
                    ["table", ["table"]],
                    ["insert", ["link", "picture", "video"]],
                    ["view", ["fullscreen", "codeview"]]
                ],
        height=300
    ),
    html.Center(html.H1('Output')),
    dash_summernote.DashSummernote(
        id='output',
        value='output',
        toolbar=[],
        height=300
    ),
    # html.Div(id='output')
])

@app.callback(Output('output', 'value'), Input('summernote', 'value'))
def display_output(value):
    return value

if __name__ == '__main__':
    app.run_server(debug=True)
