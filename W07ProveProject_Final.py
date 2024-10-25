""" 
CSE 110 - Intro to Programming
W07 Prove: Project - Windchill
Dollete, Eunice Ann

"""
# Converts the user_temperature to Fahrenheit
def convert_temp(temperature, scale):
    if scale.lower() == 'f':
        return temperature
    
    # if it's celcius convert it to F
    if scale.lower() == 'c':
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit

# Calculate for wind chill
def wind_chill_computation(temperature, wind_speed):
    wind_chill = 35.74 + (0.6215 * temperature) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature * (wind_speed ** 0.16))
    return wind_chill



# Main 
user_temperature = float(input('What is the temperature? '))
user_scale = input('Fahrenheit or Celcius (F/C)? ')

temperature = convert_temp(temperature=user_temperature, scale=user_scale)

# loops through 5 - 60 in 5 increments
for wind_speed in range(5, 61, 5):
    wind_chill = wind_chill_computation(temperature, wind_speed)
    print(f'At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F')