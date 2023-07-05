import os

class TicTacToe():
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.currentPlayer = 'X'
    
    def printBoard(self):
        for i, row in enumerate(self.board):
            if i > 0:
                print('━━╋━━━╋━━')
            print(' ┃ '.join(row))

    def changePlayer(self):
        self.currentPlayer = 'O' if self.currentPlayer == 'X' else 'X'

    def placeMarker(self, cell):
        self.board[((cell) // 3) % 9][(cell) % 3] = self.currentPlayer
    
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

            for j in range(3):
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
        if move is None:
            return move

        return self.board[(move // 3) % 9][move % 3] == ' '
    
    def checkStalemate(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        
        return True
    


    def printBoardAndMoves(self):
        

        validMoves = []

        for i, row in enumerate(self.board):
            validMovesRow = []
            for j, cell in enumerate(row):
                validMovesRow.append('_' if cell != ' ' else f"{(i * 3) + j + 1}")
            validMoves.append(validMovesRow)

        print(f"  BOARD {' ' * 30}  VALID MOVES")

        for i in range(3):
            if i > 0:
                print(f"{'━━╋━━━╋━━'} {' ' * 30} {'━━╋━━━╋━━'}")
            print(' ┃ '.join(self.board[i]), ' ' * 30, ' ┃ '.join(validMoves[i]))
        







   
    def playGame(self):
        stalemate = False
        winner = False

        while not stalemate and not winner:
            move = None
            while not self.checkMove(move):
                try:
                    os.system('clear')
                    self.printBoardAndMoves()
                    print()
                    move = (int(input(f"Player {self.currentPlayer}, please select a move: "))) - 1
                except ValueError as e:
                    print(e)
            
            self.placeMarker(move)
            os.system('clear')
            self.printBoardAndMoves()

            self.changePlayer()


            stalemate = self.checkStalemate()
            winner = self.getWinningPlayer()

            if winner:
                print(f"{winner} has won!")
                return
            elif stalemate:
                print('Stalemate')
                return
            else:
                continue


def main():
    game = TicTacToe()
    game.playGame()

if __name__ == "__main__":
    main()












    
        










        









    



game = TicTacToe()

    
