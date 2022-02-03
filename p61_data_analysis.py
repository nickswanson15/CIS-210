'''
Data Analysis

CIS 210 Winter 2021 Project 6-1

Author: Nick Swanson

Credits: N/A
'''

import doctest

def mean(alist):
    '''(int) -> float

    returns the mean given a list of numbers
    
    >>> mean([2, 4, 6, 8])
    5.0
    >>> mean([1, 2, 3, 4, 5])
    3.0
    '''

    mean = sum(alist) / len(alist)
    return mean

def median(alist):
    '''(int) -> float

    return the median given a list of numbers
    
    >>> median([1, 2, 3, 4, 5, 6, 7])
    4
    >>> median([1, 2, 3])
    2
    '''

    copylist = alist[ : ]
    copylist.sort()

    if isEven(len(copylist)):
        rightmid = len(copylist) // 2
        leftmid = rightmid - 1
        median = (copylist [leftmid] + copylist[rightmid]) / 2

    else:
        mid = len(copylist) // 2
        median = copylist[mid]

    return median

def isEven(n):
    '''(int) -> boolean

    returns true if the number is even and false if the number is false
    
    >>> isEven(6)
    True
    >>> isEven(3)
    False
    '''
    if n % 2 == 0:
        return True
    else:
        return False

def mode(alist):
    '''(int) -> float

    Returns the mode given a list of numbers
    
    >>> mode([3, 3, 4, 4, 5, 5, 5])
    [5]
    >>> mode([8, 7, 6, 7])
    [7]
    '''

    countdict = { }

    for item in alist:
        if not item in countdict:
            countdict[item] = 1
        else:
            countdict[item] += 1

    countlist = countdict.values()
    maxcount = max(countlist)
    modelist = [ ]

    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)

    return modelist
    
def frequencyTable(alist):
    '''(int) -> str

    Prints the frequncy of a number given a list of numbers.
    
    > frequencyTable([1, 3, 3, 2])
    item   frequency
    1       1
    2       1
    3       2
    > frequncyTable([1, 2, 2, 3, 3, 4])
    item   frequency
    1      1
    2      2
    3      2
    4      1
    '''

    countdict = { }

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item] + 1
        else:
            countdict[item] = 1
    itemlist = list(countdict.keys())
    itemlist.sort()

    print("ITEM", "FREQUENCY")

    for item in itemlist:
        print(item, " ", countdict[item])

    genFrequencytable(countdict)

def getFrequencyTable(alist):
    '''(int) -> str

    returns a dictionary of frequncy counts that are generated from mode and frequency table.
    
    > getFrequencyTable([1, 3, 3, 2])
    {1:1, 2:1, 3:2}
    > getFrequncyTable([1, 2, 2, 3, 3, 4])
    {1:1, 2:2, 3:2, 4:1}
    '''
    freq = {}
    for item in alist:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    for key, value in freq.items():
        print('% d : % d'%(key, value))

equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3, 2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6, 4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1, 4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9, 2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7, 4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7, 3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1, 2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1, 2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3, 6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4, 2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0, 2.5,4.9, 4.9, 2.5, 4.8, 3.1, 4.9, 4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5, 4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6, 2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1, 2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1, 2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5, 4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1, 4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0, 2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2, 3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5, 2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5, 2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7, 2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6, 2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9, 2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1, 3.1, 4.6, 2.8, 3.1, 6.3]

def main(thelist):
    print('mean ' + ":" + str(mean(thelist)))
    print('median ' + ":" + str(median(thelist)))
    print('mode ' + ":" + str(mode(thelist)))
    return None

print(main(equakes))




