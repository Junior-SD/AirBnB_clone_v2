#!/usr/bin/python3
"""A python script that starts a Flask Web App and makes hbnb application alive
"""


from flask import Flask, render_template
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
import models
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    storage.close


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    s = sorted(storage.all(State).values(), key=lambda state: state.name)
    a = storage.all(Amenity).values()
    p = storage.all(Place).values()

    return render_template('100-hbnb.html', states=s, amenities=a, places=p)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
