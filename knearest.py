#kjikiii
#rr
# from KM
import matplotlib


class Point():

    def __init__(self, x_pos, y_pos,label ):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.label = label
    
    def get_coords(self):
        return [self.x_pos,self.y_pos]

def euclidean(point1,point2):
    x1,y1 = point1.get_coords()
    x2,y2 = point2.get_coords()

    dist = abs(x2-x1)**2 + abs(y2-y1)**2
    dist = dist**0.5
 
    return dist

def manhatten(point1,point2):
    x1,y1 = point1.get_coords()
    x2,y2 = point2.get_coords()
    
    dist = abs(x2-x1) + abs(y2-y1)

    return dist

def minkowski(point1,point2,degree):
    x1,y1 = point1.get_coords()
    x2,y2 = point2.get_coords()

    dist = abs(x2-x1)**degree + abs(y2-y1)**degree
    dist = dist**(1/degree)

    return dist

class KNN:

    def __init__(self, points,k):
        self.points = points
        self.counter = {}

    def getNearest(self, point, function):
        self.points.sort(key = lambda x: function(x,point))
        maxLabel = 0
        label = None
        for point in self.points:
            self.counter[point.label] = self.counter.get(0,point.label) + 1
            if self.counter[point.label] > maxLabel:
                label = point.label
        return label
    

def getTestData():
    """
    get test data from a database
    """
    pass

def breakData(data, training, validation, test):
    tr, va, te = [], [], []
    for i in range(training+validation+test):
        if i < training:
            tr.append(data[i])
        elif i < validation+training:
            va.append(data[i])
        else:
            te.append(data[i])
    return tr,va,te


def mainLoop():
    # training phase
    firstdata = getTestData() #parameters in here to get data

    training = 0 
    validation = 0
    test = 0
    threshold = 0
    k = 0

    tr,va,te = breakData(firstdata, training,validation, test)

    knn = KNN(training)


    # validation phase
    validity = {}
    minVal = len(training)
    for i in range(threshold):
        error = 0
        for point in knn.points:
            testLabel = knn.getNearest(point,euclidean)
            error += testLabel != point.label
        validity[i] = error
    
    # test phase

    testError = 0

    for point in test:
        testLabel = knn.getNearest(point,euclidean)
        testError += testLabel != point.label
    
    return testError
    
        
    
        





    