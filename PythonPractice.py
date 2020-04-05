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
    while size >= 0: 
    # until we reach the first digit in the binary representation, iterating in reverse
        binaryDigit = int(bString[size]) 
        baseProduct = 2 ** index  
        conversionSum = binaryDigit * baseProduct
        overallSum += conversionSum 
        size -= 1  
        index += 1 
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

    
# A quick review of exercises from Professor John Zelle's Introduction to Computer Science : Python Programming
""" 
Exercise 2: Enter and run the chaos program from section 1.6. Try it out 
with various values of input to see that it functions as described 
in the chapter. The chaos program: 
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10): 
        x = 3.9 * x * (1 - x)
        print(x)
Author : Wali Morris 
File   : exercise2.py 
Date   : 02/08/2020
"""

def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: ")) # allows experiementation with diff x values
    y = int(input("Enter a range: ")) # allows experimentation with diff ranges 
    for i in range(y):
        x = 3.9 * x * (1 - x)
        print(x)

if __name__ == '__main__':
    main()

""" 
Exercise 3: Modify the chaos program using 2.0 in place of 3.9 as the multiplier 
in the logistic function. Run the program for various input values and 
compare the results to those obtained from the original program. Write
a short paragraph describing any differences that you notice in the 
behavior of the two versions.
Author : Wali Morris 
File   : exercise3.py
Date   : 02/08/2020 
"""

"""
Takes a floating point argument(x) as the multiplier and integer point(y)
as range to illustrate a chaotic function.
"""
def chaosVersion1(x, y):
     print("This program illustrates a chaotic function with mulitplier 3.9")
     print("---------------------------------------------------------------")
     for i in range(y):
        x = 3.9 * x * (1 - x) # using 3.9 multiplier 
        print(str(i+1) + ": " + str(x))
     print()

"""
Takes a floating point argument(x) as the multiplier and integer point(y)
as range to illustrate a chaotic function. 
"""

def chaosVersion2(x,y):
    print("This program illustrates a choatic function with multiplier 2.0")
    print("---------------------------------------------------------------")
    for i in range(y):
        x = 2.0 * x * (1 - x) # using 2.0 multiplier 
        print(str(i+1) +  ": " + str(x))
    print()

def main():
    chaosVersion1(.45, 5)
    chaosVersion2(.45, 5)

if __name__ == '__main__':
    main()

""" 
My observation: As the multiplier decreases, the chaos of the function decreases. 
As the multiplier increases so does the chaotic nature of the function. 
"""

""" Exercise 4: Modify the chaos program so that it prints out 20 values instead of 10. 
Author : Wali Morris
File   : exercise4.py
Date   : 02/08/2020
"""

def main():
    print("This program illustrates a chaotic function")
    print("-------------------------------------------")
    x = .57
    y = 20
    for i in range(y):
        x = 3.9 * x * (1 - x)
        print(str(i+1) + ": " + str(x))

if __name__ == '__main__':
    main()

""" 
Exercise 5: Modify the chaos program so that the number of values to 
print is determined by the user. 
Author : Wali Morris
File   : exercise5.py
Date   : 02/08/2020
"""

def main():
    print("This program illustrates an chaotic function")
    print("--------------------------------------------\n")
    x = float(input("Choose a number between 0 and 1: "))
    y = int(input("How many numbers should I print: "))
    print("---------------------------------\n")
    for i in range(y):
        x = 3.9 * x * (1 - x)
        print(str(i+1) + ": " + str(x))

if __name__ == '__main__':
    main()

    """ 
Exercise 6: The calculation performed in the chaos program can be written in 
a number of ways that are algebraically equivalent. Write a version of the 
program for each of the ways of doing the computation. Have your modified 
program print out 100 iterations of the calculation and compare the results 
on the same input.
Author : Wali Morris
File   : exercise6.py
Date   : 02/08/2020 
"""
def chaosVersionOne(x, y):
    """
    The first and original calculation version of the chaotic function. Takes a x
    parameter for the multiplier and a y parameter for the number of iterations
    """
    print("\nChoatic Function Version 1: 3.9 * x * (1 - x) Multiplier: " + str(x))
    print("--------------------------------------------------------------")
    for i in range(y):
        x = 3.9 * x * (1 - x)
        print(str(i+1) + ": " + str(x))

def chaosVersionTwo(x, y):
    """
    The second calculation version of the chaotic function. Takes a x parameter for 
    the multiplier and a y parameter for the number of iterations
    """
    print("\nChoatic Function Version 2: 3.9 * (x - x * x) Multiplier: " + str(x))
    print("--------------------------------------------------------------")
    for i in range(y):
        x = 3.9 * x * (1 - x)
        print(str(i+1) + ": " + str(x))

def chaosVersionThree(x, y):
    """
    The third calculation version of the chaotic function. Takes a x parameter for
    the multiplier and a y parameter for the number of iterations
    """
    print("\nChoatic Function Version 3: 3.9 * x  - 3.9 * x * x Multiplier: " + str(x))
    print("-------------------------------------------------------------------")
    for i in range(y):
        x = 3.9 * x -3.9 * x * x
        print(str(i+1) + ": " + str(x))


def main():
    print("\nThis program illustrates three different versions of a chaotic function")
    print("-----------------------------------------------------------------------")
    y = 100
    x = float(input("Enter a number between 0 and 1: "))
    chaosVersionOne(x, y)
    chaosVersionTwo(x, y)
    chaosVersionThree(x, y)


if __name__ == '__main__':
    main()

    """
Modify the chaos program so that it accepts two inputs and then prints a 
tables with two columns similar to the one shown in Section 1.8
Author : Wali Morris
File   : exercise7.py
Date   : 02/08/2020
"""

def chaos(x):
    """
    Helper function to calculate a chaotic function. Has one parameter(x)
    to return the calculation
    """
    x = 3.9 * x * (1 - x)
    return x

def main():
    print("\nThis program reports two tables both illustrating chaotic functions")
    print("with two different mulitpliers")
    print("-------------------------------------------------------------------\n")
    y = 10
    x1 = float(input("Enter a number between 0 and 1(Multiplier 1): "))
    x2 = float(input("Enter a number between 0 and 1(Multiplier 2): "))
    print( str(x1) + "             " + str(x2))
    print("--------------------------------")
    for i in range(y):
        """
        for every loop both the product and x1 and x2 is printed on the same line
        using formatting and space. The chaos helper function is first callled, 
        results are printed and then both x1 and x2 is updated to continue the 
        computations
        """
        x1Product = chaos(x1)
        x2Product = chaos(x2)
        print("{0:0.5f}         {1:0.5f}".format(x1Product, x2Product))
        x1 = x1Product
        x2 = x2Product
        
if __name__ == '__main__': 
    main() 
