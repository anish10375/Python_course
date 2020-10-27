odometer_initial = int(input("Enter initial odometer reading ")) ''' assume odometer_initial is the odometer reading
...just after refueling upto the full tank capacity'''
odometer_final   = int(input("Enter final odometer reading ")) ''' assume odometer_final is the odometer reading
... when the car completely runs out of fuel'''
fuel_initial     = int(input("Enter initial fuel reading "))
fuel_final       = int(input("Enter final fuel reading "))
Mileage          = (odometer_final-odometer_initial)/(fuel_initial-fuel_final)
print(Mileage, "km/L")
