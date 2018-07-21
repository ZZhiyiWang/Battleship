# Use these constants in your code 

MIN_SHIP_SIZE = 1
MAX_SHIP_SIZE = 10
MAX_GRID_SIZE = 10
UNKNOWN = '-'
EMPTY = '.'
HIT = 'X'
MISS = 'M'


def read_ship_data(game_file):
    """ (file open for reading) -> list of list of objects

    Return a list containing the ship characters in game_file as a list of \
    strings at index 0, and ship sizes in game_file as a list of ints at index \
    1.
    """

    # complete the function body for read_ship_data here
    # the method readline() reads one entire line from the file every time
    
    char_lst = game_file.readline().split()
    int_lst = game_file.readline().split()
    for i in range(len(int_lst)):
        int_lst[i] = int(int_lst[i])

    return [char_lst, int_lst]


# Write the rest of the required functions here
# Don't forget to follow the Function Design Recipe


def has_ship(fleet_grid, row, column, ship_character, ship_size):
    """ (list of list of str, int, int, str, int) -> bool
    
    Return true iff the ship appears with the correct size, the ship is \
    completely in a row or in a column at the given starting cell. Otherwise, \
    return false.
    
    >>> has_ship([['a', 'a'], ['b', '.']], 0, 0, 'a', 2)
    True
    >>> has_ship([['a', 'a'], ['b', '.']], 0, 1, 'b', 1)
    False
    """
    
    # ship_size is between MIN_SHIP_SIZE and MAX_SHIP_SIZE
    # fleet_grid is a square potential fleet grid
    
    count1 = 0
    count2 = 0
    if column + ship_size <= len(fleet_grid):
        for i in range(ship_size):
            if fleet_grid[row][(column + i)] == ship_character:
                count1 += 1
    if row + ship_size <= len(fleet_grid):
        for i in range(ship_size):
            if fleet_grid[row + i][column] == ship_character:
                count2 += 1

    return count1 == ship_size or count2 == ship_size


def validate_character_count(fleet_grid, list_of_ship_characters,
                             list_of_ship_sizes):
    """ (list of list of str, list of str, list of int) -> bool
    
    Return true iff the grid contains the correct number of ship characters \ 
    for each ship on the square fleet grid, also has the correct number of \
    empty characters.
    
    >>> validate_character_count([['a', 'a'], ['b', '.']], ['a', 'b'], [2, 1])
    True
    >>> validate_character_count([['a', 'a'], ['b', 'b']], ['a', 'b'], [1, 1])
    False
    """

    # EMPTY is the symbol used to display a cell on a fleet grid that is not \
    # covered by a ship
    # length_of_ship counts the number of appearance of each ship in the \
    # fleet_grid.
    
    for i in range(len(list_of_ship_characters)):
        length_of_ship = 0
        num_of_empty = 0
        for row in fleet_grid:
            for column in row:
                if column == list_of_ship_characters[i]:
                    length_of_ship = length_of_ship + 1
                elif column == EMPTY:
                    num_of_empty = num_of_empty + 1
        if length_of_ship != list_of_ship_sizes[i]:
            return False
        elif num_of_empty != (len(fleet_grid) ** 2) - sum(list_of_ship_sizes):
            return False
    return True


def validate_ship_positions(fleet_grid, list_of_ship_characters,
                            list_of_ship_sizes):
    """ (list of list of str, list of str, list of int) -> bool
    
    Return true iff the grid contains each ship aligned completely in a row or \
    colum, which means the ship is oriented horizontally or vertically.
    
    >>> validate_ship_positions([['a', 'a'], ['b', '.']], ['a', 'b'], [2, 1])
    True
    >>> validate_ship_positions([['a', 'a', 'b'], ['.', 'b', 'b'], \
    ['.', '.', 'b']], ['a', 'b'], [2, 2])
    False
    """
    
    # row_index is a list contains every ship character's row index.
    # column_index is a list contains every ship character's column index.
    # return True iff either row_index or column_index is a list which all \
    # elements in it are equal.
    
    for i in range(len(list_of_ship_characters)):
        row_index = []
        column_index = []

        for j in range(len(fleet_grid)):
            for k in range(len(fleet_grid[j])):
                if fleet_grid[j][k] == list_of_ship_characters[i]:
                    row_index.append(j)
                    column_index.append(k)
        for l in range(len(row_index)):
            x = row_index[0]
            y = column_index[0]
            if row_index[l] != x and column_index[l] != y:
                return False
    return True


def validate_fleet_grid(fleet_grid, list_of_ship_characters,
                        list_of_ship_sizes):
    """ (list of list of str, list of str, list of int) -> bool
    
    Return true iff the potential fleet grid is a valid fleet grid. It must \
    contains the correct number of ship characters and the correct number of \
    EMPTY characters. Also must have ships placed in consecutive cells.
    
    >>> validate_fleet_grid([['a', 'a'], ['b', '.']], ['a', 'b'], [2, 1])
    True
    >>> validate_fleet_grid([['a', 'a', 'b'], ['b', '.', 'b'], \
    ['b', '.', '.']], ['a', 'b'], [2, 2])
    False
    """

    # use validate_character_positions as the help function to check if every \
    # ship completely placed in  a row or a column.
    # use validate_character_count as the help functionon to check if every \
    # ship only appears once.

    return validate_character_count(fleet_grid, list_of_ship_characters,
                                    list_of_ship_sizes) == True and \
           validate_ship_positions(fleet_grid, list_of_ship_characters,
                                   list_of_ship_sizes) == True


def valid_cell(row, column, grid_size):
    """ (int, int, int) -> bool
    
    Return True iff the cell specified by the row and the column is a valid \
    cell inside a square grid of that size.
    
    >>> valid_cell(2, 2, 10)
    True
    >>> valid_cell(10, 20, 3)
    False
    """

    return row <= grid_size - 1 and column <= grid_size - 1


def is_not_given_char(row, column, grid, given_character):
    """ (int, int, list of list of str, str) -> bool
    
    Return True iff the cell specified by the row and column is not the given \
    character. Otherwise, return False.
    
    >>> is_not_given_char(0, 0, [['a', 'a'], ['b', '.']], 'a')
    False
    >>> is_not_given_char(0, 0, [['a', 'a'], ['b', '.']], 'b')
    True
    """

    return grid[row][column] != given_character


def update_fleet_grid(row, column, fleet_grid, list_of_ship_characters,
                      list_of_ship_sizes, hits_list):
    """ (int, int, list of list of str, list of str, list of int, list of int) \
    -> NoneType
    
    This function updates the fleet grid and also the hits list to indicate \
    that there has been a hit on a ship.
    
    >>> fleet_grid = [['a', 'a'], ['b', '.']]
    >>> hits_list = [0, 0]
    >>> update_fleet_grid(0, 0, fleet_grid,['a', 'b'], [2, 1], hits_list)
    >>> fleet_grid
    [['A', 'a'], ['b', '.']]
    >>> hits_list 
    [1, 0]
    
    >>> fleet_grid = [['A', 'a'], ['b', '.']]
    >>> hits_list = [1, 0]
    >>> update_fleet_grid(0, 1, fleet_grid,['a', 'b'], [2, 1], hits_list)
    >>> fleet_grid
    [['A', 'A'], ['b', '.']]
    >>> hits_list 
    [2, 0]
    """

    # HIT is a symbol used to display a cell on a target grid
    # sunk_message is printed when a ship is sunk.
    
    if fleet_grid[row][column] != '.':
        i = list_of_ship_characters.index(fleet_grid[row][column])
        if (hits_list[i] == list_of_ship_sizes[i] and
                    fleet_grid[row][column] == list_of_ship_characters):
            print_sunk_message(list_of_ship_sizes[i],
                               list_of_ship_characters[i])

        elif not fleet_grid[row][column].isupper():
            fleet_grid[row][column] = fleet_grid[row][column].upper()
            hits_list[i] += 1


def update_target_grid(row, column, target_grid, fleet_grid):
    """ (int, int, list of list of str, list of list of str) -> NoneType
    
    This function updates the element of the specified cell in the target grid \
    to HIT or MISS using the information from the corresponding cell from the \
    fleet grid.
    
    >>> target_grid = [['-', '-'], ['-', '-']]
    >>> update_target_grid(0, 0, target_grid, [['a', 'a'], ['b', '.']])
    >>> target_grid
    [['X', '-'], ['-', '-']]
   
   
    >>> target_grid = [['-', '-'], ['-', '-']]
    >>> update_target_grid(1, 1, target_grid, [['a', 'a'], ['b', '.']])
    >>> target_grid
    [['-', '-'], ['-', 'M']]
    """
    
    # EMPTY is a symbol used to display a cell on a fleet grid
    # MISS is a symbol used to display a cell on a target grid when the player \
    # does not hit the ship.
    # HIT is a symbol used to display a cell on a target grid when the player \
    # hits the ship.

    if fleet_grid[row][column] == EMPTY:
        for i in range(len(target_grid[row])):
            if i == column:
                target_grid[row][i] = MISS
    else:
        for j in range(len(target_grid[row])):
            if j == column:
                target_grid[row][j] = HIT


def is_win(list_of_ship_sizes, hits_list):
    """ (list of int, list of int) -> bool
    
    Return True iff the number of hits for each ship in the hits list is the \
    same as the size of each ship.
    
    >>> is_win([1,2,3,4,5], [1,2,3,4,5])
    True
    >>> is_win([2,3,4,5,6], [1,3,3,5,6])
    False
    """
    
    return list_of_ship_sizes == hits_list

##################################################
## Helper function to call in update_fleet_grid
## Do not change!
##################################################

def print_sunk_message(ship_size, ship_character):
    """ (int, str) -> NoneType
  
    Print a message telling player that a ship_size ship with ship_character
    has been sunk.
    """

    print('The size {0} {1} ship has been sunk!'.format(ship_size, ship_character))


if __name__ == '__main__':
    import doctest
    # uncomment the line below to run the docstring examples     
    # doctest.testmod()
