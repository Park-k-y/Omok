from board import Board

class Omok():
    def __init__(self):
        self.__board = Board()
        self.__is_black_turn = True
    
    @property
    def board(self):
        return self.__board

    @property
    def is_black_turn(self):
        return self.__is_black_turn

    def get_history(self, row, col):
        if self.__is_black_turn == True:
            if self.__board.is_stone_existed(row, col) != True:
                self.__board.black_list.append([row, col])
                
        else:
            if self.__board.is_stone_existed(row,col) != True:
                self.__board.white_list.append([row, col])


    def win_condition(self):
        if max(self.count_max_sequence_in_black()) == 5:
            return True

        elif max(self.count_max_sequence_in_white()) == 5:
            return True
    
        else:
            return False

    def black_three_three(self):
        if self.count_max_sequence_in_black().count(3) >=2:
            return True
        
        else:
            return False
        
    
    def switch_turn(self):
        if self.__is_black_turn:
            self.__is_black_turn = False
        else:
            self.__is_black_turn = True
    

    def search_stone_in_direction(self, stone, direction, constant):
        surrounding_stone = []
        for i in range(0,2):
            surrounding_stone.append(direction[i]*constant + stone[i])

        return surrounding_stone

    def count_max_sequence_in_white(self):
        current_stone = self.__board.white_last_stone()
        directions = [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
        count_direction = []
        count = 1
        
        for dir in directions:
            for i in range(0,5):
                sur_stone = self.search_stone_in_direction(current_stone, dir, i+1)
                if sur_stone in self.__board.white_list:
                    count += 1
                else:
                    count_direction.append(count)
                    count = 1
                    break

        right_diagonal = count_direction[1] + count_direction[5] -1
        left_diagonal = count_direction[3] + count_direction[7] -1
        col = count_direction[0] + count_direction[4] -1
        row =count_direction[2] + count_direction[6] -1
        
        return [col, right_diagonal, row, left_diagonal]


    def count_max_sequence_in_black(self):
        current_stone = self.__board.black_last_stone()
        directions = [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
        count_direction = []
        count = 1
        
        for dir in directions:
            for i in range(0,5):
                sur_stone = self.search_stone_in_direction(current_stone, dir, i+1)
                if sur_stone in self.__board.black_list:
                    count += 1
                else:
                    count_direction.append(count)
                    count = 1
                    break

        right_diagonal = count_direction[1] + count_direction[5] -1
        left_diagonal = count_direction[3] + count_direction[7] -1
        col = count_direction[0] + count_direction[4] -1
        row = count_direction[2] + count_direction[6] -1
        
        return [col, right_diagonal, row, left_diagonal]
