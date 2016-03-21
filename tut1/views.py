from flask import render_template
from tut1 import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'ashu'}
    return render_template('index.html',
    	title = 'home',
    	user = user)
