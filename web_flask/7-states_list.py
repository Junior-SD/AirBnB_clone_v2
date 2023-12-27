#!/usr/bin/python3
"""A python script that starts a Flask Web App and runs the HBNB
storage
"""


from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    s = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=s)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
