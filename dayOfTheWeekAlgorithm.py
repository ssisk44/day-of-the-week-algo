import datetime
import calendar

import pandas as pd

year = 2023
#
# x = calendar.Calendar(firstweekday=0).itermonthdates(2023, 1)
# for i in x:
#
#     print(i.weekday(), i.strftime("%m/%d/%Y, %H:%M:%S"))

monthNumToMonthNameDict: dict = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}
weekDayIndexToDayNameDict: dict = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def main(yearStart, yearEnd):
    allData = []
    for year in range(yearStart, yearEnd):

        calendarYearList = list(calendar.Calendar().yeardayscalendar(year, width=3))
        isLeapYear = 0
        if year % 4 == 0:
            isLeapYear = 1

        for quarterIndex in range(0, len(calendarYearList)):
            quarter = calendarYearList[quarterIndex]

            for quarterMonthIndex in range(0, len(quarter)):
                monthData = quarter[quarterMonthIndex]
                monthNum = (3 * quarterIndex) + quarterMonthIndex
                monthName = monthNumToMonthNameDict[monthNum]
                firstWeek = monthData[0]
                lastWeek = monthData[-1]
                daysInMonth = max(lastWeek)
                firstDayIndex = firstWeek.index(1)
                firstDayName = weekDayIndexToDayNameDict[firstDayIndex]
                lastDayIndex = lastWeek.index(daysInMonth)
                lastDayName = weekDayIndexToDayNameDict[lastDayIndex]
                allData.append([year, monthName, daysInMonth, firstDayName, lastDayName, isLeapYear])

    pd.DataFrame(allData, columns=["Year", "MonthName", "DaysInMonth", "MonthFirstDayDayOfWeekName", "MonthLastDayDayOfWeekName", "IsLeapYear"], index=None).to_csv('finalData.csv', index=False)

main(2000,2024)
