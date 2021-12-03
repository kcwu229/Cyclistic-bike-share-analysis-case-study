import pandas as pd 
from datetime import datetime
import sqlite3

# merge dataset
path = "C:\\Users\\123\\Desktop\\case study\\case study\\Phase 2 Clean\\Fill values finish\\"
df1 = pd.read_csv(path + "sharing_bike_dataset_1.csv")
df2 = pd.read_csv(path + "sharing_bike_dataset_2.csv")
df3 = pd.read_csv(path + "sharing_bike_dataset_3.csv")
df4 = pd.read_csv(path + "sharing_bike_dataset_4.csv")
df5 = pd.read_csv(path + "sharing_bike_dataset_full.csv")


# after ignoring both null values in station_name and station_id: 4354489 rows 
data = pd.concat([df1,df2,df3,df4,df5])


# ----------------------------------------------------------------------------
""" 
3 missions:
1. Remove ride_length rows that is smaller than 5 mins (uneffective count)
2. Add started_time_slot and ended_time_slot column to store time_slot in hour
3. Grouping ride_length into more meaningful way (this part do in SQL)
"""

# mission 1: Remove ride_length rows that is smaller than 5 mins
data = data[data["ride_length"]>=5]


# mission 2 Add started_time_slot and ended_time_slot column to store time_slot in hour
def split(text):
    return text.split(" ")[1].split(":")[0]

data["started_at"] = data["started_at"].astype("str")
data["ended_at"] = data["ended_at"].astype("str")

data["started_time_slot"] = data["started_at"].apply(split)
data["ended_time_slot"] = data["ended_at"].apply(split)



# Import data to datbase for mission 3

connect = sqlite3.connect("./main_data.db")
cur = connect.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS sharing_bike_dataset_clean_ver1(
    ride_id TEXT, 
    rideable_type TEXT, 
    started_at TIMESTAMP, 
    ended_at TIMESTAMP, 
    start_station_name TEXT, 
    start_station_id TEXT, 
    end_station_name TEXT, 
    end_station_id TEXT, 
    start_lat TEXT, 
    start_lng TEXT, 
    end_lat TEXT, 
    end_lng TEXT, 
    member_casual TEXT,
    ride_length INTEGER,
    day_of_week INTEGER,
    started_time_slot INTEGER,
    ended_time_slot INTEGER    
    );             
            """)

data.to_sql("sharing_bike_dataset_clean_ver1", con=connect, if_exists="append", index=False)

connect.commit()
connect.close()
print("Successful")