
import datetime

from flask import Flask, render_template, flash, redirect, request, url_for
from pprint import pprint as pp
from gamble import query_api

app = Flask(__name__)


@app.route('/')
def index():
    

    return render_template('index.html', data=[{'name':'Ver partidos del día'}, {'name':'Ver partidos En Juego'}])


@app.route('/result', methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api()
    pp(resp)
    if resp:
        data.append(resp)
    return render_template('result.html', data=data)



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
