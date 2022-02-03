# this is Ben Robin's population dispersion project 

import statistics

# set value 
value = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

statistics.pvariance(value)

print('Variance =',statistics.pvariance(value))

print('Standard deviation =',statistics.pstdev(value))

import math
print('Another way to get standard deviation =', math.sqrt(statistics.pvariance(value)))
