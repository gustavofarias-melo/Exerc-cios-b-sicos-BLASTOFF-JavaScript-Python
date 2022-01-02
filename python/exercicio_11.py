import numpy as nump;

num = nump.array([1,2,3,4,5,6])
num2 = nump.array([2,3,4,5,8,9,0])

uniao = nump.unique(num, num2)
print(uniao)