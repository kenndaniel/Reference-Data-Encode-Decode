""" 
Program to encode and decode a wspr telemetry message that contains
     Direction in degrees
     Speed up to 150 kph
     Extended precision for grid position 5 and 6
     Fine altitude which will position the balloon altitude within +-30 m
     A balloon designator of a value of 0-9 that is chosen to identify the balloon
     A prefix of T9 which is not used by any country. There are many other prefixes
     that can be used.
Intended to be used in conjunction with wb8elk telemetry messageu
 K9YO 
"""

def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

pow = [0, 3, 7, 10, 13, 17, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 53, 57, 60]

def codeFineAltitude(altitude):
# fine altitude coded db position
    
    a = int(altitude) % 1000
    a = int(a/60 )

    if (a <= 0):
        a = 0
    if (a > 18):
        a = 18
    return pow[a]


# Coding/decoding arrays
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
pow = [0, 3, 7, 10, 13, 17, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 53, 57, 60]

def bit_split (n):
  # use bitwise operators to extract the bits
  a = n & 3 # get the first two bits
  b = (n >> 2) & 3 # get the next two bits
  return a, b # return a tuple of bits

def decode(prefix, bd,Grid5,Grid6,Call3,Grid1,Grid2,Grid3,Grid4,power):

    grid1 = alpha.index(Grid1)
    grid2 = alpha.index(Grid2)
    grid3 = num.index(Grid3)
    grid4 = num.index(Grid4)
    grid2 = alpha.index(Grid2)

    grid2a, grid2b = bit_split (grid2)
    # print ("grid2a =", a, "grid2a =", b)

    print(" Message type is ", prefix)

    print(" BD  is ", bd)

    # Grid square 5 and 6
    print(" Grid square 5 and 6",Grid5,Grid6)


    digits = 0
    digits = grid2b*18*26
    digits = digits + grid1 * 26
    digits = digits + call3
    speed = digits/10.
    print( " Speed is ", speed)


    direction = grid2a*100+grid3*10+grid4
    print(" Direction is ",direction)

    fineAltitude = (pow.index(int(power)))*60

    print ( " Fine altitude is ",fineAltitude )
    return



#******************* Encoding Section ****************************
prefix = "T9"
bd = 9  # balloon designator or balloon identifier can be any value 0-9
Grid5 = "A"  # grid square character 5
Grid6 = "G"  #  grid square character 6
speed = 149.9  # Speed maximum value is 150.0 m/s

direction = 360.  # degrees
Altitude = 43950.  # for fine altitude
Altitude = Altitude + 30. # correct for integer division by 60.

print( "****** Encode ******")
print(" Speed is ", speed)
print(" direction is ", direction)
print(" Altitude is ", Altitude)
print("Grid 5&6 are ",Grid5, Grid6)
print("")



speed = speed*10
# 10 10 18 18 25

value2, grid4 = divide_and_remainder(direction, 10)

value3, grid3 = divide_and_remainder(value2, 10)

value4, grid2a = divide_and_remainder(value3, 4)


value6, call3 = divide_and_remainder(speed, 26)

value5, grid1 = divide_and_remainder(value6, 18)

value4b, grid2b = divide_and_remainder(value5, 4)


print(f"grid4 is {grid4} ")
print(f"grid3 is {grid3} ")
print(f"grid2a is {grid2a} ")
print(f"value2 is {value4} must be zero")
print(f"call3 is {call3} ")
print(f"grid1 is {grid1} ")
print(f"grid2b is {grid2b} ")
print(f"value4b is {value4b} must be zero ")

# Define two variables with values between 0 and 3
a = int(grid2a)  # value will be less than 4
b = int(grid2b)  # value will be less than 4

# Zero the variable x
x = 0

# Put the first value in the lower two bits of x
x = x | (a & 3)

# Put the second value in bits 3 and 4 of x
x = x | ((b & 3) << 2)

grid2 = int(x) # Value will be less than 17
# Print the result in binary format
#print(f"grid2 b  is {bin(x)}")
print(f"grid2 i is {grid2}")

power = codeFineAltitude(Altitude)  # fine altitude per wb8elk

Grid4 = num[int(grid4)]
Grid3 = num[int(grid3)]
Grid2 = alpha[int(grid2)]
Grid1 = alpha[int(grid1)]
Call3 = alpha[int(call3)]

print(" Encoded telemetry method")
print(">>",prefix,bd,Grid5,Grid6,Call3," ",Grid1,Grid2,Grid3,Grid4," ",power,"<<")
print("")
# ********** decode section **********************************
print( "****** Decode ******")

decode(prefix, bd,Grid5,Grid6,Call3,Grid1,Grid2,Grid3,Grid4,power)



