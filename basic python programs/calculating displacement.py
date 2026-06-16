#For finding displacement we are using this formula d = (v*v - u*u)/(2*a).
#so we need to take three input from the user u(initial velocity), v(final velocity) and acceleration a.
#defining function
def finding_displacement(u, v, a):
	d = (v*v - u*u)/(2 * a)
	return d

#Takibg input from user
u = int(input("Enter initial velocity: "))
v = int(input("Enter final velocity: "))
a = int(input("Enter accelaration: "))
d = finding_displacement(u, v, a)
print(f"The displacement of a particular body would be {d}")
