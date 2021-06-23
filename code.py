import math

def equationroots( a, b, c):

	dis = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis))
	
	if dis > 0:
		print(" real and different roots ")
		print((-b + sqrt_val)/(2 * a))
		print((-b - sqrt_val)/(2 * a))
	
	elif dis == 0:
		print(" real and same roots")
		print(-b / (2 * a))
	
	else:
		print("Complex Roots")
		print(- b / (2 * a), " + i", sqrt_val)
		print(- b / (2 * a), " - i", sqrt_val)

a = float(input("Enter A Number : "))
b = float(input("Enter B Number : "))
c = float(input("Enter C Number : "))

if a == 0:
		print("Input correct quadratic equation")

else:
	equationroots(a, b, c)
