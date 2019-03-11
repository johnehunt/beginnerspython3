import random


class Player:
    """ Represents a Player and their counter """

    def __init__(self, type):
        self.type = type

    def set_letter(self, letter):
        self.letter = letter

    def __str__(self):
        return self.type + '[' + self.letter + ']'


class Board:
    """ The ticTacToe board"""

    def __init__(self):
        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # List of lists
        self.separator = '\n' + ('-' * 11) + '\n'

    def __str__(self):
        row1 = ' ' + self.cells[0][0] + ' | ' + self.cells[0][1] + ' | ' + self.cells[0][2]
        row2 = ' ' + self.cells[1][0] + ' | ' + self.cells[1][1] + ' | ' + self.cells[1][2]
        row3 = ' ' + self.cells[2][0] + ' | ' + self.cells[2][1] + ' | ' + self.cells[2][2]
        return row1 + self.separator + row2 + self.separator + row3

    def add_move(self, letter, x, y):
        row = self.cells[x]
        row[y] = letter

    def is_empty_cell(self, row, column):
        return self.cells[row][column] == ' '

    def check_cell(self, letter, row, column):
        return self.cells[row][column] == letter

    def is_full(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for row in range(0, 3):
            for column in range(0, 3):
                if self.is_empty_cell(row, column):
                    return False
        return True

    def check_for_winner(self, player):
        player = player.letter
        return ((self.check_cell(player, 0, 0) and self.check_cell(player, 0, 1) and self.check_cell(player, 0,
                                                                                           2)) or  # across the top
                (self.check_cell(player, 1, 0) and self.check_cell(player, 1, 1) and self.check_cell(player, 1,
                                                                                           2)) or  # across the middle
                (self.check_cell(player, 2, 0) and self.check_cell(player, 2, 1) and self.check_cell(player, 2,
                                                                                           2)) or  # across the bottom
                (self.check_cell(player, 0, 0) and self.check_cell(player, 1, 0) and self.check_cell(player, 2,
                                                                                           0)) or  # down the left side
                (self.check_cell(player, 0, 1) and self.check_cell(player, 1, 1) and self.check_cell(player, 2,
                                                                                           1)) or  # down the middle
                (self.check_cell(player, 0, 2) and self.check_cell(player, 1, 2) and self.check_cell(player, 2,
                                                                                           2)) or  # down the right side
                (self.check_cell(player, 0, 0) and self.check_cell(player, 1, 1) and self.check_cell(player, 2, 2)) or  # diagonal
                (self.check_cell(player, 0, 2) and self.check_cell(player, 1, 1) and self.check_cell(player, 2, 0)))  # diagonal

class Game:
    """ Contains the Game Playing Logic """

    def __init__(self):
        self.board = Board()
        self.human = Player('Human')
        self.computer = Player('Computer')
        self.next_player = None

    def get_user_input(self, prompt):
        invalid_input = True
        while invalid_input:
            print(prompt)
            user_input = input()
            if not user_input.isdigit():
                print('Input must be a number')
            else:
                user_input_int = int(user_input)
                if user_input_int < 0 or user_input_int > 2:
                    print('input must be a number in the range 0 to 2')
                else:
                    invalid_input = False
        return user_input_int

    def select_first_player(self):
        if random.randint(0, 1) == 0:
            self.next_player = self.human
        else:
            self.next_player = self.computer

    def select_player_letter(self):
        """ Let the player select which letter they want to be"""
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()
            if letter != 'X' and letter != 'O':
                print('Input must be X or O')
        self.human.set_letter(letter)
        if letter == 'X':
            self.computer.set_letter('Y')
        else:
            self.computer.set_letter('X')

    def get_human_move(self):
        """ Allow the human player to enter their move """
        invalid_position = True
        while invalid_position:
            row = self.get_user_input('Please input the row')
            column = self.get_user_input('Please input the column')

            if self.board.is_empty_cell(row, column):
                invalid_position = False
                self.board.add_move(self.next_player.letter, row, column)
            else:
                print('That position is not free')
                print('Please try again')

    def randomly_select_cell(self):
        free_cell_not_found = True
        while free_cell_not_found:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if self.board.is_empty_cell(row, column):
                self.board.add_move(self.next_player.letter, row, column)
                free_cell_not_found = False

    def make_computer_move(self):
        """ Provide a very simple algorithm for selecting a move"""
        if self.board.is_empty_cell(1, 1):
            # Choose the center
            self.board.add_move(self.next_player.letter, 1, 1)
        elif self.board.is_empty_cell(0, 0):
            # Choose the top left
            self.board.add_move(self.next_player.letter, 0, 0)
        elif self.board.is_empty_cell(2, 2):
            # Choose the bottom right
            self.board.add_move(self.next_player.letter, 2, 2)
        elif self.board.is_empty_cell(0, 2):
            # Choose the top right
            self.board.add_move(self.next_player.letter, 0, 2)
        elif self.board.is_empty_cell(0, 2):
            # Choose the top right
            self.board.add_move(self.next_player.letter, 2, 0)
        else:
            # otherwise randomly select a free cell
            self.randomly_select_cell()

    def play(self):
        print('Welcome to TicTacToe')
        self.select_player_letter()
        self.select_first_player()
        print(self.next_player, 'will play first first')
        winner = None  # None represents the absence of a value
        while winner is None:
            print(self.board)
            # Human players move
            if self.next_player == self.human:
                print('Your move')
                self.get_human_move()
                if self.board.check_for_winner(self.human):
                    winner = self.human
                else:
                    self.next_player = self.computer
            # Computers move
            else:
                print('Computers move')
                self.make_computer_move()
                if self.board.check_for_winner(self.computer):
                    winner = self.computer
                else:
                    self.next_player = self.human
            # Check for a winner or a draw
            if winner is not None:
                print('The Winner is the ' + str(winner))
            elif self.board.is_full():
                print('Game is a Tie')
                break

        print(self.board)


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
