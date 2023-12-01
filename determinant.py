A= [[17,-3,4],
         [-3,13,15],
          [2,6,6]]
 
                       
Hold = A.copy()

result=0

işlem = 0

for satır in range(1):
	for sütun in range(3):
		
		sayı = A[satır][sütun] 
		Hold.pop(satır)
		
		if sütun == 0:
			Hold = [Hold[0][1:],Hold[1][1:]]
		elif sütun == 1:
			Hold = [Hold[0][0::2],Hold[1][0::2]]
		else:
			Hold = [Hold[0][0:2],Hold[1][0:2]]
		
		det = Hold[0][0] * Hold[1][1] - Hold[0][1] * Hold[1][0]
		
		if işlem  == 0:
			result += (sayı * det)
			işlem +=1
		elif işlem == 1:
			result -= (sayı * det)
			işlem-=1
		
		
		Hold = A.copy()
		
print(result)
		
		
		
	
	
			
			

	
	