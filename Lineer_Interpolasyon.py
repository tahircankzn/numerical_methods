def Lineer_Interpolasyon(x1,y1,x2,y2,x):

    return y1 + ((y2-y1) / (x2 - x1)) * (x - x1)

result = Lineer_Interpolasyon(5,2,15,8,8)
print(result)
