class Geometry(object):
    uniqueID = -1
    def __init__(self):
        Geometry.uniqueID += 1
        self.id = Geometry.uniqueID

class Point(Geometry):
    def __init__(self, x, y):
        Geometry.__init__(self)
        self.x = x
        self.y = y

    def __str__(self):
        return '(%.2f, %.2f)' % (int(self.x*100)/100.0, int(self.y*100)/100.0)


    def __eq__(self, point):
        if type(point) is Point:
            if self.x == point.x and self.y == point.y:
                return True
            else:
                return False
        else:
            raise Exception("The input parameter has to be a Point object!")

    def identify(self, other):
        if type(other) is Point:
            if self.id == other.id:
                return True
            else:
                return False
        else:
            raise Exception("The input parameter has to be a Point object!")

    def distance(self, other):
        if type(other) is Point:
            x_square = (other.x - self.x) ** 2
            y_square = (other.y - self.y) ** 2
            d = (x_square + y_square) ** 0.5
            return float(d)
        else:
            raise Exception("The input parameter has to be a Point object!")

    def quadrant(self):
        output = ""
        if self.x > 0 and self.y > 0:
            output = "Quad I"
        elif self.x < 0 and self.y > 0:
            output = "Quad II"
        elif self.x < 0 and self.y < 0:
            output = "Quad III"
        elif self.x > 0 and self.y < 0:
            output = "Quad IV"
        elif self.x == 0:
            output = "Y-axis"
        elif self.y == 0:
            output = "X-axis"
        elif self.x == 0 and self.y == 0:
            output = "Origin"

        return output

    def test():

        p1 = Point(0, 3)
        p2 = Point(-3, 7)
        p3 = Point(-3, 7)
        
        return p1, p2, p3




    def collinear(p1, p2, p3):
        p1x = p1.x
        p1y = p1.y

    # m1 = ?
    # m2 = ?


    if __name__ == "__main__":

        p1, p2, p3= test()

        #Either this 
        print "p1 is " + p1.__str__()
        print "p2 is " + p2.__str__()
        print "p3 is " + p3.__str__()

        #Or this
        print p1
        print p2
        print p3
