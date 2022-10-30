#!/usr/bin/env python
# coding: utf-8

# In[10]:


from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'


# In[11]:


# Set Up the Flask Weather App
import datetime as dt
import numpy as np
import pandas as pd


# In[12]:


# get the dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database. Add the SQLAlchemy dependencies 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[13]:


# import the dependencies that we need for Flask
from flask import Flask, jsonify


# In[14]:


#Set Up the Database We'll set up our database engine for the Flask application
engine = create_engine("sqlite:///hawaii.sqlite")


# In[15]:


# # reflect an existing database into a new model
Base = automap_base()


# In[16]:


# reflect the tables
Base.prepare(engine, reflect=True)


# In[17]:


#We'll create a variable for each of the classes so that we can reference them later, as shown below.
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[18]:


# Finally, create a session link from Python to our database with the following code:
session = Session(engine)


# In[19]:


### Set Up Flask
### at the folder & terminal 
#### pip install flask
#### app = Flask(__name__)
#### FLASK_APP
#### @app.route("/")
#### and enter message required egdef welcome():
#    return(
#    '''
#    Welcome to the Climate Analysis API!
#    Available Routes:
#    /api/v1.0/precipitation
#    /api/v1.0/stations
#    /api/v1.0/tobs
#    /api/v1.0/temp/start/end
#    ''')



app = Flask(__name__)


# In[20]:


import app

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")


# In[22]:


# when we run the script with python app.py, the __name__ variable will be set to __main__. This indicates that we are not using any other file to run this code.

# Now we're ready to build our Flask routes!


# In[27]:


# All of your routes should go after the app = Flask(__name__) line of code. Otherwise, your code may not run properly.

app = Flask(__name__)


# In[28]:


# We can define the welcome route using the code below:
@app.route("/")


# In[ ]:


# create a function welcome() with a return statement. 
# def welcome():
  #  return


# In[ ]:


## Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement. We'll use f-strings to display them for our investors:
# 
# When creating routes, we follow the naming convention /api/v1.0/ followed by the name of the route. This convention signifies that this is version 1 of our application.

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


# In[42]:


flask run
from flask import jsonify
@app.route("/users/me")
def get_current_user():
    return jsonify(
        username=g.user.username,
        email=g.user.email,
        id=g.user.id,


# In[43]:


# To create the route, add the following code. Make sure that it's aligned all the way to the left.
@app.route("/api/v1.0/precipitation")


# In[39]:


# code that calculates the date one year ago from the most recent date in the database.& 
# query to get the date and precipitation for the previous year
# Notice the .\ in the first line of our query? This is used to signify that we want our query to continue on the next line. 

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).      filter(Measurement.date >= prev_year).all()
   return


# In[40]:


# create a dictionary with the date as the key and the precipitation as the value. To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file.


def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


# In[37]:


@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).      filter(Measurement.date >= prev_year).all()
   return


# In[35]:


@app.route("/api/v1.0/stations")


# In[36]:


def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# In[ ]:


@app.route("/api/v1.0/tobs")


# In[ ]:


def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    return


# In[ ]:


def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).        filter(Measurement.station == 'USC00519281').        filter(Measurement.date >= prev_year).all()
    return
Finally, as before, unrave


# In[ ]:


def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).      filter(Measurement.station == 'USC00519281').      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# In[ ]:


flask run


# In[ ]:


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")


# In[ ]:


def stats(start=None, end=None):
     return


# In[ ]:


def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]


# In[ ]:


def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).        filter(Measurement.date >= start).        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)


# In[ ]:


flask run


# In[ ]:


api(/v1.0/temp/start/end, route)
[null,null,null]


# In[ ]:



#Student Support
#Career Services
#Billing
#Career Events
#9.5.6
#Statistics Route
#The investors will need to see the minimum, maximum, and average temperatures. For this we'll create a route for our summary statistics report.
#Just one more route to create! Our last route will be to report on the minimum, average, and maximum temperatures. However, this route is different from the previous ones in that we will have to provide both a starting and ending date. Add the following code to create the routes:

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#Next, create a function called stats() to put our code in.

def stats():
     return
#We need to add parameters to our stats()function: a start parameter and an end parameter. For now, set them both to None.

def stats(start=None, end=None):
     return
#With the function declared, we can now create a query to select the minimum, average, and maximum temperatures from our SQLite database. We'll start by just creating a list called sel, with the following code:

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
#Since we need to determine the starting and ending date, add an if-not statement to our code. This will help us accomplish a few things. We'll need to query our database using the list that we just made. Then, we'll unravel the results into a one-dimensional array and convert them to a list. Finally, we will jsonify our results and return them.

#NOTE
#In the following code, take note of the asterisk in the query next to the sel list. Here the asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures.

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
#Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. We'll use the sel list, which is simply the data points we need to collect. Let's create our next query, which will get our statistics data.

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).        filter(Measurement.date >= start).        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
#Finally, we need to run our code. To do this, navigate to the "surfs_up" folder in the command line, and then enter the following command to run your code:

flask run
#After running this code, you'll be able to copy and paste the web address provided by Flask into a web browser. Open /api/v1.0/temp/start/end route and check to make sure you get the correct result, which is:

[null,null,null]
#This code tells us that we have not specified a start and end date for our range. Fix this by entering any date in the dataset as a start and end date. The code will output the minimum, maximum, and average temperatures. For example, let's say we want to find the minimum, maximum, and average temperatures for June 2017. You would add the following path to the address in your web browser:

api(/v1.0/temp/2017-06-01/2017-06-30)


# In[ ]:



#9.5.6
#Statistics Route
#The investors will need to see the minimum, maximum, and average temperatures. For this we'll create a route for our summary statistics report.
#Just one more route to create! Our last route will be to report on the minimum, average, and maximum temperatures. However, this route is different from the previous ones in that we will have to provide both a starting and ending date. Add the following code to create the routes:

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#Next, create a function called stats() to put our code in.

def stats():
     return
#We need to add parameters to our stats()function: a start parameter and an end parameter. For now, set them both to None.

def stats(start=None, end=None):
     return
#With the function declared, we can now create a query to select the minimum, average, and maximum temperatures from our SQLite database. We'll start by just creating a list called sel, with the following code:

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
#Since we need to determine the starting and ending date, add an if-not statement to our code. This will help us accomplish a few things. We'll need to query our database using the list that we just made. Then, we'll unravel the results into a one-dimensional array and convert them to a list. Finally, we will jsonify our results and return them.

#NOTE
#In the following code, take note of the asterisk in the query next to the sel list. Here the asterisk is used to indicate there will be multiple results for our query: minimum, average, and maximum temperatures.

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
Now we need to calculate the temperature minimum, average, and maximum with the start and end dates. We'll use the sel list, which is simply the data points we need to collect. Let's create our next query, which will get our statistics data.

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).        filter(Measurement.date >= start).        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
#Finally, we need to run our code. To do this, navigate to the "surfs_up" folder in the command line, and then enter the following command to run your code:

flask run
#After running this code, you'll be able to copy and paste the web address provided by Flask into a web browser. Open /api/v1.0/temp/start/end route and check to make sure you get the correct result, which is:

[null,null,null]
#This code tells us that we have not specified a start and end date for our range. Fix this by entering any date in the dataset as a start and end date. The code will output the minimum, maximum, and average temperatures. For example, let's say we want to find the minimum, maximum, and average temperatures for June 2017. You would add the following path to the address in your web browser:

api(/v1.0/temp/2017-06-01/2017-06-30)
#When you run the code, it should return the following result:

["temps":[71.0,77.21989528795811,83.0]]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




