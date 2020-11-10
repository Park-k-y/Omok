from board import Board
from omok import Omok

class Omok_cui():
    def __init__(self):
        self.__game = Omok()

    def play_by_typing(self):
        while True:
            self.show_board(self.__game.board.board_data)
            self.inform_which_turn()
            current_row, current_col = self.select_stone_coord()
            exist_value = self.put_stone(self.__game.board.board_data, current_row, current_col)
            while exist_value == False:
                self.show_board(self.__game.board.board_data)
                self.inform_which_turn()
                current_row, current_col = self.select_stone_coord()
                exist_value = self.put_stone(self.__game.board.board_data, current_row, current_col)
            # print(self.__game.board.black_list)
            # print(self.__game.board.white_list)
            # print(self.__game.count_max_sequence_in_black())
            # print(self.__game.count_max_sequence_in_white())
            if self.__game.win_condition() == True:
                break
            self.__game.switch_turn()

        self.show_board(self.__game.board.board_data)
        if self.__game.is_black_turn == False:
            print("White wins!!!")
        else:
            print("Black wins!!!")


    def show_board(self,game_board):
        for row in range(len(game_board)):
            for col in range(len(game_board[row])):
                print(game_board[row][col], end = '\t')
            print()


    def put_stone(self,game_board,row, col):

        if self.__game.is_black_turn and self.__game.board.is_stone_existed(row, col) == False:
            self.__game.board.board_data = [row,col,"●"]
            self.__game.get_history(row, col)
            return True

        elif self.__game.is_black_turn == False and self.__game.board.is_stone_existed(row, col) == False:
            self.__game.board.board_data = [row,col,"○"]
            self.__game.get_history(row, col)
            return True

        else:
            print("This is a place that already exists.")
            return False

        
        

    def inform_which_turn(self):
        if self.__game.is_black_turn:
            print("It's black turn.")
        else:
            print("It's white turn.")
        
    def select_stone_coord(self):
        row, col = input("[row, col]\n").split(',')

        return int(row), int(col)

    
        # coordinate = x,y
    # omok.action(x,y,color)