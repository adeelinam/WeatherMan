# -*- coding: utf-8 -*-
import copy
import os
from collections import OrderedDict

def main():
    print "WeatherMan"
    # reportNumber = raw_input("Please enter \n1 for Annual Max/Min Temperature\n2 for Hottest day of each year\n"
    #                          "3 for coldest day of each year​\n")
    #
    # print "You pressed " + reportNumber
    yearlyData = OrderedDict()
    previousYear = -1
    currentYear = 0
    year = "year"
    hottestDate = "date"
    temp = "temp"
    maxTemperature = "Max TemperatureC";
    minTemperature = "Min TemperatureC";
    maxHumidity = "Max Humidity"
    minHumidity = "Min Humidity"

    yearData = dict()
    hottestDate = ""
    coldestDate = ""
    hottestDate = ""

    hottestDateData = OrderedDict()
    coldestDateData = OrderedDict()

    yearData[maxTemperature] = -99
    yearData[minTemperature] = 99
    yearData[maxHumidity] = -99
    yearData[minHumidity] = 99

    hottestDateData[year] = ""
    hottestDateData[hottestDate] = ""
    hottestDateData[temp] = ""

    weatherFiles = os.listdir("data")
    for weatherFile in weatherFiles:

        if currentYear != 0:
            if previousYear < currentYear:
                storeData = copy.deepcopy(yearData)
                yearlyData[currentYear] = storeData
                yearData.clear()
                yearData[maxTemperature] = -99
                yearData[minTemperature] = 99
                yearData[maxHumidity] = -99
                yearData[minHumidity] = 99

                hottestDateData[year] = currentYear
                hottestDateData[hottestDate] = hottestDate
                hottestDateData[temp] = storeData[maxTemperature]

                previousYear = currentYear


        monthFileName = os.path.abspath(os.path.join("data", weatherFile))

        with open(monthFileName, 'r') as monthlyFile:
            titles = monthlyFile.readline()
            if titles == "\r\n":
                titles = monthlyFile.readline().strip().split(",")

            # after reading from file
            monthlyData = []
            monthlyMaxData = []
            # sorted data with highest/lowest values
            # highestMonthlyWeather = []
            for day in monthlyFile:
                print "****" + str(monthlyFile) + "****"

                dayData = dict()
                if not day.__contains__("<!--"):
                    parsedDayList = day.strip().split(",")

                    for index, title in enumerate(titles):
                        dayData[str.strip(title)] = parsedDayList[index]

                    # To store year when a new file is parsed and to check yearly max/min
                    if 'PKT' in dayData:
                        currentYear = str(dayData['PKT']).split("-").__getitem__(0)
                        hottestDate = str(dayData['PKT'])
                    elif 'PKST' in dayData:
                        currentYear = str(dayData['PKST']).split("-").__getitem__(0)
                        hottestDate = str(dayData['PKST'])
                    # if yearData[year] == "":
                    #     yearData[year] = previousYear
                    # elif yearData[year] == previousYear:
                    if dayData[maxTemperature] != '':
                        if yearData[maxTemperature] < int(dayData[maxTemperature]):
                            yearData[maxTemperature] = int(dayData[maxTemperature])
                            hottestDate = hottestDate
                    if dayData[minTemperature] != '':
                        if yearData[minTemperature] > int(dayData[minTemperature]):
                            yearData[minTemperature] = int(dayData[minTemperature])
                            coldestDate = hottestDate
                    if dayData[maxHumidity] != '':
                        if yearData[maxHumidity] < int(dayData[maxHumidity]):
                            yearData[maxHumidity] = int(dayData[maxHumidity])
                    if dayData[minHumidity] != '':
                        if yearData[minHumidity] > int(dayData[minHumidity]):
                            yearData[minHumidity] = int(dayData[minHumidity])
                            # else:
                            #     yearlyData.append(yearData)
                            #     yearData.clear()
                            #     yearData[year] = "";
                            #     if dayData[maxTemperature] != '':
                            #         yearData[maxTemperature] = int(dayData[maxTemperature])
                            #     else:
                            #         yearData[maxTemperature] = -99
                            #     if dayData[minTemperature] != '':
                            #         yearData[minTemperature] = int(dayData[minTemperature])
                            #     else:
                            #         yearData[minTemperature] = 99
                            #     if dayData[maxHumidity] != '':
                            #         yearData[maxHumidity] = int(dayData[maxHumidity])
                            #     else:
                            #         yearData[maxHumidity] = -99
                            #     if dayData[minHumidity] != '':
                            #         yearData[minHumidity] = int(dayData[minHumidity])
                            #     else:
                            #         yearData[minHumidity] = 99

                            # monthlyData.append(dayData)
                            # print monthlyData
                            # monthlyMaxData.append(max(monthlyData, key=lambda x: x['Max TemperatureC']))

        # for month in yearlyData:
        #     for dayy in month:
        """To get MAX VALUE"""
        #         [max(monthlyData, key=lambda x:x['Max TemperatureC']) for monthly in monthlyData]
    print "Year\tMAX Temp\tMIN Temp\tMAX Humidity\tMIN​ Humidity​"
    print "--------------------------------------------------------------------------"
    for key in yearlyData:
        year = yearlyData[key]
        print key + "\t\t" + str(year[maxTemperature]) + "\t\t" + str(year[minTemperature]) + "\t\t" \
        + str(year[maxHumidity]) + "\t\t" + str(year[minHumidity])

    print "Year\tMAX Temp\tMIN Temp\tMAX Humidity\tMIN​ Humidity​"
    print "--------------------------------------------------------------------------"
    for key in hottestDateData:
        hottestDate = hottestDateData[key]
        print key + "\t\t" + str(hottestDate[year]) + "\t\t" + str(hottestDate[hottestDate]) + "\t\t" \
              # + str(hottestDate[temp])


if __name__ == '__main__':
    main()
