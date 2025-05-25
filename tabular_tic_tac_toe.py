"""
This is based on MENACE (Matchbox Educable Noughts And Crosses Engine), which was originally created by Donald Michie. I wanted to code a version of my own to practice Python.

Notes:
- 0 represents a blank box, 1 represents an 'X', and 2 represents an 'O'
- We use base 3 to store each board state as a unique integer. Reading right-to-left, top-to-bottom, the least significant digit comes first
"""
from random import randint

def convert_state_to_number(state: list[list[int]]) -> int:
    """A function that takes in a tic-tac-toe board and returns an integer corresponding to its state.

    Parameters:
        (list) state: a list of length 9 that determines our tic-tac-toe board.
    
    Returns:
        (int): a number uniquely corresponding to the current board state.
    """
    return sum([3**(3 * i + j) * state[i][j] for i in range(3) for j in range(3)])

def convert_number_to_state(rep: int) -> list[list[int]]:
    """Takes in the unique representation integer and returns the list of length 9 corresponding to the board.

    Parameters:
        (int) rep: the unique representation integer of a board's state.
    
    Returns:
        (list): the board state.
    """
    return [(rep / 3**(3 * i + j)) % 3 for i in range(3) for j in range(3)]

def pretty_print(state: list[list[int]]) -> None:
    """Prints the current tic-tac-toe board in an easily readible way.

    Parameters:
        (list) state: a list of lists that represents our tic-tac-toe board.
    """
    # Making a new list that translates the characters
    s = [[' ' if state[i][j] == 0 else ('X' if state[i][j] == 1 else 'O') for i in range(3)] for j in range(3)]

    print('+---+---+---+')
    print(f'| {s[0][0]} | {s[0][1]} | {s[0][2]} |')
    print('+---+---+---+')
    print(f'| {s[1][0]} | {s[1][1]} | {s[1][2]} |')
    print('+---+---+---+')
    print(f'| {s[2][0]} | {s[2][1]} | {s[2][2]} |')
    print('+---+---+---+')

def random_state() -> list[list[int]]:
    """Generates a random tic-tac-toe board.

    Returns:
        (list): a list of lists representing a random board state. Not guaranteed to be a valid tic-tac-toe game.
    """
    return [[randint(0, 2) for _ in range(3)] for _ in range(3)]

def winner_q(state: list[list[int]]) -> int:
    """Takes in a board state and determines if there is a winner

    Parameters:
        (list) state: the board state.
    
    Returns:
        (int): 0 if there is no winner, 1 if the first player wins, 2 if the second player wins.
    """
    # If either '1' or '2' appears in positions where both sets of indices, compare MORE HERE
    
    # Collecting each '1' or '2' that appears in the state
    ones_positions = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 1]
    twos_positions = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 2]
    
    # Determining if the first player has won


    # Determining if the second player has won


    # In the final case, there is no winner
    return 0

# INCOMPLETE ^^^

def generate_initial_list() -> list[list[int]]:
    """Generates the initial list that our model trains on.

    Returns:
        (list): our initial training state. Each position corresponds to the unique integer representating a board state.
    """
    # There are nine choices for where we can place the MORE HERE
    return [] * 3**9