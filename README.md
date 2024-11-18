# Reference-Data-Encode-Decode

This code in this reposititory contains a reference Python implementations of two wspr messages that contains data.
The first reference implementation (encode-decode) uses values of humidity, pressure and temperature that follow these rules:

Pressure:
Sensor: MS561101BA03-50
Address: 0x77
Data Range: 10.0 : 999.9 hPa
Units: 000.0 hPa

Temperature:
Sensor: MCP3221A5T-I/OT
Address: 0x4D
Data Rage: -80.0 : +40.0
Units: ±00.0 C

Humidity:
Sensor: SHT41A-AD1B-R2
Address: 0x44
Data Range: 0.0 : 99.9
Units: 00.0 %RH

# Example Data
The example implementation uses the example 

humidity = 10.3     # limited to 3 digits
pressure = 210.9     # limited to 4 digits
temperature = -13.1  # limited to 3 digits
# Identifying informaiton
In addition to the data portion of the message, the message contains identification.  
The first two characters are a callsign prefix that is not assigned to any country:
For example "any letter other than A,B,F,G,I,K,M,N,W,R, + 1", "X + any number", E8, E9,J9, " letter O + any number" ,T1, T9, "U + any number"
Following the two letter prefix is a number between 0 and 9 which can be used to further identify the balloon e.g. up to 10 balloons with the prefix of B1 - B10, B12, B13, etc

The transmission of this message must be combined with a standard wspr message with a valid callsign.  Together they comprise on identified transmission. 
# Speed and direction
The second reference implementation (speed-direction) will encode and decode the following into a wspr message
     Direction in degrees
     Speed up to 150 kph
     Extended precision for grid position 5 and 6
     Fine altitude which will position the balloon altitude within +-30 m
     A balloon designator of a value of 0-9 that is chosen to identify the balloon
     A prefix of T9 which is not used by any country. There are many other prefixes
     that can be used.
Intended to be used in conjunction with wb8elk telemetry message

