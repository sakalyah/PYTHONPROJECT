from math import sin

import numpy
import array as arr

values = arr.array('i',[1,2,3,4,5,6])
print(values.buffer_info())
print(values.typecode)

newarr = arr.array(values.typecode,(a for a in values))
print(newarr)
array = numpy.array([23,45,56,43,54],int)
print (array)
linspacearrays =numpy.linspace(0,20,20)
print(linspacearrays)
arangearrays = numpy.arange(0,15,2)
print(arangearrays)
logspacearrays=numpy.logspace(0,5,6)
print(logspacearrays)
zeroarrays = numpy.zeros(14)
print(zeroarrays)
onearrays = numpy.ones(14)
print(onearrays,zeroarrays,logspacearrays,arangearrays,linspacearrays)
Arraysss=onearrays + 5
print((Arraysss))
Arraysss = Arraysss + zeroarrays
print((numpy.sin(Arraysss)))
arr1 = Arraysss #Copy of Array where memory address will be same.
print(id(arr1),id(Arraysss))
arr2 = arr1.view()
arr3 = arr1.copy()
print(id(arr2))
print(id(arr3))
#Matrices
arr4 = numpy.array([[1,2,3,4,5,6],[4,5,6,100,2000,3000]])
print(arr4.dtype,arr4.ndim,arr4.shape,arr4.size)
print(arr4.flatten())
print(arr4.reshape(3,1,4))#Should Understand.





