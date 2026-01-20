fuel=int(input("Please enter the fuel quantity:"))    # fuel_status_inquiry

altitude=int(input("Please enter the altitude: "))  # altitude control 

speed=int(input("Please enter the speed: "))    # speed control 


if fuel>=80 and altitude>=2000 and speed<=50:   # status verification for a safe flight
    print("You can safely land the Mars Lander.")


elif fuel<80 and altitude<500 and speed>50: # danger moment control
    print("Warning! Low fuel, high speed, YOU ARE İN DANGER.")


elif fuel>=20 and altitude<=40 and speed<=10:   # landing moment control
    print("Preparations for landing on the surface of Mars have begun. Deploy the landing gear.")


else:   # status check for other situations.
    print("Oh no! There's a problem.Conditions are not suitable for landing. Adjust your parameters.")
