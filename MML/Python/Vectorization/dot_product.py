import array
import time  
import numpy

#create two vectors
vector_a = array.array('f')
vector_b = array.array('f')


for i in range(100000):
	vector_a.append(i)

for i in range(100000,200000):
	vector_b.append(i)

#dot product of two vectors
start = time.clock()
for i in range(len(vector_a)):
	vector_c = vector_a[i]*vector_b[i]
stop = time.clock()
print("Using * operator",vector_c)
print(stop-start)

#dot product of two vectors using numpy
start = time.clock()
vector_d = numpy.dot(vector_a,vector_b)
stop = time.clock()
print("Using Numpy",vector_c)
print(stop-start)