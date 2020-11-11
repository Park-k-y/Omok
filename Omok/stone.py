class Stone():
    def __init__(self,row, col,color):
        self.__color = color 
        self.__col = col
        self.__row = row
            
    @property
    def col(self):
        return self.__col

    @property
    def row(self):
        return self.__row
    
    @property
    def color(self):
        return self.__color
    
    @col.setter
    def col(self, new_col):
        self.__col = new_col
    
    @row.setter
    def row(self, new_row):
        self.__row = new_row
    
    @color.setter
    def color(self, new_color):
        self.__color = new_color
    
    def get_coord(self):
        coord = [self.__row, self.__col]
        return coord

    def __eq__(self, other): 
        if not isinstance(other, Stone):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.__row == other.row and self.__col == other.col and self.__color == other.color
    