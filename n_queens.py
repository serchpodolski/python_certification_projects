def dfs_n_queens(n: int):
    if n<1:
        return []
    solutions = []
    # State tracking sets for O(1) conflict lookups
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def dfs(row, current_board):
        # Base Case: All rows processed successfully
        if row == n:
            # Format board into standard chess visualization
            formatted_board = [
                "".join("Q" if col == c else "." for col in range(n))
                for c in current_board
            ]
            solutions.append(list(current_board))
            print(f'Valid solution:\n{"\n".join(str(i) for i in formatted_board)}')
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # Conflict found, prune search tree

            # Place queen (Choose)
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            current_board.append(col)

            # Move to next row (Explore)
            dfs(row + 1, current_board)

            # Backtrack (Unchoose)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            current_board.pop()

        

    dfs(0, [])
    return solutions


# --- Example Run for N = 4 ---
if __name__ == "__main__":
    N = 5
    results = dfs_n_queens(N)
    print(f"Total valid configurations for {N}x{N}: {len(results)}\n")
    
    for idx, board in enumerate(results, 1):
        print(f"Solution {idx}:")
        print(board)