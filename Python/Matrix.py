import numpy as np
#INVERSE AND EIGENVALUES
A=np.array([[6,1,1],[4,2,5],[2,8,7]])
inv = np.linalg.inv(A)
eigval = np.linalg.eigvals(A)

#EIGENVALUES & EIGENVECTORS
B=np.array([[0,2],[2,3]])
EigenValue, EigenVector = np.linalg.eig(B)

#OUTER & INNER PRODUCT
mat1 = np.array([1,2,3,4])
mat2 = np.array([[5],[2],[1],[2]])
OuterProduct=np.outer(mat1,mat2)
InnerProduct=np.inner(mat1,mat1)
print(InnerProduct)

#DOT & CROSS PRODUCT