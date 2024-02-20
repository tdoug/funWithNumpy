import numpy as np

#random math operations using numpy
 
a = [[2, 1], [0, 3]]
b = [[1, 1], [3, 2]]
 
# Calculating dot product using dot()
print(np.dot(b, a))

n_array = np.array([[50, 29], [30, 44]]) 
  
# Displaying the Matrix 
print("Matrix is:") 
print(n_array) 
  
# calculating the determinant of matrix 
det = np.linalg.det(n_array) 
  
print("\nDeterminant of given 2X2 matrix:") 
print(int(det)) 

# Finding an inverse of given array 
arr = np.array([[1, 2], [5, 6]]) 
inverse_array = np.linalg.inv(arr) 
print("Inverse array is ") 
print(inverse_array) 
print() 
  
# inverse of 3X3 matrix 
arr = np.array([[1, 2, 3],  
                [4, 9, 6],  
                [7, 8, 9]]) 
  
inverse_array = np.linalg.inv(arr) 
print("Inverse array is ") 
print(inverse_array) 
print() 
  
# inverse of 4X4 matrix 
arr = np.array([[1, 2, 3, 4],  
                [10, 11, 14, 25], 
                [20, 8, 7, 55],  
                [40, 41, 42, 43]]) 
  
inverse_array = np.linalg.inv(arr) 
print("Inverse array is ") 
print(inverse_array) 
print() 
  
# inverse of 1X1 matrix 
arr = np.array([[1]]) 
inverse_array = np.linalg.inv(arr) 
print("Inverse array is ") 
print(inverse_array)