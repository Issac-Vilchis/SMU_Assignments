import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#set up sqlite db and tables
engine = create_engine('sqlite:///C:/Users/Owner/Desktop/SMU_Assignments/Unit_10_Advanced_Data_Storage_and_Retrieval/Resources/hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station

#create flask app
app = Flask(__name__)


#create home page
@app.route('/')
def origin():
    return(
      f'Welcome<br/>'
      f'To see Precipitation page, please follow the path: /api/v1.0/precipitation<br/>'
      f'To see Stations page, please follow the path: /api/v1.0/stations<br/>'
      f'To see Dates and Temperature page, please follow the path: /api/v1.0/tobs<br/>'
      f'To see Temperature with the beginning date page, please follow the path and apply years(yyyy-mm-dd): /api/v1.0/<start<br/>'
      f'Te see Temperature with the ending date page, please follow the path and apply years(yyyy-mm-dd): /api/v1.0/<start>/<end><br/>'
    )

#create precipitation page
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    prcp = session.query(Measurement.date, Measurement.prcp).group_by(Measurement.date).all()
    results = list(np.ravel(prcp))
    session.close()
    return jsonify(results)

#create stations page
@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    stations = session.query(Measurement.station).group_by(Measurement.station).all()
    results = list(np.ravel(stations))
    session.close()
    return jsonify(results)

#create dates and temperature page
@app.route('/api/v1.0/tobs')
def dates_and_temp():
    session = Session(engine)
    date_prcp = session.query(Measurement.date, func.sum(Measurement.tobs)).group_by(Measurement.date).all()
    results = list(np.ravel(date_prcp))
    session.close()
    return jsonify(results)

#create Start Temperature page
@app.route('/api/v1.0/<start>')
def start(start):
    session = Session(engine)
    begin = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    
    results = list(np.ravel(begin))
    session.close()
    return jsonify(results)

#create End Temperature date
@app.route('/api/v1.0/<start>/<end>')
def end():
    session = Session(engine)
    end = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    results = list(np.ravel(end))
    session.close()
    return jsonify(results)

#run debug
if __name__ == '__main__':
    app.run(debug=True)