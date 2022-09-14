import numpy as np

x = np.array([[0.25,0.15,0],[0.45,0.50,0.75],[0.30,0.35,0.25]])
r = np.array([1500,5000,3000])

def crammer():
    dx = np.linalg.det(x)
    results = "ABC"
    if dx==0:
        return 0
    for i in range(3):
        y = np.copy(x)
        y[0,i]=r[0]
        y[1,i]=r[1]
        y[2,i]=r[2]
        temp = np.linalg.det(y)
        print("{} = {}".format(results[i],temp/dx))
    return 1

def numpysolver():
    solution = np.linalg.solve(x,r)
    print(solution)
    return 1

crammer()
numpysolver()