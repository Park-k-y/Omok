from stone import Stone

class Board():
    def __init__(self):
        self.__stone = Stone
        self.__max_row = 10
        self.__max_col = 10
        self.__data = self.new_board()

    @property
    def stone(self):
        return self.__stone
    
    def new_board(self):
        board = []
        for row in range(0,self.__max_row):
            board_list_row = []
            for col in range(0,self.__max_col):
                if row == 0 or col == 0:
                    board_list_row.append(None)
                else:
                    board_list_row.append("0")
            board.append(board_list_row)
        return board

    @property
    def data(self):
        return self.__data

    def get_stone_in_data(self, stone):
        self.__data[stone.row][stone.col] = stone.color