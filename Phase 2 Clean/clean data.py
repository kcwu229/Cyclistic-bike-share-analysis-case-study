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
3. Grouping ride_length into more meaningful way 
"""

# mission 1
data = data[data["ride_length"]>=5]


# mission 2
def split(text):
    return text.split(" ")[1].split(":")[0]

data["started_at"] = data["started_at"].astype("str")
data["ended_at"] = data["ended_at"].astype("str")

data["started_time_slot"] = data["started_at"].apply(split)
data["ended_time_slot"] = data["ended_at"].apply(split)


# mission 3
data["duration_group"] = ""

def grouping(duration_time):
    if duration_time <= 30:
        data["duration_group"] = "5 - 30 mins"
        
    elif duration_time <= 60:
         data["duration_group"] = "30 to 1 hour"
         
    elif duration_time <= 180:
        data["duration_group"] = "1 to 3 hours"
    
    elif duration_time <= 480:
        data["duration_group"] = "3 to 8 hours"
        
    elif duration_time > 480:
        data["duration_group"] = "above 8 hours"
    
data["ride_length"].apply(grouping)

print(data["duration_group"])


"""df = data.to_csv("./sharing_bike_dataset_cleaned.csv", index=False)

print("Successful !")"""
