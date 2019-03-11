import random


class Move:
    """ Represents a move made by a player """

    def __init__(self, counter, x, y):
        self.x = x
        self.y = y
        self.counter = counter


class Player:
    """ Represents a Player and their counter """

    def __init__(self, board):
        self.board = board

    def set_counter(self, counter):
        self.counter = counter

    def __str__(self):
        return self.__class__.__name__ + '[' + self.counter + ']'


class HumanPlayer(Player):
    """ Represents a Human Player and their behaviour """

    def __init__(self, board):
        super().__init__(board)

    def get_user_input(self, prompt):
        invalid_input = True
        while invalid_input:
            print(prompt)
            user_input = input()
            if not user_input.isdigit():
                print('Input must be a number')
            else:
                user_input_int = int(user_input)
                if user_input_int < 1 or user_input_int > 3:
                    print('input must be a number in the range 1 to 3')
                else:
                    invalid_input = False
        return user_input_int - 1

    def get_move(self):
        """ Allow the human player to enter their move """
        while True:
            row = self.get_user_input('Please input the row')
            column = self.get_user_input('Please input the column')

            if self.board.is_empty_cell(row, column):
                return Move(self.counter, row, column)
            else:
                print('That position is not free')
                print('Please try again')


class ComputerPlayer(Player):
    """ Implements algorithms for playing game """

    def __init__(self, board):
        super().__init__(board)

    def randomly_select_cell(self):
        """ Use a simplistic random selection approach
        to find a cell to fill. """
        while True:
            # Randomly select the cell
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            # Check to see if the cell is empty
            if self.board.is_empty_cell(row, column):
                return Move(self.counter, row, column)

    def get_move(self):
        """ Provide a very simple algorithm for selecting a move"""
        if self.board.is_empty_cell(1, 1):
            # Choose the center
            # self.board.add_move(self.next_player.counter, 1, 1)
            return Move(self.counter, 1, 1)
        elif self.board.is_empty_cell(0, 0):
            # Choose the top left
            # self.board.add_move(self.next_player.counter, 0, 0)
            return Move(self.counter, 0, 0)
        elif self.board.is_empty_cell(2, 2):
            # Choose the bottom right
            # self.board.add_move(self.next_player.counter, 2, 2)
            return Move(self.counter, 2, 2)
        elif self.board.is_empty_cell(0, 2):
            # Choose the top right
            # self.board.add_move(self.next_player.counter, 0, 2)
            return Move(self.counter, 0, 2)
        elif self.board.is_empty_cell(0, 2):
            # Choose the top right
            # self.board.add_move(self.next_player.counter, 2, 0)
            return Move(self.counter, 2, 0)
        else:
            # otherwise randomly select a free cell
            return self.randomly_select_cell()


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

    def add_move(self, move):
        """ A a move to the board """
        row = self.cells[move.x]
        row[move.y] = move.counter

    def is_empty_cell(self, row, column):
        """ Check to see if a cell is empty or not"""
        return self.cells[row][column] == ' '

    def check_cell(self, counter, row, column):
        """ Check to see if a cell contains the provided counter """
        return self.cells[row][column] == counter

    def is_full(self):
        """ Check to see if the board is full or not """
        for row in range(0, 3):
            for column in range(0, 3):
                if self.is_empty_cell(row, column):
                    return False
        return True

    def check_for_winner(self, player):
        """ Check to see if a player has won or not """
        c = player.counter
        return (# across the top
               (self.check_cell(c, 0, 0) and self.check_cell(c, 0, 1) and self.check_cell(c, 0, 2)) or
                # across the middle
                (self.check_cell(c, 1, 0) and self.check_cell(c, 1, 1) and self.check_cell(c, 1, 2)) or
                # across the bottom
                (self.check_cell(c, 2, 0) and self.check_cell(c, 2, 1) and self.check_cell(c, 2, 2)) or
                # down the left side
                (self.check_cell(c, 0, 0) and self.check_cell(c, 1, 0) and self.check_cell(c, 2, 0)) or
                # down the middle
                (self.check_cell(c, 0, 1) and self.check_cell(c, 1, 1) and self.check_cell(c, 2, 1)) or
                # down the right side
                (self.check_cell(c, 0, 2) and self.check_cell(c, 1, 2) and self.check_cell(c, 2, 2)) or
                # diagonal
                (self.check_cell(c, 0, 0) and self.check_cell(c, 1, 1) and self.check_cell(c, 2, 2)) or
                # other diagonal
                (self.check_cell(c, 0, 2) and self.check_cell(c, 1, 1) and self.check_cell(c, 2, 0)))


class Game:
    """ Contains the Game Playing Logic """

    def __init__(self):
        self.board = Board()
        self.human = HumanPlayer(self.board)
        self.computer = ComputerPlayer(self.board)
        self.next_player = None
        self.winner = None

    def select_player_counter(self):
        """ Let the player select which counter they want to be"""
        counter = ''
        while not (counter == 'X' or counter == 'O'):
            print('Do you want to be X or O?')
            counter = input().upper()
            if counter != 'X' and counter != 'O':
                print('Input must be X or O')
        self.human.set_counter(counter)
        if counter == 'X':
            self.computer.set_counter('Y')
        else:
            self.computer.set_counter('X')

    def select_player_to_go_first(self):
        """ Uses a random number to determine who will play first -
        the human or the computer."""
        if random.randint(0, 1) == 0:
            self.next_player = self.human
        else:
            self.next_player = self.computer

    def play(self):
        """ Main game playing loop """
        print('Welcome to TicTacToe')
        self.select_player_counter()
        self.select_player_to_go_first()
        print(self.next_player, 'will play first first')
        while self.winner is None:
            # Human players move
            if self.next_player == self.human:
                print(self.board)
                print('Your move')
                move = self.human.get_move()
                self.board.add_move(move)
                if self.board.check_for_winner(self.human):
                    self.winner = self.human
                else:
                    self.next_player = self.computer
            # Computers move
            else:
                print('Computers move')
                move = self.computer.get_move()
                self.board.add_move(move)
                if self.board.check_for_winner(self.computer):
                    self.winner = self.computer
                else:
                    self.next_player = self.human
            # Check for a winner or a draw
            if self.winner is not None:
                print('The Winner is the ' + str(self.winner))
            elif self.board.is_full():
                print('Game is a Tie')
                break

        print(self.board)


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
