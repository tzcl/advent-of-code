import sys
import multiprocessing as mp
from functools import partial


def walk(grid, R, C, dirs, start_r, start_c):
    """
    Perform a single maze walk from a given starting point.

    :param grid: 2D grid of the maze
    :param R: Number of rows
    :param C: Number of columns
    :param dirs: Possible movement directions
    :param start_r: Starting row
    :param start_c: Starting column
    :return: Tuple of (seen path, is_loop_detected)
    """
    r, c, d = start_r, start_c, 0
    visited = set()
    seen = set()

    while True:
        if (r, c, d) in visited:
            return seen, True

        visited.add((r, c, d))
        seen.add((r, c))

        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < R and 0 <= nc < C):
            return seen, False

        if grid[nr][nc] == "#":
            d = (d + 1) % 4
        else:
            r, c = nr, nc


def parallel_process_path(grid, R, C, dirs, start_r, start_c, point_to_block):
    """
    Process a single path point in parallel.

    :param grid: 2D grid of the maze
    :param R: Number of rows
    :param C: Number of columns
    :param dirs: Possible movement directions
    :param start_r: Starting row for walk
    :param start_c: Starting column for walk
    :param point_to_block: Point to block in the grid
    :return: Whether a loop is detected
    """
    # Create a deep copy of the grid to avoid race conditions
    local_grid = [row.copy() for row in grid]

    # Block the specified point
    r, c = point_to_block
    local_grid[r][c] = "#"

    # Walk from the original start position
    _, is_loop = walk(local_grid, R, C, dirs, start_r, start_c)
    return is_loop


def main():
    # Read input
    lines = [line.strip() for line in sys.stdin]
    grid = [[c for c in line] for line in lines]

    # Grid dimensions and directions
    R = len(grid)
    assert R > 0
    C = len(grid[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Find start position
    sr, sc = None, None
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "^":
                sr, sc = r, c
                break
        if sr is not None:
            break

    # Part 1: Walk the initial path
    path, _ = walk(grid, R, C, dirs, sr, sc)
    p1 = len(path)
    print(p1)

    # Part 2: Parallel processing of path points
    with mp.Pool() as pool:
        # Create a partial function with fixed grid, R, C, dirs, start pos
        process_func = partial(parallel_process_path, grid, R, C, dirs, sr, sc)

        # Map the parallel processing function to path points
        p2_results = pool.map(process_func, path)

        # Sum the loop detections
        p2 = sum(p2_results)

    print(p2)


if __name__ == "__main__":
    main()
