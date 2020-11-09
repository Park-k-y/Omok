from board import Board
from omok_rule import Omok_rule
from omok_cui import Omok_cui
 

play_game = Omok_rule()
ocui= Omok_cui()
board = Board()
game_board = board.board_to_list()
ocui.new_board()
while play_game.win_condition() == False:
    print(board.is_black_turn)
    row, col = ocui.inform_which_turn()
    ocui.put_stone(game_board, row, col)
    ocui.show_board(game_board)
    board.switch_turn()
    
    # print(game_board)