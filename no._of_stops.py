full_tank_capacity     = int(input( "Enter full tank capacity " ))
Mileage          = float(input( "Enter Mileage" ))
#Distance travelled between fuel stops would be the same as we assumed mileage is constant
no_of_stops      = 560 // (full_tank_capacity * Mileage)
print(no_of_stops)
