# 1. import Flask
from flask import Flask
from flask import jsonify
import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from sqlalchemy import select

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
@app.route("/index")
@app.route("/index.html")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my Home page!"

#Flask prcp route
@app.route('/precipitation')
def prcp ():

    #reflecting database
    engine = create_engine("sqlite:///Resources/hawaii.sqlite").connect()
    base = automap_base()
    base.prepare(autoload_with=engine)

    #defining tables within the DB
    measurements = base.classes.measurement
    stations = base.classes.station

    #query
    query = db.select(
        [measurements.date, measurements.prcp]).where(measurements.prcp >= 0, measurements.date >= '2016-08-24')
    result = engine.execute(query).fetchall()
    response = jsonify({'result': [dict(row) for row in result]})
    return response

#Flask stations route
@app.route('/stations')
def stations ():

    #reflecting database
    engine = create_engine("sqlite:///Resources/hawaii.sqlite").connect()
    base = automap_base()
    base.prepare(autoload_with=engine)

    #defining tables within the DB
    measurements = base.classes.measurement
    stations = base.classes.station

    #query
    query = db.select(
        [stations])
    result = engine.execute(query).fetchall()
    response = jsonify({'result': [dict(row) for row in result]})
    return response


#Flask stations route
@app.route('/tobs')
def tobs ():

    #reflecting database
    engine = create_engine("sqlite:///Resources/hawaii.sqlite").connect()
    base = automap_base()
    base.prepare(autoload_with=engine)

    #defining tables within the DB
    measurements = base.classes.measurement
    stations = base.classes.station

    #query
    query = db.select(
        [measurements.station, measurements.tobs]).where(measurements.station == 'USC00519281')
    result = engine.execute(query).fetchall()
    response = jsonify({'result': [dict(row) for row in result]})
    return response

if __name__ == "__main__":
    app.run(debug=True)
    
