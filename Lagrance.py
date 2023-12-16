
"""

x1 = 1
y1 = 2

x2 = 2
y2 = 4

x3 = 3
y3 = 9

b1 = y1 / ((x1-x2) * (x1 -x3))

b2 = y2 / ((x2-x1) * (x2 -x3))

b3 = y3 / ((x3-x1) * (x3 -x2))

def fonk(b1,b2,b3,x = None):

    return b1 * (x - x2) * (x - x3) + b2 * (x - x1) * (x - x3) + b3 * (x - x1) * (x - x2)

print(fonk(b1,b2,b3,1))

"""

class Lagrance():

    def __init__(self,x_list,y_list,x):

        self.x_list = x_list
        self.y_list = y_list
        self.x = x

    def run (self):
        
        Fx = 0
        for i in range(len(self.y_list)):
            Li = 1
            for j in range(len(self.x_list)):
                if i != j:
                    Li *= ( self.x - self.x_list[j] ) / ( self.x_list[i] - self.x_list[j] )
                

            Fx += self.y_list[i] * Li

        print(Fx)


lagrance = Lagrance([1,3,6],[1,9,36],5)
lagrance.run()

    
