def decode(prefix, Calln, Call1, Call2, Call3, Grid1, Grid2, Grid3, Grid4, Power):

    #calln = num.index(Calln)
    call1 = alpha.index(Call1)
    call2 = alpha.index(Call2)
    call3 = alpha.index(Call3)
    grid1 = alpha.index(Grid1)
    grid2 = alpha.index(Grid2)
    grid3 = num.index(Grid3)
    grid4 = num.index(Grid4)
    power = pow.index(int(Power))

    digits = 0
    #digits = calln*26*26*26*18*18*10*10*19
    digits = digits + call1*26*26*18*18*10*10*19
    digits = digits + call2*26*18*18*10*10*19
    digits = digits + call3*18*18*10*10*19
    digits = digits + grid1*18*10*10*19
    digits = digits + grid2*10*10*19
    digits = digits + grid3*10*19
    digits = digits + grid4*19
    digits = digits + power

    print(f" Original value was {digits}")

    trackerNo = Calln
    humidity = int((digits)/10000000)
    pressure = int((digits - humidity*10000000)/1000)
    temperature = int((digits - humidity*10000000 - pressure *1000 ))

    humidity = humidity/10.
    pressure = pressure/10.
    temperature = (temperature/10.)-80
    print(f"trackerNo is {trackerNo} humidity is {humidity}")
    print(f" pressure is {pressure} temperature is {temperature}")



def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Input data and callsign prefix
# Message identification used in conjunction with time slot and (maybe) frequency channel
prefix = "T1"       # callsign prefix not assigned to any country
trackerNo = 8      # number to identify tracker 0-9

# Data
humidity = 14.3     # limited to 3 digits
pressure = 264.9     # limited to 4 digits
temperature = -10.1  # limited to 3 digits

humidity = 2.1     # limited to 3 digits
pressure = 233.1    # limited to 4 digits
temperature = -10.5  # limited to 3 digits

print(f" humidity is {humidity} pressure is {pressure} temperature is {temperature}")

# Need to check limits. The algorithm does not work with larger numbers.

# Encode Section ********************************

humidity = humidity *10
pressure = pressure *10
temperature = (temperature + 80) *10
# humidity = 888
# pressure = 9999
# temperature = 777

value = humidity*10000000+pressure*1000+temperature

print(f" Value is {int(value)}")

value1, power = divide_and_remainder(value, 19)

value2, grid4 = divide_and_remainder(value1, 10)

value3, grid3 = divide_and_remainder(value2, 10)

value4, grid2 = divide_and_remainder(value3, 18)

value5, grid1 = divide_and_remainder(value4, 18)

value6, call3 = divide_and_remainder(value5, 26)

value7, call2 = divide_and_remainder(value6, 26)

value, call1 = divide_and_remainder(value7, 26)

#value, calln = divide_and_remainder(value8, 10)

print(f"power is {power} ")
print(f"grid4 is {grid4} ")
print(f"grid3 is {grid3} ")
print(f"grid2 is {grid2} ")
print(f"grid1 is {grid1} ")
print(f"call3 is {call3} ")
print(f"call2 is {call2} ")
print(f"call1 is {call1} ")
#print(f"calln is {calln} ")
print(f"value is {value} ")

if value !=0  :
    print(" Error data values are too large ")


# Coding/decoding arrays
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
pow = [0, 3, 7, 10, 13, 17, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 53, 57, 60]

Power = str(pow[int(power)])
Grid4 = num[int(grid4)]
Grid3 = num[int(grid3)]
Grid2 = alpha[int(grid2)]
Grid1 = alpha[int(grid1)]
Call3 = alpha[int(call3)]
Call2 = alpha[int(call2)]
Call1 = alpha[int(call1)]
Calln = trackerNo

print ("Encoded callsign ")

# Decode Section ***********************************************


print(prefix, Calln, Call1, Call2, Call3,'\t', Grid1, Grid2, Grid3, Grid4,'\t', Power)

decode(prefix, Calln, Call1, Call2, Call3, Grid1, Grid2, Grid3, Grid4, Power)

def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

# Input data and callsign prefix
# Message identification used in conjunction with time slot and (maybe) frequency channel
prefix = "T1"       # callsign prefix not assigned to any country
trackerNo = 9      # number to identify tracker 0-9

# Data
humidity = 10.3     # limited to 3 digits
pressure = 210.9     # limited to 4 digits
temperature = -13.1  # limited to 3 digits


print(f" humidity is {humidity} pressure is {pressure} temperature is {temperature}")

# Need to check limits. The algorithm does not work with larger numbers.

# Encode Section ********************************

humidity = humidity *10
pressure = pressure *10
temperature = (temperature + 80) *10


value = trackerNo*10000000000+humidity*10000000+pressure*1000+temperature

print(f" Value is {int(value)}")

value1, power = divide_and_remainder(value, 19)

value2, grid4 = divide_and_remainder(value1, 10)

value3, grid3 = divide_and_remainder(value2, 10)

value4, grid2 = divide_and_remainder(value3, 18)

value5, grid1 = divide_and_remainder(value4, 18)

value6, call3 = divide_and_remainder(value5, 26)

value7, call2 = divide_and_remainder(value6, 26)

value8, call1 = divide_and_remainder(value7, 26)

value, calln = divide_and_remainder(value8, 10)

print(f"power is {power} ")
print(f"grid4 is {grid4} ")
print(f"grid3 is {grid3} ")
print(f"grid2 is {grid2} ")
print(f"grid1 is {grid1} ")
print(f"call3 is {call3} ")
print(f"call2 is {call2} ")
print(f"call1 is {call1} ")
print(f"calln is {calln} ")
print(f"value is {value} ")

if value !=0  :
    print(" Error data values are too large ")


# Coding/decoding arrays
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
pow = [0, 3, 7, 10, 13, 17, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 53, 57, 60]

Power = str(pow[int(power)])
Grid4 = num[int(grid4)]
Grid3 = num[int(grid3)]
Grid2 = alpha[int(grid2)]
Grid1 = alpha[int(grid1)]
Call3 = alpha[int(call3)]
Call2 = alpha[int(call2)]
Call1 = alpha[int(call1)]
Calln = num[int(calln)]

print ("Encoded callsign ")
print(prefix, Calln, Call1, Call2, Call3,'\t', Grid1, Grid2, Grid3, Grid4,'\t', Power)

# Decode Section ***********************************************

calln = num.index(Calln)
call1 = alpha.index(Call1)
call2 = alpha.index(Call2)
call3 = alpha.index(Call3)
grid1 = alpha.index(Grid1)
grid2 = alpha.index(Grid2)
grid3 = num.index(Grid3)
grid4 = num.index(Grid4)
power = pow.index(int(Power))

digits = 0
digits = calln*26*26*26*18*18*10*10*19
digits = digits + call1*26*26*18*18*10*10*19
digits = digits + call2*26*18*18*10*10*19
digits = digits + call3*18*18*10*10*19
digits = digits + grid1*18*10*10*19
digits = digits + grid2*10*10*19
digits = digits + grid3*10*19
digits = digits + grid4*19
digits = digits + power

print(f" Original value was {digits}")

trackerNo = int(digits/10000000000)
humidity = int((digits-trackerNo*10000000000)/10000000)
pressure = int((digits-trackerNo*10000000000 - humidity*10000000)/1000)
temperature = int((digits-trackerNo*10000000000 - humidity*10000000 - pressure *1000 ))

humidity = humidity/10.
pressure = pressure/10.
temperature = (temperature/10.)-80
print(f"trackerNo is {trackerNo} humidity is {humidity}")
print(f" pressure is {pressure} temperature is {temperature}")
