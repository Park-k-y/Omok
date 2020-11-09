import numpy as np
class Board():
    def __init__(self):
        self.__white_list = []
        self.__black_list = []
        self.__is_black_turn = True
    
    def board_to_list(self):
        board_list = []
        board_list_row = []
        for row in range(0,10):
            for col in range(0,10):
                if row == 0:
                    board_list_row.append(col)
                elif col == 0:
                    board_list_row.append(row)
                else:
                    board_list_row.append("+")

            board_list.append(board_list_row)
            board_list_row = []
    
        return np.array(board_list)

    @property
    def is_black_turn(self):
        return self.__is_black_turn
    
    @property
    def white_list(self):
        return self.__white_list
    
    @property
    def white_list(self, stone):
        self.__white_list.sppend(stone)
    
    @property
    def black_list(self):
        return self.__black_list
    
    @property
    def black_list(self, stone):
        self.__black_list.sppend(stone)

    def switch_turn(self):
        if self.__is_black_turn:
            self.__is_black_turn = False
        else:
            self.__is_black_turn = True

    def is_stone_existed(self, row, col):
        if [row, col] in self.__white_list:
            return True
        elif [row, col] in self.__black_list:
            return True
        else:
            return False

    def put_stone(self, row, col):
        if self.__is_black_turn == True:
            if self.is_stone_existed(row, col) != True:
                self.__black_list.append([row, col])
                
        else:
            if self.is_stone_existed(row,col) != True:
                self.__white_list.append([row, col])
    
    def last_stone(self):
        if self.__is_black_turn:
            if len(self.__black_list) != 0:
                return self.__black_list[-1]
            else:
                return [0,0]
        else:
            if len(self.__white_list) != 0:
                return self.__white_list[-1]
            else:
                return [0,0]

    def search_stone_in_direction(self, stone, direction, constant):
        surrounding_stone = []
        for i in range(0,2):
            surrounding_stone.append(direction[i]*constant + stone[i])

        return surrounding_stone


    def count_max_sequence_in_white(self):
        current_stone = self.last_stone()
        directions = [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
        count_direction = []
        count = 0
        
        for dir in directions:
            for i in range(0,5):
                sur_stone = self.search_stone_in_direction(current_stone, dir, i+1)
                if sur_stone in self.__white_list:
                    count += 1
                else:
                    count_direction.append(count)
                    count = 0

        right_diagonal = count_direction[1] + count_direction[5]
        left_diagonal = count_direction[3] + count_direction[7]
        row = count_direction[0] + count_direction[4]
        col =count_direction[2] + count_direction[6]

        return [row, right_diagonal, col, left_diagonal]

    def count_max_sequence_in_black(self):
        current_stone = self.last_stone()
        directions = [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
        count_direction = []
        count = 0
        
        for dir in directions:
            for i in range(0,5):
                sur_stone = self.search_stone_in_direction(current_stone, dir, i+1)
                if sur_stone in self.__black_list:
                    count += 1
                else:
                    count_direction.append(count)
                    count = 0

        right_diagonal = count_direction[1] + count_direction[5] +1
        left_diagonal = count_direction[3] + count_direction[7] +1
        row = count_direction[0] + count_direction[4] +1
        col =count_direction[2] + count_direction[6] +1
        
        return [row, right_diagonal, col, left_diagonal]