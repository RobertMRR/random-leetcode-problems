# Search a 2D Matrix
def searchMatrix(matrix, target):
    for row in matrix:
        l,r = 0, len(row)-1
        while r >= l:
            med = (r + l)//2
            if target == row[med]:
                return True
            elif target > row[med]:
                l = med + 1
            else:
                r = med - 1
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))