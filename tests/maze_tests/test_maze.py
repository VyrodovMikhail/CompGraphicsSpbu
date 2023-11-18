from src.maze_solver import MazeSolver


def test_maze_solver():
    solver = MazeSolver("tests/maze_tests/1.txt")
    expected_free_set = {
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (2, 3),
        (2, 6),
        (3, 3),
        (3, 4),
        (3, 6),
        (4, 6),
        (5, 2),
        (5, 3),
        (5, 4),
        (5, 5),
        (5, 6),
        (6, 2),
        (6, 4),
        (7, 4),
    }

    for point in expected_free_set:
        assert solver.is_free(point)

    for i in range(8):
        for k in range(9):
            if (i, k) not in expected_free_set:
                assert not solver.is_free((i, k))

    new_solver = MazeSolver("tests/maze_tests/2.txt")

    for point in expected_free_set:
        assert new_solver.is_free(point)

    for i in range(8):
        for k in range(9):
            if (i, k) not in expected_free_set:
                assert not new_solver.is_free((i, k))