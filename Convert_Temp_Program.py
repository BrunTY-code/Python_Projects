############################################################################
# Write a function to calculate and return the wind chill based on a given 
# temperature and wind speed.                                              
############################################################################
def wind_chill(temp, mph):
    windchill_F = (
        35.74
        + (0.6215 * temp)
        - (35.75 * (mph ** 0.16))
        + ((0.4275 * temp) * (mph ** 0.16))
    )
    return windchill_F

###############################################################################
# Write a function to convert from Celsius to Fahrenheit. The formula for this
# conversion is to multiply the Celsius temperature by (9/5) and then add 32. 
###############################################################################
def convert_C_to_F(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

#############################################################################
# Allow the user to enter the temperature in Celsius of Fahrenheit. If they 
# provide it in Celsius, first convert it to Fahrenheit before using the    
# formula above.                                                            
#############################################################################
temp = int(input("What is the temperature? "))

temp_type = input("Fahrenheit or Celsius (F/C)? ").upper()


if temp_type == "C":
    temp = convert_C_to_F(temp)

###############################################################################
# Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and
# calculate and display the wind chill for each of these wind speeds.         
###############################################################################
mph = 5
while mph <= 60:
    wc = wind_chill(temp, mph)
    mph += 5
    
############################################################
# Display the wind chill value to 2 decimals of precision. 
############################################################
    print(
        f"""At the temperature of {temp}˚, and wind speed {mph-5} mph, the windchill is: {wc:.2f}˚ Fahrenheit"""
    )