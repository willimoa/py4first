import datetime
from py4web import action

@action('index')
def page():
	return "hello, now is %s" % datetime.datetime.now()

@action('colors')
def colors():
    return {'colors': ['red', 'blue', 'green']}	

@action('color/<name>')
def color(name):
    if name in ['red', 'blue', 'green']:
        return 'You picked color %s' % name
    return 'Unknown color %s' % name

from py4web import request

@action('paint')
@action.uses('paint.html')
def paint():
    return dict(color = request.query.get('color', 'green'))
