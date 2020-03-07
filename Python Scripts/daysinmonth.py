# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:47:00 2020

@author: CEC
"""
def isYearLeap(year):
    if year%4!=0:
        return False
    elif year%100!=0:
        return True
    elif year%400!=0:
        return False
    else:
        return True
#
#print(str(isYearLeap(2020)))
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")


#
diasMeses=[31,28,31,30,31,30,31,31,30,31,30,31]
def daysInMonth(year, month):
#

    if isYearLeap(year)==True:
        diasMeses[1]=29
        if month>=13 or month<=0:
            return None
        else:
            return diasMeses[month-1]
    else:
        if month>=13 | month<=0:
            return None
        else:
            return diasMeses[month-1]
#print(str(daysInMonth(2020,2)))


def dayOfYear(year, month, day):
    dias=0

    #print(day)
    #print(daysInMonth(year,month))
    if  daysInMonth(year,month)==None:
        return None
    elif day > daysInMonth(year,month) or day<1:
        return None
    else:
        for i in range(month-1):
            dias=dias+daysInMonth(year, i+1)
        return dias+day    
#

print(dayOfYear(2020, 12,31 ))
