row = ["WHITE_PAWN" for i in range(8)]
print(row)

squares = [x ** 2 for x in range(10)]
print(squares)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)

twos = [2 ** i for i in range(8)]
print(twos)

row = []

for i in range(8):
    row.append("WHITE_PAWN")
print(row)

# multi dimensional 

board = []

for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)

print(board)


boards =[["EMPTY"+str(i) for i in range(8)] for i in range(8)]
print(boards)
if boards==board:
    print(True)
else:
    print(False)

print(boards[1][2])


EMPTY = "-"
ROOK = "ROOK"
board = []

board =[[EMPTY for i in range(8)] for i in range(8)]


board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)


boards =[[0,1,2,3] for i in range(2)]
print(boards[2][0])