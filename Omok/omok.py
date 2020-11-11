from board import Board

class Omok():
    def __init__(self):
        self.__board = Board()
        self.__is_black_turn = True
        self.__history = []
    
    @property
    def board(self):
        return self.__board
    
    @property
    def history(self):
        return self.__history

    @property
    def is_black_turn(self):
        return self.__is_black_turn
         
    def is_stone_existed(self, stone):
        for i in range(len(self.__history)):
            if stone.get_coord() == self.__history[i].get_coord():
                return True
        else:
            return False

    def add_history(self, stone):
        if self.is_black_turn == True:
            if self.is_stone_existed(stone) != True:
                self.__history.append(stone)

        else:
            if self.is_stone_existed(stone) != True:
                self.__history.append(stone)

    def win_condition(self, last_stone):
        if max(self.count_max_sequence(last_stone)) == 5:
            if self.__is_black_turn:
                return 1
            else:
                return -1

        else:
            return 0

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
    

    def __search_stone_in_direction(self, stone, direction, constant):
        surrounding_stone = []
        for i in range(0,2):
            surrounding_stone.append(direction[i]*constant + stone[i])

        return surrounding_stone

    def count_max_sequence(self,last_stone):
        current_stone = last_stone.get_coord()
        directions = [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
        count_direction = []
        count = 1
        
        for dir in directions:
            for i in range(0,5):
                axis_stone = self.__search_stone_in_direction(current_stone, dir, i+1)
                if self.__is_black_turn:
                    find_stone = self.__board.stone(axis_stone[0], axis_stone[1], 1)
                else:
                    find_stone = self.__board.stone(axis_stone[0], axis_stone[1], -1)

                if find_stone in self.__history:
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
