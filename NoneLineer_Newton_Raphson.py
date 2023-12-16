def NL_NEWTON_RAPHSON(x1,y1,x2,y2,x):

    return y1 + ((y2-y1) / (x2 - x1)) * (x - x1)

result = NL_NEWTON_RAPHSON(5,2,15,8,8)
print(result)