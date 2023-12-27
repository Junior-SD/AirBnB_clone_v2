#!/usr/bin/python3
"""A python script that starts a Web Flask App plus extra tweaks
"""


from flask import Flask, render_template
from models import storage
import models
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    s = sorted(storage.all(State).values(), key=lambda state: state.name)
    a = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=s, amenities=a)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
