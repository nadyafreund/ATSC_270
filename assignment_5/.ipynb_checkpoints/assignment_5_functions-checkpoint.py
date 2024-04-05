#
#
from siphon.simplewebservice.iastate import IAStateUpperAir
from metpy.io import add_station_lat_lon
import datetime
import pandas

# get_raobs 
# returns a pandas dataframe with RAOBs
# input = dt (a datetime object)
def get_raobs(dt: datetime.datetime) -> pandas.DataFrame:
    #collecting data
    data=IAStateUpperAir().request_all_data(dt)
    #adding lat lon data to raobs
    data=add_station_lat_lon(data)
    return(data)


# select_press
# returns a pandas dataframe with RAOB observations at the specified pressure level
# input = data (a RAOB pandas dataframe)
#       = press_lev (the pressure level requested in hPa)
def select_press(data: pandas.DataFrame,pres_lev) -> pandas.DataFrame:
    #using loc to grab rows
    data=data.loc[data.pressure==pres_lev]
    return(data)

