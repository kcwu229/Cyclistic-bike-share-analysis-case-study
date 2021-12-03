import pandas as pd
import sqlite3 

df = pd.read_csv("./whole_year_dataset.csv")
print(df.columns)
df = df.drop("Unnamed: 0", axis=1)

connect = sqlite3.connect("./main_data.db")
cur = connect.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS sharing_bike_dataset(
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
    day_of_week INTEGER);             
            """)

df.to_sql("sharing_bike_dataset", con=connect, if_exists="append", index=False)

connect.commit()
connect.close()
print("Successful")