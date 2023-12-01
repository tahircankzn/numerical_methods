import numpy as np
import math
A=np.array([[1,0,0],
	[0,1,0],
	[-0.97119,-0.9719,1]],dtype=float)
	
B=np.array([[0.2425,0,-0.9701],
	  [0,0.2425,-0.9701],
	  [0,0,-2.8284]
	  ],dtype=float)
	  
result=np.array([[0,0,0],
	  [0,0,0],
	  [0,0,0]
	  ],dtype=float)
	  
for satır in range(len(A[0])):
	for sütun in range(len(B[0])):
		result[satır,sütun] = sum(A[satır,:]*B[:,sütun])
		#print(A[satır,:]*B[:,sütun])
		
		
print(result)
	