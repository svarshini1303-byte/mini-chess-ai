from src.board import create_board, is_white, is_black, is_inside


def test_board_creation():
    board = create_board()

    assert len(board) == 5
    assert all(len(row) == 5 for row in board)


def test_white_piece():
    assert is_white("P")
    assert is_white("K")


def test_black_piece():
    assert is_black("p")
    assert is_black("k")


def test_board_position():
    assert is_inside(0, 0)
    assert is_inside(4, 4)
    assert not is_inside(-1, 0)
    assert not is_inside(5, 5)
