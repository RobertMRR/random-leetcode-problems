def tictactoe(moves):
    moves_of_a = []
    moves_of_b = []
    winning_moves=[[[0,0],[1,1],[2,2]], [[0,0],[0,1],[0,2]],[[0,0],[1,0],[2,0]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[2,0],[1,1],[0,2]]]
    for i in range(len(moves)):
        if i % 2 == 0:
            moves_of_a.append(moves[i])
        else:
            moves_of_b.append(moves[i])
   
    for winning_move in winning_moves:
        score = 0
        for move in winning_move:
            if move not in moves_of_a:
                break
            score += 1
            if score == 3:
                return "A"
        score = 0
        for move in winning_move:
            if move not in moves_of_b:
                break
            score += 1
            if score == 3:
                return "B"
    if len(moves)== 9:
        return "Draw"
    else:
        return "Pending"

print(tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
xd = 42
print(xd.bit_count())