# Mini Chess AI
# Board representation for a reduced 5x5 chess game

BOARD_SIZE = 5

EMPTY = "."

# Uppercase = White
# Lowercase = Black
# K = King, Q = Queen, R = Rook, B = Bishop, P = Pawn

INITIAL_BOARD = [
    ["r", "q", "k", "b", "r"],
    ["p", "p", "p", "p", "p"],
    [".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P"],
    ["R", "B", "K", "Q", "R"]
]


def create_board():
    """Return a fresh copy of the starting board."""
    return [row[:] for row in INITIAL_BOARD]


def print_board(board):
    """Display the board."""
    print("\n  1 2 3 4 5")

    for row in range(BOARD_SIZE):
        print(f"{5 - row} " + " ".join(board[row]))

    print()


def is_white(piece):
    """Check whether a piece belongs to White."""
    return piece.isupper()


def is_black(piece):
    """Check whether a piece belongs to Black."""
    return piece.islower()


def is_inside(row, col):
    """Check whether a position is inside the board."""
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE
