import pandas as pd
import datetime

# ready to be merged
one = pd.read_csv("./202010.csv")
two = pd.read_csv("./202011.csv")
three = pd.read_csv("./202012.csv")
four = pd.read_csv("./202101.csv")
five = pd.read_csv("./202102.csv")
six = pd.read_csv("./202103.csv")
seven = pd.read_csv("./202104.csv")
eight = pd.read_csv("./202105.csv")
nine = pd.read_csv("./202106.csv")
ten = pd.read_csv("./202107.csv")
eleven = pd.read_csv("./202108.csv")
twelve = pd.read_csv("./202109.csv")

# merge table into one dataframe
df = pd.concat([one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve])
df.to_csv("./whole_year_dataset.csv", index=False)
