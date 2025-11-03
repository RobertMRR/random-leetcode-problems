# Matrix Diagonal Sum
def diagonalSum(mat):
    sum = 0
    visited = []
    y = 0
    for i in range(len(mat)):
        sum += mat[i][i]
        visited.append([i,i])
    for i in range(len(mat)-1,-1,-1):
        if [y,i] not in visited:
            sum += mat[y][i]
        y += 1
    return sum

print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
    