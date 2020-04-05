"""
In these examples we will create two functions. 

1. Convert Binary to Decimal 
2. Convert Decimal to Binary

Author : Wali Morris<walimmorris@gmail.com>
"""

def binaryToDecimal(bNum):
    """
    To convert Binary to decimal we read binary numbers from right to left starting
    at 0 index, here we will call this 'i'. Binary numbers are represented by two
    digits, 1 or 0 ( on or off ). We multiply the given binary digit ( 0 or 1 ) by
    base 2^i (i being the index we are currently reading from our binary number).
    Record the each product and at the end get the sum of all product. This result
    is the decimal number or this binary representation.
    """
    bString = binaryToString(bNum) # convert binary digit to string representation
    index = 0 # reading binary digit from right to left beginning at 0 index
    size = len(bString) - 1 # length of the binary digit
    overallSum = 0
    while size >= 0: # until we reach the first digit in the binary representation, iterating in reverse
        binaryDigit = int(bString[size]) # read the current index from left to right
        baseProduct = 2 ** index # get the product of base 2 ^ of current index 
        conversionSum = binaryDigit * baseProduct # sum the product
        overallSum += conversionSum # add to overall sum
        size -= 1 # go to next digit to the left 
        index += 1 # increase the index
    return overallSum

def binaryToString(bNum): 
    """
    Converts Binary digit to its string representation
    """
    bNumString = str(bNum)
    return bNumString

def main():
    output1 = binaryToDecimal(1011)
    output2 = binaryToDecimal(110101)
    print(str(1011) + " in decimal form = " + str(output1))
    print(str(110101) + " in decimal form = " + str(output2))

if __name__ == '__main__':
    main()


import random

""" 
The general idea of a binary search is to speed up the process of finding a value in a 
given array. Things are sped up when the given array is sorted. The first and last values 
are given, and the midpoint is found. If the midpoint is the searched value, that index 
value is returned. If the given value is less than the mid point then the array can be 
broken up and the lower half searched. If the value is greater than the midpoint then the 
array can be broken up and the upper half can be searched. This process is repeated until 
the value is found or it's deemed the value isn't present in the given array.

Author : Wali Morris<walimmorris@gmail.com>
"""

def binarySearch(x, nums):
    low = 0
    high = len(nums) - 1
    while low <= high: # still items to search
        mid = (low + high) // 2 # find middle item 
        item = nums[mid]
        if x == item: # found item 
            return mid
        elif x < item:  # x is lower 
            high = mid -1 # highest value becomes the current mid point - 1
        else:
            low = mid + 1 # x is higher; lowest value becomes midpoint + 1
    return -1 # x is not in list 

def longList(x):
    """ This method creates a long list of random integers between 0 and 100. 
    The parameter x represents how many integers to create. Returns a sorted 
    array of x values. 
    """
    array = []
    while len(array) < x:
        r = random.randint(1, 100) # establish random number
        if r not in array: # no duplicates
            array.append(r) # if r is not a duplicate, append to array
        array.sort()
    return array

def main():
    array = longList(25) # create an array of 25
    print(array)
    x = 44 # find this value 
    item = binarySearch(x, array) # search for x in array
    if item == -1:
        print(str(x) + " is not in the list")
    else:
        print(str(x) + " is at index: " + str(item))

if __name__ == '__main__':
    main()
    
 

"""
The idea of a linear search is to loop through an array of values one by one 
until the value being searched is found or the array is searched and the given 
value isn't present. This algorithm represents a linear search. 

Author : Wali Morris<walimmorris@gmail.com>
"""

def linearSearch(x, nums):
    """ This method receives two arguments, the value to search(x) and nums(array).
    The value x will be returned once found. -1 will be returned if x is not present.
    """
    for i in range(len(nums)):
        if nums[i] == x: # x was found, return index value
            return i
    return -1 # loop has processed and x was not found in array

def main():
    x = 10
    array = [1, 10, 5, 15, 22, 44]
    arrayValue = linearSearch(x, array)
    print(str(x) + " is at index: " + str(arrayValue))

if __name__ == '__main__':
    main()
