import flask
import json
from handlers import brilcalc


app = flask.Flask(__name__)


@app.route('/')
def root():
    return 'welcome to brilview API'


@app.route('/query', methods=['GET', 'POST'])
def forward_to_server():
    data = flask.request.json
    if data is None:
        return ('Bad request. Query body must be not empty.', 400)
    run_from = data['from']
    run_to = data['to']
    result = brilcalc.get(run_from, run_to)
    return flask.Response(json.dumps(result), mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6000')
