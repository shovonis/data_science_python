#!/usr/bin/env python

import numpy as np

_author_ = "rifatul.islam"

a = np.array([1, 2, 3, 4, 5], float)
print(a)
print(a[:2])

a = np.array([[1, 2, 3], [4, 5, 6], [1, 1, 1]], float)
print(a)
print(a.shape)
print(a.dtype)

a = np.array([range(10)])
print(a)
print(a.reshape((5, 2)))
print(a.transpose())

a = np.array([[1, 2, 3], [4, 5, 6]], float)
print(a.flatten())

a = np.array([1, 2], float)
b = np.array([3, 4, 5, 6], float)
c = np.array([7, 8, 9], float)
print(np.concatenate((a, b, c)))

a = np.array([[1, 2], [3, 4]], float)
b = np.array([[5, 6], [7, 8]], float)
print(np.concatenate((a, b)))
print(np.concatenate((a, b), axis=1))

print(np.zeros((2, 2), float))