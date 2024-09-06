def isValid(list):
    seen = set()
    for cells in list:
        if cells == ".":
            pass
        else:
            if cells in seen:
                return False
            elif cells not in seen:
                seen.add(cells)

def row_checker(sudoku):
    for rows in sudoku:
        if isValid(rows) == False:
            return False
        else:
            pass

def column_checker(sudoku):
    curr_column = []
    for column in range(9):
        for index in range(9):
            curr_column.append(sudoku[column][index])
        if isValid(curr_column) == False:
            return False
        else:
            curr_column = []

def grid_checker(sudoku):
    # Initialize variables for subgrid column indices
    a = 0
    a1 = 0
    b1 = 1
    c1 = 2
    
    # Iterate over 3 main subgrid rows
    for x in range(3):
        # Iterate over 3 main subgrid columns
        for y in range(3):
            # Collect the 3x3 subgrid elements
            curr_list = [
                sudoku[a][a1], sudoku[a][b1], sudoku[a][c1],
                sudoku[a + 1][a1], sudoku[a + 1][b1], sudoku[a + 1][c1],
                sudoku[a + 2][a1], sudoku[a + 2][b1], sudoku[a + 2][c1]
            ]
            
            # Check if the subgrid is valid
            if not isValid(curr_list):
                return False
            
            # Move to the next set of subgrid columns
            a1 += 3
            b1 += 3
            c1 += 3
        
        # Reset the column indices and move down 3 rows for the next subgrid row
        a1 = 0
        b1 = 1
        c1 = 2
        a += 3
    
    return True


        

def isValidSudoku(List):

    if row_checker(List) == False:
        return False
    if column_checker(List) == False:
        return False
    if grid_checker(List) == False:
        return False
    else:
        return True

print(isValidSudoku([[".",".","4",".",".",".","6","3","."],
                     [".",".",".",".",".",".",".",".","."],
                     ["5",".",".",".",".",".",".","9","."],
                     [".",".",".","5","6",".",".",".","."],
                     ["4",".","3",".",".",".",".",".","1"],
                     [".",".",".","7",".",".",".",".","."],
                     [".",".",".","5",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".","."],
                     [".",".",".",".",".",".",".",".","."]]))