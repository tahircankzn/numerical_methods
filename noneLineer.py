import math
a = 2
b = 4
x = None

def fonk(x):
	return x**3-2*(x**2)-5
	
for i in range(1,6):
	x = ((a+b)/2)
	
	print(f"_________{i}__________")
	print("a : {}\nb : {}\nx : {}\nf(a) : {}\nf(x) : {}\nişaret : {}\nhata : {}".format(a,b,x,fonk(a) ,fonk(x) ,fonk(a) * fonk(x),abs(a+b)/2))
	
	if fonk(a) * fonk(x) <= 0:
		b=x
		
	else:
		a=x
	
