from board import Board
from omok_rule import Omok_rule

class Omok_cui():
    def __init__(self):
        self.__board = Board()

    def new_board(self):
        for row in range(len(self.__board.board_to_list())):
            for col in range(len(self.__board.board_to_list()[row])):
                print(self.__board.board_to_list()[row][col], end = '\t')
            print()
        
    def show_board(self,game_board):
        for row in range(len(game_board)):
            for col in range(len(game_board[row])):
                print(game_board[row][col], end = '\t')
            print()
                

    def put_stone(self,game_board,row, col):
        if self.__board.is_black_turn:
            game_board[row][col] =  "●"
        elif self.__board.is_black_turn == False:
            game_board[row][col] =  "○"
        else:
            print("You can't put it there.")
        
        self.__board.put_stone(row, col)
        
        return game_board

    def inform_which_turn(self):
        if self.__board.is_black_turn:
            row, col = input("It's black turn. (row, col)\n").split(',') 
        else:
            row, col = input("It's white turn. (row, col)\n").split(',')
        
        return int(row), int(col)

