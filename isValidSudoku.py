def isValidSudoku(board):
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    rows= []
    columns = []
    boxes = []
    boxes_without_dots = []
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            if board[j][i] in digits:
                row.append(board[j][i])
        rows.append(row)
    for col in board:
        new_col = []
        for item in col:
            if item in digits:
                new_col.append(item)
        columns.append(new_col)
    for row in rows:
        if len(row) != len(set(row)):
            return False
    for col in columns:
        if len(col) != len(set(col)):
            return False
    for i in range(2,len(board),3):
        box=[]
        for j in range(2,len(board),3):
            box2=[]
            for k in range(-2+j,j+1):
                print(k)
                box2.append(board[k][-2+i:i+1])
            boxes.append(box2)
    for box in boxes:
        boxer = []
        for row in box:
            for digit in row:
                if digit in digits:
                    boxer.append(digit)
        boxes_without_dots.append(boxer)
    for box in boxes_without_dots:
        if len(box) != len(set(box)):
            return False
    return True
print(isValidSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))