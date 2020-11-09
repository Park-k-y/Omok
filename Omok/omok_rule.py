from stone import Stone
from board import Board

class Omok_rule():
    def __init__(self):
        # self.__stone = Stone()
        self.__board = Board()
    
    def win_condition(self):
        if max(self.__board.count_max_sequence_in_black()) == 5:
            return True
            
        elif max(self.__board.count_max_sequence_in_white()) == 5:
            return True
    
        else:
            return False

    def black_three_three(self):
        if self.__board.count_max_sequence_in_black().count(3) >=2:
            return True
        
        else:
            return False