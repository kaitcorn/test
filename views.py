from flask import render_template, request
from app import app
from schedule_api import get_terms
from schedule_api import get_schools

@app.route('/')
def index():
    options = {}
    try:
        options['terms'] = get_terms()
    except:
        options['api_error'] = True
    try:
        options['schools'] = get_schools()
    except:
        options['api_error'] = True

    return render_template('index.html', **options)
