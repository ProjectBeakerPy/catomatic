from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app

@app.route('/')
@app.route('/index')
def index():
    username = 'cap'
    return render_template('index.html', title='Home', username=username )
