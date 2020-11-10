class Board():
    def __init__(self):
        self.__white_list = []
        self.__black_list = []
        self.__board_data = []
        self.__max_row = 10
        self.__max_col = 10
        self.board_to_list()
    
    def board_to_list(self):
        board_list_row = []
        for row in range(0,self.__max_row):
            for col in range(0,self.__max_col):
                if row == 0:
                    board_list_row.append(col)
                elif col == 0:
                    board_list_row.append(row)
                else:
                    board_list_row.append("+")

            self.__board_data.append(board_list_row)
            board_list_row = []

    @property
    def board_data(self):
        return self.__board_data

    @board_data.setter
    def board_data(self, stone_data):
        self.__board_data[stone_data[0]][stone_data[1]] = stone_data[2]
    
    @property
    def white_list(self):
        return self.__white_list
    
    @white_list.setter
    def white_list(self, stone):
        self.__white_list.sppend(stone)
    
    @property
    def black_list(self):
        return self.__black_list
    
    @black_list.setter
    def black_list(self, stone):
        self.__black_list.sppend(stone)
    
    def is_stone_existed(self, row, col):
        if [row, col] in self.__white_list:
            return True
        elif [row, col] in self.__black_list:
            return True
        else:
            return False
        
    def black_last_stone(self):
        return self.__black_list[-1]

        
    def white_last_stone(self):
        if len(self.__white_list) != 0:
            return self.__white_list[-1]
        else:
            return [0,0]
