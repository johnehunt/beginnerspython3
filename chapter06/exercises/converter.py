distance_in_km_str = input('Please input the distance in kilometers:')

if distance_in_km_str.isnumeric():
    distance_in_km = int(distance_in_km_str)

    if distance_in_km < 1:
        print('You must enter a positive distance')
    else:
        print('You entered the distance', distance_in_km, 'in kilometers')
        distance_in_miles = distance_in_km * 0.6214
        print('The distance in miles is', distance_in_miles)

else:
    print('Not an integer number')
