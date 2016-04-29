#
# with open("/Users/arbisoft/Downloads/weatherdata/lahore_weather_1996_Dec.txt", "r+") as weatherFile:
#     line = str(weatherFile.readline())
#     while not line == "":
#         print line
#         line = weatherFile.readline()
#
#
import os


def main():
    print "WeatherMan"
    filename = os.path.abspath(os.path.join("data", "lahore_weather_1996_Dec.txt"))
    print filename
    with open(filename, 'r') as fileStream:

        titles = fileStream.readline()
        if titles == "\r\n":
            titles = fileStream.readline().strip().split(",")

        dataRows = []
        for fileLine in fileStream:

            dataMap = dict()
            if not fileLine.__contains__("<!--"):
                parsedList = fileLine.strip().split(",")

                for index, title in enumerate(titles):
                    dataMap[title] = parsedList[index]

                dataRows.append(dataMap)
        dataRows.sort(key= lambda r: r['PKT'])
        print dataRows

if __name__ == '__main__':
    main()
