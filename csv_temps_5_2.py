import matplotlib.pyplot as plt
import csv
from datetime import datetime
#
#
#
def main():
    open_file = open('death_valley_2018_simple.csv', "r")  ## DEATH VALLEY
    open_file2 = open("sitka_weather_2018_simple.csv", "r") ##SITKA

    DV_file = csv.reader(open_file, delimiter=",")  ## DEATH VALLEY
    SA_file = csv.reader(open_file2, delimiter=',')  ##SITKA

    dates_D, highs_D, lows_D, station_name_D = get_attributes(DV_file)   ###################################################

    dates_S, highs_S, lows_S, station_name_S = get_attributes(SA_file) ###################################################


    fig, (death, sitka) = plt.subplots(2)
    
    fig.subplots_adjust(hspace=0.5)

    # fig = plt.figure()
    death.set_title(station_name_D , fontsize =16) # automatic station name from second row of csv in "NAME" column
    
    death.plot(dates_D, highs_D, color='red', alpha= 0.8)
    death.plot(dates_D, lows_D, color='blue', alpha = 0.8)

    sitka.plot(dates_S, highs_S, color='red', alpha= 0.8)
    sitka.plot(dates_S, lows_S, color='blue', alpha = 0.8)

    death.fill_between(dates_D, highs_D, lows_D, facecolor = "blue", alpha = 0.3) #give it an x-axis and two points in between to fill color
    sitka.fill_between(dates_S, highs_S, lows_S, facecolor = "blue", alpha = 0.3) #give it an x-axis and two points in between to fill color

    death.set_title(station_name_D , fontsize =16) # automatic station name from second row of csv in "NAME" column
    sitka.set_title(station_name_S , fontsize =16) # automatic station name from second row of csv in "NAME" column

    death.set_xlabel("", fontsize=8)
    sitka.set_xlabel("", fontsize=8)

    death.set_ylabel("Temperature in (F)",fontsize = 12)
    sitka.set_ylabel("Temperature in (F)",fontsize = 12)

    death.tick_params(axis="both", which="major" , labelsize= 12)
    sitka.tick_params(axis="both", which="major" , labelsize= 12)

    fig.autofmt_xdate() #makes dates fit diagonally

    plt.show() #dont forget this or the plot wont show
#
#
#
#
def get_attributes(csv_file):
    header_row = next(csv_file)
    first_row = next(csv_file)  ## this selects the first row after the header row. Will need this for the title later

    print(type(header_row))

    for index, column_header in enumerate(header_row):
        if column_header == "TMIN":
            TMIN_index = index
        if column_header == "TMAX":
            TMAX_index = index
        if column_header == "NAME":
            station_name_index = index

    station_name = first_row[station_name_index]  #3 This gets the station name for the title later

    highs = []
    lows = []
    dates = []

    for row in csv_file:
        try:
            high = int(row[TMAX_index])
            low = int(row[TMIN_index])
            current_date = datetime.strptime(row[2], "%Y-%m-%d") #fixes the dates into less amount of dates
        except ValueError:
            print(f"Missing data for {current_date}") # f --> format. Shows where there is a value error (aka missing data)
        else: # if the except statement is the case, then it omits that data and keeps on going with the for loop
            highs.append(high)     #only appends values from column 5 (TMAX)
            lows.append(low)
            dates.append(current_date)
    

    return dates, highs, lows, station_name


#print(highs[:10]) #shows everything up till 9 (not including 10)

main()


# For your 5th python script file - 


# create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

# Matplotlib's pyplot API has a convenience function called subplots() which acts as a 
# utility wrapper and helps in creating common layouts of subplots, including the 
# enclosing figure object, in a single call.

# # fig, ax = plt.subplots(2,2)  -  this will create a visualization with 2 charts on it

'''fig, ax = plt.subplots(2,2)


    fig = plt.figure()

    plt.plot(dates_S, highs_S, color='red', alpha= 0.5)
    plt.plot(dates_S, lows_S, color='blue', alpha = 0.5)

    plt.fill_between(dates_S, highs_S, lows_S, facecolor = "blue", alpha = 0.3) #give it an x-axis and two points in between to fill color

    plt.title(station_name_S , fontsize =16) # automatic station name from second row of csv in "NAME" column
    plt.xlabel("", fontsize=8)
    plt.ylabel("Temperature in (F)",fontsize = 12)
    plt.tick_params(axis="both", which="major" , labelsize= 12)

    fig.autofmt_xdate() #makes dates fit diagonally

    plt.show() #dont forget this or the plot wont show '''