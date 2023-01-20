#nested loop
#create a loop of below example
# 0 1 2 3
# 0 1 2 3
# 0 1 2 3

mymatrix = [[0,1,2,3],[0,1,2,3],[0,1,2,3]]

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(4):
        matrix[i].append(j)
print(matrix)

#nested list comprehension
print("Nested List Comprehension example")
MyMatrix = [[j for j in range(4)] for i in range(3)]

flatList = [i[3] for i in MyMatrix]
#print(MyMatrix)
print(flatList)