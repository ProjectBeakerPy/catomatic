from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from werkzeug.urls import url_parse
from app.forms import FeedForm
from app import app
from app import petfeeder


@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
  username = 'cap'    
  # app.logger.info('this is an INFO message')
  # app.logger.warning('this is a WARNING message')
  # app.logger.error('this is an ERROR message')
  # app.logger.critical('this is a CRITICAL message')
  form = FeedForm() 
  if form.validate_on_submit():
    petfeeder.feed(1)
  return render_template('index.html', title='Cat-o-matic', username=username, form=form )

  # @app.route('/feed', methods=['POST'])
# def feed():
#     data = {'message': 'Created', 'code': 'SUCCESS'}
#     app.logger.debug('data')
#     return make_response(jsonify(data), 201) 
