import array
import time  
import numpy

#create two vectors
vector_a = array.array('f')
vector_b = array.array('f')


for i in range(5):
	vector_a.append(i)

for i in range(5,10):
	vector_b.append(i)

print("Vector A: ",vector_a)
print("Vector B: ",vector_b)
vector_c = 0.0
#dot product of two vectors
start = time.clock()
for i in range(len(vector_a)):
	vector_c += vector_a[i]*vector_b[i]
stop = time.clock()
print("Using * operator",vector_c)
print(stop-start)

#dot product of two vectors using numpy
start = time.clock()
vector_d = numpy.dot(vector_a,vector_b)
stop = time.clock()
print("Using Numpy",vector_d)
print(stop-start)

cross_a = array.array('f')
cross_a = numpy.zeros((5,5))

cross_a = numpy.outer(vector_a,vector_b)
print("Cross Product",str(cross_a))


'''Element wise Product'''
multiply = numpy.zeros((5))
multiply = numpy.multiply(vector_a,vector_b)
print("multiply",str(cross_a))

'''
2d matrix'''

x = numpy.array([[1,2], [4,5]])
y = numpy.array([[4,5], [1,2]])

dot = numpy.dot(x,y)
cross = numpy.cross(x,y)
outer = numpy.outer(x,y)
mul = numpy.multiply(x,y)

print("Dot: ",dot)
print("cross: ",cross)
print("outer: ",outer)
print("mul: ",mul)








