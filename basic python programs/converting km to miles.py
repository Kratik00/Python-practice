#for converting km into miles we had to just multiply km with 0.62137
#defining function
def converting_km_to_miles(distance):
	d = distance*0.6213271
	return d

#Taking input from users
try:
	distance = float(input("Enter distance in km: "))
	d = converting_km_to_miles(distance)
	print(f"The distance in mile is {d}.")
except ValueError:
	print("Enter the valid distance.")
