import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open('death_valley_2018_simple.csv', "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index,column_header in enumerate(header_row): #this gives number to what index station each header name is in
    print(index, column_header)

highs = []
lows = []
dates = []

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2], "%Y-%m-%d") #fixes the dates into less amount of dates
    except ValueError:
        print(f"Missing data for {current_date}") # f --> format. Shows where there is a value error (aka missing data)
    else: # if the except statement is the case, then it omits that data and keeps on going with the for loop
        highs.append(high)     #only appends values from column 5 (TMAX)
        lows.append(low)
        dates.append(current_date)

#print(highs[:10]) #shows everything up till 9 (not including 10)

fig = plt.figure()

plt.plot(dates, highs, color='red', alpha= 0.5)
plt.plot(dates, lows, color='blue', alpha = 0.5)

plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1) #give it an x-axis and two points in between to fill color

plt.title("Daily High Temps for Death Valley, July 2018" , fontsize =16)
plt.xlabel("", fontsize=8)
plt.ylabel("Temperature in (F)",fontsize = 12)
plt.tick_params(axis="both", which="major" , labelsize= 12)

fig.autofmt_xdate() #makes dates fit diaagonally

plt.show() #dont forget this or the plot wont show
