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
