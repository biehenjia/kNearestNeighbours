import random
import knearest as knn
import math

def rings(points):
    data = []
    for i in range(2):
        for j in range(points):
            angle = 2*math.pi * random.random()
            radius = 10*(i+1) + 3*random.random()
            print(angle)
            print('radius: ',radius)
            x = radius * math.cos(angle) + 25
            y = radius * math.sin(angle) + 25
            label = 'or'
            if i: label = 'ob'
            print(x,y)
            data.append(knn.Point(x,y,label))
    return data

def moons(clusters, points):
    data = []
    pointsPerCluster = points//clusters

def spots(points):
    data = []
    clusters = [(10,10),(25,40),(40,10)]
    labels = ['or','ob','oc']
    for i in range(3):
        for j in range(points):
            x = clusters[i][0] + 20*(random.random()-0.5)
            y = clusters[i][1] + 20*(random.random()-0.5)
            label = labels[i]
            data.append(knn.Point(x,y,label))
    return data
