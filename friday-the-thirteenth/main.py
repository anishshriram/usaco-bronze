"""
ID: ashrira1
LANG: PYTHON3
TASK: friday
"""

# read input
fin = open('friday.in', 'r')
data = fin.readlines()
fin.close()

endYear = int(data[0].strip())

daysInMonth = {0: 31, 1: 28, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}

# the result will be a dictionary, where the key is the day of the week, and the value is the number of 13ths that fell on each day
result = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# 1/1/1900 was a Monday
dayOfWeek = 0

for yearCounter in range(0, endYear):
    for monthCounter in range(0, 12):
        numDaysInMonth = daysInMonth[monthCounter]

        # handle leap years if February
        year = 1900 + yearCounter

        if year % 4 == 0 and monthCounter == 1:
            numDaysInMonth = 29

        if year % 100 == 0 and not year % 400 == 0 and monthCounter == 1:
            numDaysInMonth = 28

        for dayCounter in range(0, numDaysInMonth):
            if dayCounter == 12:
                result[dayOfWeek] += 1

            dayOfWeek += 1
            if dayOfWeek == 7:
                dayOfWeek = 0

# write output
resultString = ''
resultString += str(result[5]) + ' '
resultString += str(result[6]) + ' '
resultString += str(result[0]) + ' '
resultString += str(result[1]) + ' '
resultString += str(result[2]) + ' '
resultString += str(result[3]) + ' '
resultString += str(result[4])

fout = open('friday.out', 'w')
fout.write(resultString + '\n')
fout.close()