class Stone(self):
    def __init__(self):
        self.__Black = []
        self.__White = []
    
    @property
    def Black(self):
        return self.__Black
    
    @property
    def White(self):
        return self.__White
    
    def count_Black(self):
        return len(self.__Black)
    
    def count_White(self):
        return len(self.__White)
    
    def put_Black(self,coord):
        self.__Black.append(coord)
    
    def put_White(self,coord):
        self.__White.append(coord)

    def    