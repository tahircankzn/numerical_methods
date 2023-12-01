import numpy as np
			
			
arry = np.array([[10,2,1,13],
								[1,10,2,13],
								[2,1,10,13]
								])	
x1 = 0
x2 = 0
x3 = 0

epoc = 10

for i in range(epoc):
	hold_x1 = (arry[0,3] - (x2*arry[0,1] + x3*arry[0,2] ))/arry[0,0]
	hold_x2 = (arry[1,3] - (hold_x1*arry[1,0] + x3*arry[1,2] ))/arry[1,1]
	hold_x3 = (arry[2,3] - (hold_x1*arry[2,0] + hold_x2*arry[2,1] ))/arry[2,2]
	hata = abs(hold_x1-x1)+abs(hold_x2-x2)+abs(hold_x3-x3)
	
	x1 = hold_x1
	x2 = hold_x2
	x3 = hold_x3
	
	print(f"iterason {i+1} : ",hold_x1,hold_x2,hold_x3,"hata",hata,"\n")
	
	if hata < 10**(-4):
		print(f"Max epoc {i+1}")
		break
	
	
	
	