def encode_data(value1, value2, prefix, telenType):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    pow_vals = [0, 3, 7, 10, 13, 17, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 53, 57, 60]
    numAlpha = num + alpha

    telen1 = 567890
    telen2 = 123456
    prefix = "Q5"

    # Encoding
    def divide_and_remainder(dividend, divisor):
        return dividend // divisor, dividend % divisor

    value1, call4 = divide_and_remainder(telen1, 26)
    value2, call3 = divide_and_remainder(value1, 26)
    value3, call2 = divide_and_remainder(value2, 26)
    value4, call1 = divide_and_remainder(value3, 36)

    if value4 != 0:
        raise ValueError("Error: Data values are too large for encoding.")
    value = telen2*4
    value5, power = divide_and_remainder(value, 19)
    value6, grid4 = divide_and_remainder(value5, 10)
    value7, grid3 = divide_and_remainder(value6, 10)
    value8, grid2 = divide_and_remainder(value7, 18)
    value, grid1 = divide_and_remainder(value8, 18)

    if value != 0:
        raise ValueError("Error: Data values are too large for encoding.")
    
    power = power +2

    # Convert to characters
    callsign = prefix[0]+numAlpha[int(call1)] + prefix[1]+ alpha[int(call2)] + alpha[int(call3)] + alpha[int(call4)]
    grid = alpha[int(grid1)] + alpha[int(grid2)] + num[int(grid3)] + num[int(grid4)]
    power_str = str(pow_vals[int(power)])

    return  callsign, grid, power_str




def decode_data(callsign, grid, power_str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    numAlpha = num + alpha
    pow_vals = [0, 3, 7, 10, 13, 17, 20, 23, 27, 30, 33, 37, 40, 43, 47, 50, 53, 57, 60]

    # Convert characters to numbers
    call1 = numAlpha.index(callsign[1])
    call3 = alpha.index(callsign[3])
    call4 = alpha.index(callsign[4])
    call5 = alpha.index(callsign[5])

    grid1 = alpha.index(grid[0])
    grid2 = alpha.index(grid[1])
    grid3 = num.index(grid[2])
    grid4 = num.index(grid[3])
    power = pow_vals.index(int(power_str))

    # Reconstruct the original value
    value1 = (call1 * 26 * 26 * 26  +
             call3 * 26 * 26  +
             call4 * 26  +
             call5 )

    value2 = (grid1 * 18 * 10 * 10 * 19 +
             grid2 * 10 * 10 * 19 +
             grid3 * 10 * 19 +
             grid4 * 19 +
             power)
    
    type = value2 % 4
    value2 = value2 / 4

    # Extract tracker number, humidity, pressure, temperature from the value
    # extracted_humidity = (value // 10000000) % 1000
    # extracted_pressure = (value // 1000) % 10000
    # extracted_temperature = value % 1000

    # # Convert back to original units
    # humidity = extracted_humidity / 10.0
    # pressure = extracted_pressure / 10.0
    # temperature = extracted_temperature / 10.0 - 80
    # temperature = round(temperature, 1)

    # return tracker_no, humidity, pressure, temperature
    return value1, value2, type



# Encoding
telen1 = 567890 # max value 
telen2 = 123456 # max value
prefix = "Q5"
type =1   # 1 or 2

callsign, grid, power_str = encode_data(telen1, telen2, prefix, type)
print(callsign, grid, power_str)


decoded_data = decode_data(callsign, grid, power_str)
print("Decoded Data:", decoded_data)



