import numpy as np

zPositions = np.array([0,10,20,30])

smearing   = 0.0001 

for i in np.arange(4):
    position = np.random.rand(2)
    vector   = np.random.rand(2)

    #hitPositions = position+vector*zPositions
    

    randomAddition = np.random.normal(0,smearing,2)
    
    #print(hitPositions)
    print(randomAddition)
