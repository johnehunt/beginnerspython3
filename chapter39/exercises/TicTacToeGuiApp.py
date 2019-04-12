import wx
from abc import ABCMeta, abstractmethod
import random


class TicTacToeButton(wx.Button):
    """ Version of a button that knows its
    position within a grid layout"""

    def __init__(self, parent=None, label=None, row=0, col=0):
        super().__init__(parent=parent, label=label)
        self.row = row
        self.col = col


class TicTacToeFrame(wx.Frame):

    def __init__(self):
        super(TicTacToeFrame, self).__init__(parent=None,
                                             title='TicTacToe App',
                                             size=(250, 100))
        self.button_grid = []
        self.board = Board()
        self.human = HumanPlayer(self.board)
        self.computer = ComputerPlayer(self.board)

        self.setup_display()

        self.get_player_name()
        self.select_player_counter()
        self.select_first_player()

    def setup_display(self):
        # Create the panel to contain the widgets
        panel = wx.Panel(self)
        # Create the GridSizer to use with the Panel
        grid_sizer = wx.GridSizer(3, 3, 1, 1)
        panel.SetSizer(grid_sizer)

        for row_position in range(0, 3):
            row = []
            for col_position in range(0, 3):
                button = TicTacToeButton(panel, label=' ', row=row_position, col=col_position)
                button.Bind(wx.EVT_BUTTON, self.button_handler)
                row.append(button)
                grid_sizer.Add(button)
            self.button_grid.append(row)

    def button_handler(self, event):
        button_clicked = event.EventObject
        if button_clicked.GetLabel() != ' ':
            dialog = wx.MessageDialog(None,
                                      'Cell is already in use',
                                      'Cell Message',
                                      wx.OK | wx.ICON_ERROR)
            dialog.ShowModal()
        else:
            move = Move(self.human.counter, button_clicked.row, button_clicked.col)
            self.make_a_move(move)
            finished = False
            if self.board.check_for_winner(self.human):
                self.show_winner_message(self.human)
                finished = True
            else:
                print('Computers move')
                move = self.computer.get_move()
                self.make_a_move(move)
                if self.board.check_for_winner(self.computer):
                    self.show_winner_message(self.computer)
                    finished = True
            if finished == False and self.board.is_full():
                print('Game is a Tie')
                self.show_tie_message()
                finished = True
            if finished:
                print('Goodbye')
                wx.Exit()

    def select_first_player(self):
        print('Starting to play the game')
        if random.randint(0, 1) == 0:
            print('Computer goes first')
            move = self.computer.get_move()
            self.make_a_move(move)

    def make_a_move(self, move):
        self.board.add_move(move)
        row = self.button_grid[move.x]
        row[move.y].SetLabel(move.counter.label)

    def show_winner_message(self, winner):
        dialog = wx.MessageDialog(None,
                                  'The winner is ' + str(winner),
                                  'Winner',
                                  wx.OK)
        dialog.ShowModal()

    def show_tie_message(self):
        dialog = wx.MessageDialog(None,
                                  'The game is a tie',
                                  'No Winner',
                                  wx.OK)
        dialog.ShowModal()

    def select_player_counter(self):
        dialog = wx.MultiChoiceDialog(parent=None,
                                      message='Do you want to be X or O?',
                                      caption='Counter Selection',
                                      choices=['X', 'O'],
                                      style=wx.OK)
        dialog.ShowModal()
        selection = dialog.GetSelections()
        if selection == [0]:
            self.human.counter = X
            self.computer.counter = O
        else:
            self.human.counter = O
            self.computer.counter = X

    def get_player_name(self):
        dialog = wx.TextEntryDialog(None,
                                    'Please enter your name',
                                    'Player Name',
                                    value='unknown',
                                    style=wx.OK)
        dialog.ShowModal()
        self.human.name = dialog.GetValue()


class Counter:
    def __init__(self, string):
        self.label = string

    def __str__(self):
        return self.label


# Set up Counter Globals
X = Counter('X')
O = Counter('O')


class Move:
    """ Represents a move made by a player """

    def __init__(self, counter, x, y):
        self.x = x
        self.y = y
        self.counter = counter

    def __str__(self):
        return 'Move(' + str(self.x) + ', ' + str(self.y) + ')'


class Player(metaclass=ABCMeta):
    """ Abstract class representing a Player and their counter """

    def __init__(self, board):
        self.board = board
        self._counter = None

    @property
    def counter(self):
        """ Represents Players Counter - may be X or Y"""
        return self._counter

    @counter.setter
    def counter(self, value):
        self._counter = value

    def get_move(self): pass


class HumanPlayer(Player):
    """ Represents a Human Player """

    def __init__(self, board, name=''):
        super().__init__(board)
        self.name = name

    def __str__(self):
        return self.name + ' [' + str(self.counter) + ']'


class ComputerPlayer(Player):
    """ Implements algorithms for playing game """

    def __init__(self, board):
        super().__init__(board)

    def _randomly_select_cell(self):
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
            return Move(self.counter, 1, 1)
        elif self.board.is_empty_cell(0, 0):
            # Choose the top left
            return Move(self.counter, 0, 0)
        elif self.board.is_empty_cell(2, 2):
            # Choose the bottom right
            return Move(self.counter, 2, 2)
        elif self.board.is_empty_cell(0, 2):
            # Choose the top right
            return Move(self.counter, 0, 2)
        elif self.board.is_empty_cell(0, 2):
            # Choose the top right
            return Move(self.counter, 2, 0)
        else:
            return self._randomly_select_cell()

    def __str__(self):
        return 'Computer [' + str(self.counter) + ']'


class Board:
    """ The ticTacToe board"""

    def __init__(self):
        # Set up the 3 by 3 grid of cells
        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # List of lists
        self.separator = '\n' + ('-' * 11) + '\n'

    def __str__(self):
        row1 = ' ' + str(self.cells[0][0]) + ' | ' + str(self.cells[0][1]) + ' | ' + str(self.cells[0][2])
        row2 = ' ' + str(self.cells[1][0]) + ' | ' + str(self.cells[1][1]) + ' | ' + str(self.cells[1][2])
        row3 = ' ' + str(self.cells[2][0]) + ' | ' + str(self.cells[2][1]) + ' | ' + str(self.cells[2][2])
        return row1 + self.separator + row2 + self.separator + row3

    def add_move(self, move):
        """ A a move to the board """
        row = self.cells[move.x]
        row[move.y] = move.counter

    def is_empty_cell(self, row, column):
        """ Check to see if a cell is empty or not"""
        return self.cells[row][column] == ' '

    def cell_contains(self, counter, row, column):
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
        return (  # across the top
                (self.cell_contains(c, 0, 0) and self.cell_contains(c, 0, 1) and self.cell_contains(c, 0, 2)) or
                # across the middle
                (self.cell_contains(c, 1, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 1, 2)) or
                # across the bottom
                (self.cell_contains(c, 2, 0) and self.cell_contains(c, 2, 1) and self.cell_contains(c, 2, 2)) or
                # down the left side
                (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 0) and self.cell_contains(c, 2, 0)) or
                # down the middle
                (self.cell_contains(c, 0, 1) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 1)) or
                # down the right side
                (self.cell_contains(c, 0, 2) and self.cell_contains(c, 1, 2) and self.cell_contains(c, 2, 2)) or
                # diagonal
                (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 2)) or
                # other diagonal
                (self.cell_contains(c, 0, 2) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 0)))


class MainApp(wx.App):

    def OnInit(self):
        frame = TicTacToeFrame()
        frame.Show()
        return True


# Run the GUI application
app = MainApp()
app.MainLoop()
