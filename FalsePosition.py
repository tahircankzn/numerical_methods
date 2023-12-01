import math
x1 = 2
x2 = 4
x3 = None

def fonk(x):
	return x**3-2*(x**2)-5
	
for i in range(1,19):
	x3 = (fonk(x1)*x2-fonk(x2)*x1)/(fonk(x1)-fonk(x2))
		
	print(f"_________{i}__________")
	print("x1 : {}\nx2 : {}\nx3 : {}\nf(x1) : {}\nf(x2) : {}\nf(x3) : {}".format(x1,x2,x3,fonk(x1),fonk(x2),fonk(x3)))
	
	x1 = x3
	