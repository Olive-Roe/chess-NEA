from copy import copy
import random
import time

SETUP = {
    "R": ["00", "70"],
    "N": ["10", "60"],
    "B": ["20", "50"],
    "Q": ["30"],
    "K": ["40"],
    "r": ["07", "77"],
    "n": ["17", "67"],
    "b": ["27", "57"],
    "q": ["37"],
    "k": ["47"],
    "P": ["01", "11", "21", "31", "41", "51", "61", "71"],
    "p": ["06", "16", "26", "36", "46", "56", "66", "76"],
}


def setup():
    b = [["" for _ in range(8)] for _ in range(8)]
    for piece in SETUP:
        for pos in SETUP[piece]:
            b[int(pos[0])][int(pos[1])] = piece
    return b


board = [["" for _ in range(8)] for _ in range(8)]


WHITE = list("RKBQNP")
BLACK = list("rkbqnp")

def moves(x, y, board, castling_rights):
    """Returns a list of moves, where each move is (x, y, C)\n
    C: 0-regular move, 1-capture, 2-promotion, 3-capture and promotion"""
    outputMoves = []
    piece = board[x][y]
    enemies = WHITE if piece in BLACK else BLACK
    if castling_rights:
        castle_kingside = True
        castle_queenside = True
    if piece in "Kk":
        for xo, yo in [
            [1, 1],
            [1, 0],
            [1, -1],
            [0, 1],
            [0, -1],
            [-1, 0],
            [-1, 1],
            [-1, -1],
        ]:
            xo, yo = int(xo), int(yo)
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                continue
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        # FIXME
        # attacks = all_move("white", board, castling_rights)
        attacks = []
        if (
            castle_kingside
            and board[5][0] == ""
            and board[6][0] == ""
            and (5, 0) not in attacks
            and (6, 0) not in attacks
        ):
            outputMoves.append(("O-O", 0))
        elif (
            castle_queenside
            and board[3][0] == ""
            and board[2][0] == ""
            and board[1][0] == ""
            and (3, 0) not in attacks
            and (2, 0) not in attacks
            and (1, 0) not in attacks
        ):
            outputMoves.append(("O-O-O", 0))
    elif piece in "Nn":
        for xo, yo in [
            [2, 1],
            [2, -1],
            [1, 2],
            [1, -2],
            [-1, 2],
            [-1, -2],
            [-2, 1],
            [-2, -1],
        ]:
            xo, yo = int(xo), int(yo)
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                continue
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
    elif piece in "Rr":
        yo = 0
        for xo in range(1, 8):
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            attack = board[x + xo][y + yo]
            if xo == 0 and yo == 0:
                continue
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for xo in range(-1, -8, -1):
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        xo = 0
        for yo in range(1, 8):
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for yo in range(-1, -8, -1):
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
    elif piece in "Bb":
        yo = 0
        for xo in range(1, 8):
            yo = xo
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for xo in range(-1, -8, -1):
            yo = -1 * xo
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for xo in range(1, 8):
            yo = -1 * xo
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for xo in range(-1, -8, -1):
            yo = xo
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
    elif piece in "Qq":
        yo = 0
        for xo in range(1, 8):
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for xo in range(-1, -8, -1):
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        xo = 0
        for yo in range(1, 8):
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for yo in range(-1, -8, -1):
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        yo = 0
        for xo in range(1, 8):
            yo = xo
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for xo in range(-1, -8, -1):
            yo = -1 * xo
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for xo in range(1, 8):
            yo = -1 * xo
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
        for xo in range(-1, -8, -1):
            yo = xo
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            if xo == 0 and yo == 0:
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                break
            elif attack == "":
                outputMoves.append((x + xo, y + yo, 0))
            else:  # capture
                outputMoves.append((x + xo, y + yo, 1))
    elif piece == "P":
        while True:
            xo, yo = 0, 1
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            attack = board[x + xo][y + yo]
            if attack == "":
                outputMoves.append((x + xo, y + yo, 2 if x + xo == 7 else 0))
            else:
                break
            for xo, yo in [[-1, 1], [1, 1]]:
                if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                    break
                attack = board[x + xo][y + yo]
                if attack in enemies:
                    outputMoves.append((x + xo, y + yo, 2 if x + xo == 7 else 1))
            # TODO: En passant
            if y != 1:
                break
            xo, yo = 0, 2
            if attack == "":
                outputMoves.append((x + xo, y + yo, 2 if x + xo == 7 else 0))
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            attack = board[x + xo][y + yo]
            if attack != "":
                break
            break
    elif piece == "p":
        while True:
            xo, yo = 0, -1
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            attack = board[x + xo][y + yo]
            if attack == "":
                outputMoves.append((x + xo, y + yo, 2 if x + xo == 7 else 0))
            else:
                break
            for xo, yo in [[-1, -1], [1, -1]]:
                if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                    break
                attack = board[x + xo][y + yo]
                if attack in enemies:
                    outputMoves.append((x + xo, y + yo, 2 if x + xo == 7 else 1))
            # TODO: En passant
            if y != 6:
                break
            xo, yo = 0, -2
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                break
            attack = board[x + xo][y + yo]
            if attack != "":
                break
            outputMoves.append((x + xo, y + yo, 0))
            break
    return outputMoves


def all_move(side, board, castling_rights):
    pieces = WHITE if side else BLACK
    out = []
    for i in range(8):
        for j in range(8):
            if board[i][j] in pieces:
                for move in moves(i, j, board, castling_rights):
                    if move[0] == "O-O":
                        move = (6, 0, 0) if side else (6, 7, 0)
                    elif move[0] == "O-O-O":
                        move = (1, 0, 0) if side else (1, 7, 0)
                    out.append((i, j, move[0], move[1], move[2]))
    return out


# rooks are teleporting! so are queens and possibly bishops

def attacks(x, y, board):
    moves = []
    piece = board[x][y]
    enemies = WHITE if piece in BLACK else BLACK
    if piece in "Kk":
        for xo, yo in [
            [1, 1],
            [1, 0],
            [1, -1],
            [0, 1],
            [0, -1],
            [-1, 0],
            [-1, 1],
            [-1, -1],
        ]:
            xo, yo = int(xo), int(yo)
            if (x + xo < 0 or x + xo > 7) or (y + yo < 0 or y + yo > 7):
                continue
            attack = board[x + xo][y + yo]
            if attack != "" and attack not in enemies:
                continue
            elif attack == "":
                moves.append((x + xo, y + yo, 0))
            else:  # capture
                moves.append((x + xo, y + yo, 1))


def attacks_slow(i, j, board):
    out = []
    piece = board[i][j]
    side = piece in WHITE
    # is castling rights important?
    possible_moves = moves(i, j, board, True)
    for move in possible_moves:
        if move[0] in ["O-O", "O-O-O"]:
            # Ignore castling
            continue
        if move[2] in [0, 2]:
            # Ignore non-capturing moves
            continue
        out.append((move[0], move[1], move[2], move[3]))
    return out

def all_attacks(side, board):
    targets = []
    pieces = BLACK if side else WHITE
    for i in range(8):
        for j in range(8):
            if board[i][j] in pieces:
                for attack in attacks_slow(i, j, board):
                    # Target square
                    targets.append((attack[2], attack[3]))
    return targets


def is_check(side_is_checked, board):
    breaking = False
    for i, c in enumerate(board):
        for j, r in enumerate(c):
            if side_is_checked and r == "K" or (side_is_checked is False) and r == "k":
                king_loc = (i, j)
                breaking = True
                break
        if breaking:
            break
    else:
        raise ValueError(f"No {'white' if side_is_checked else 'black'} king in board {board}")
    targets = all_attacks(side_is_checked, board)
    return king_loc in targets



# INVASIVE FUNCTIONS

def copyboard(board):
    board2 = [[] for x in range(8)]
    for i, c in enumerate(board):
        for j, r in enumerate(c):
            board2[i].append(r)
    return board2

def naivemove(move, board):
    board2 = copyboard(board)
    x1, y1, x2, y2, castle = move
    board2[x2][y2] = board2[x1][y1]
    board2[x1][y1] = ""
    return board2

# FORMATTING & AESTHETIC FUNCTIONS
def t2san(t):
    a, b, c, d, e = t
    for i in [a, b, c, d]:
        if i < 0 or i > 7:
            return t
    return list("abcdefgh")[a] + str(b + 1) + list("abcdefgh")[c] + str(d + 1)

def pprint(board):
    xb = [[] for x in range(8)]
    for i, c in enumerate(board):
        for j, r in enumerate(c):
            xb[j].append(r)
    for row in xb[::-1]:
        for cell in row:
            print("." if cell == "" else cell, end="")
        print()

# IMPORTANT FUNCTIONS

def legal_moves(side, board, castling_rights):
    pieces = WHITE if side else BLACK
    out = []
    checked = is_check(side, board)
    for i in range(8):
        for j in range(8):
            if board[i][j] in pieces:
                for move in moves(i, j, board, castling_rights):
                    b2 = copyboard(board)
                    if move[0] == "O-O":
                        move = (6, 0, 0) if side else (6, 7, 0)
                    elif move[0] == "O-O-O":
                        move = (1, 0, 0) if side else (1, 7, 0)
                    b3 = naivemove((i, j, move[0], move[1], castling_rights), b2)
                    if checked and is_check(side, b3):
                        # Didn't get out of check sadly
                        continue
                    if board[move[0]][move[1]] in "Kk":
                        # Cannot capture king
                        continue
                    out.append((i, j, move[0], move[1], move[2]))
    return out

if __name__ == "__main__":
    a = setup()
    # print(a)
    #print([t2san(move) for move in all_move(True, a, True)])
    for i in range(10000):
        movies = all_move(i % 2 == 0, a, True)
        m1 = random.choice(movies)
        a = naivemove(m1, a)
        print(t2san(m1), str((i + 1)//2))
        pprint(a)
        # time.sleep(0.5)
