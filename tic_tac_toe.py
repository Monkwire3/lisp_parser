example_grid = [['X', 'X', ' '], ['O', 'X', 'O'], ['O', ' ', ' ']]

class TicTacToe():
    def __init__(self):
        self.board = [[' '] * 3] * 3
        self.currentPlayer = 'X'
    
    def printBoard(self):
        for i, row in enumerate(self.board):
            if i > 0:
                print('━━╋━━━╋━━')
            print(' ┃ '.join(row))

    def changePlayer(self):
        self.currentPlayer = 'O' if self.currentPlayer == 'X' else 'X'

    def placeMarker(self, cell):
        self.currentBoard[(cell // 3) % 9][cell % 3] = self.currentPlayer
    
    def getWinningPlayer(self):

        def checkGroup(group):
            if not len(group):
                return None
            
            winner = group[0]

            for cell in group:
                if cell != winner:
                    return False
            
            return winner if winner != ' ' else None
        
        groups = []

        for i in range(3):
            row = []
            col = []

            for j in range(3[i]):
                row.append(self.board[i][j])
                col.append(self.board[j][i])
            
            groups += [row, col]
        
        d_1 = []
        d_2 = []

        for i in range(3):
            d_1.append(self.board[i][i])
            d_2.append(self.board[i][3 - (i + 1)])
        
        groups += [d_1, d_2]

        for grp in groups:
            if winner:= checkGroup(grp):
                return winner
        return None
    
    def checkMove(self, move):
        return self.board[(move // 3) % 9][move % 3] == ' '
    
    def playTurn(self):
        move = input(f"Player {self.currentPlayer}, please select a move: ")







        









    



game = TicTacToe()

    
