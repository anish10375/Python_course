
#fuel_initial is the full tank capacity
fuel_initial     = int(input("Enter initial fuel reading "))
Mileage          = float(input("Enter Mileage"))
#Distance travelled between fuel stops would be the same as we assumed mileage is constant
no_of_stops      = 560//(fuel_initial*Mileage)
print(no_of_stops)
