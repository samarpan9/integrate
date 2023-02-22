import flask
from flask.templating import render_template 

#Internal file import
from web_app import app

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#dashboard
@app.route("/")
@app.route("/dashboard")
def dashboard():
    return flask.render_template("section.html")



