from omok import Omok

class Omok_cui():
    def __init__(self):
        self.__game = Omok()

    def play_by_typing(self):
        while True:
            self.show_board(self.__game.board.data)
            self.inform_which_turn()
            current_row, current_col = self.select_stone_coord()
            exist_value = self.put_stone(self.__game.board.data, current_row, current_col)
            while exist_value == False:
                self.show_board(self.__game.board.data)
                self.inform_which_turn()
                current_row, current_col = self.select_stone_coord()
                exist_value = self.put_stone(self.__game.board.data, current_row, current_col)
            last_stone = self.__game.history[-1]
            # print(self.__game.count_max_sequence(last_stone))
            if self.__game.win_condition(last_stone) != 0:
                break
            self.__game.switch_turn()

        self.show_board(self.__game.board.data)
        if self.__game.win_condition(last_stone) == -1:
            print("White wins!!!")
        else:
            print("Black wins!!!")


    def show_board(self,game_board):
        for row in range(len(game_board)):
            for col in range(len(game_board[row])):
                if row == 0:
                    print(col, end = '|')
                elif col == 0:
                    print(row, end = "|")
                elif game_board[row][col] == 1:
                    print("○", end = '|')
                elif game_board[row][col] == -1:
                    print("●", end = '|')
                else:
                    print(" ", end = '|')
            print()


    def put_stone(self,game_board,row, col):
        current_stone = self.__game.board.stone(row, col, 1)
        if self.__game.is_black_turn and self.__game.is_stone_existed(current_stone) == False:
            self.__game.board.get_stone_in_data(self.__game.board.stone(row, col, 1))
            self.__game.add_history(self.__game.board.stone(row, col, 1))
            return True

        elif self.__game.is_black_turn == False and self.__game.is_stone_existed(current_stone) == False:
            self.__game.board.get_stone_in_data(self.__game.board.stone(row, col, -1))
            self.__game.add_history(self.__game.board.stone(row, col, -1))
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