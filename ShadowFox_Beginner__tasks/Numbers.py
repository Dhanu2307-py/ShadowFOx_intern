def format_example(number, char):
    formatted_string = "{:o}".format(number)
    return formatted_string

result = format_example(145, 'o')
print(result) #it will print the octal number 221

# Given values
radius = 84  # in meters
pi = 3.14

# Calculate the area of the pond
area_of_pond = pi * (radius ** 2)
print(f"Area of the pond: {area_of_pond} square meters")

# Calculate the total amount of water in the pond
water_per_square_meter = 1.4  # in liters
total_water = area_of_pond * water_per_square_meter

# Print the total amount of water without any decimal points
print(f"Total amount of water in the pond: {int(total_water)} liters")


# Given values
distance = 490  # in meters
time_minutes = 7  # in minutes

# Convert time to seconds
time_seconds = time_minutes * 60

# Calculate speed
speed_mps = distance / time_seconds

# Print the speed without any decimal points
print(f"Speed: {int(speed_mps)} meters per second")
