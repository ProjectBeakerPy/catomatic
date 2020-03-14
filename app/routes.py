from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from werkzeug.urls import url_parse
from app.forms import FeedForm
from app import app

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
      def feed():
    # let the GPIO library know where we've connected our servo to the Pi
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    attempts = int(sys.argv[1])

    try:
        servo = GPIO.PWM(12, 50)
        servo.start(12.5)

        # spin left, right, then left again rather than in a continuous circle
        # to prevent the food from jamming the servo
        for index in range(0, 3):
            dutyCycle = 2.5 if (index % 2 == 0) else 12.5
            servo.ChangeDutyCycle(dutyCycle)
            # adjust the sleep time to have the servo spin longer or shorter in that direction
            time.sleep(.75)
    finally:
        # always cleanup after ourselves
        servo.stop()
        GPIO.cleanup()


if __name__ == '__main__':
    # kick off the feeding process (move the servo)
    feed()
  return render_template('index.html', title='Cat-o-matic', username=username, form=form )

  # @app.route('/feed', methods=['POST'])
# def feed():
#     data = {'message': 'Created', 'code': 'SUCCESS'}
#     app.logger.debug('data')
#     return make_response(jsonify(data), 201) 