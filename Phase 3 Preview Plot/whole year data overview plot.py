import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

# check for null value or 0
def check_len(text):
    if len(text) != 8:
        text = "0" + text        
    return text

df["ride_length"] = df["ride_length"].apply(check_len)

# show the time in mins
df["ride_length"] = pd.to_datetime(df["ride_length"],format='%H:%M:%S').dt.minute + pd.to_datetime(df["ride_length"],format='%H:%M:%S').dt.hour*60


plt.figure(figsize=(26, 15), dpi=80)
""" Preview 1 """
# average ride_length for members and casual riders
member_casual = df.groupby("member_casual")["ride_length"].agg("mean")
member_casual.plot.bar()
plt.xlabel("member_casual")
plt.ylabel("average_ride_length")
plt.savefig("./average ride_length for members and casual riders.png")


""" Preview 2 """
# average ride_length for users by day_of_week
day_of_week = df.groupby(["day_of_week", "member_casual"])["ride_length"].agg("mean")
day_of_week.plot.bar()
plt.xlabel("day_of_week")
plt.ylabel("average_ride_length")
plt.savefig("./average ride_length for users by day_of_week.png")


""" Preview 3 """
# number of rides for users by day_of_week
count_of_ride_id = df.groupby(["day_of_week", "member_casual"])["ride_id"].size()
count_of_ride_id.plot.bar()
plt.xlabel("day_of_week")
plt.ylabel("number of rides")
plt.savefig("./number of rides for users by day_of_week.png")

print("Successful")