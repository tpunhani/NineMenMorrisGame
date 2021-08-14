import sys
import math
from MorrisVariantUtil import MorrisVariantUtil

class ABOpening:
    '''
    Program plays a move in the opening phase of the game with alpha-beta pruning.
    '''


    def __init__(self) -> None:
        '''
        Take 3 arguments: input file, output file and depth of the game tree.
        '''
        self.inFile = sys.argv[1]
        self.outFile = sys.argv[2]
        self.depth = int(sys.argv[3])
        self.positionsEvaluated = 0
        self.alpha_beta_estimate = 0


    def generateMovesOpening(self, boardPos):
        '''
        Return a list of all possible moves from current position.
        '''
        return self.generateAdd(boardPos)


    def generateAdd(self, boardPos):
        '''
        Return a list of all posiible moves from current position.
        '''
        copyBoardPos = []
        listBoardPositions = []
        for location, value in enumerate(boardPos):
            if value=='x':
                copyBoardPos = list(boardPos)
                copyBoardPos[location] = 'W'
                if morrisVariantUtil.closeMill(location, copyBoardPos):
                    listBoardPositions = morrisVariantUtil.generateRemove(''.join(copyBoardPos), listBoardPositions)
                else:
                    listBoardPositions.append(''.join(copyBoardPos))
        return listBoardPositions



    def staticEstimation(self, board):
        '''
        Calculate the static estimation of the position.
        '''
        numWhitePieces = 0
        numBlackPieces = 0
        for value in board:
            if value == 'W':
                numWhitePieces += 1
            elif value == 'B':
                numBlackPieces += 1
        return numWhitePieces - numBlackPieces

            
    def maxMin(self, boardPos, depth, alpha, beta):
        '''
        Return the best move for the MAX player.
        '''
        maxChoice : str
        if depth > 0:
            depth -= 1
            v = -math.inf
            # find all possible moves
            possibleMovesList = self.generateAdd(boardPos)
            for move in possibleMovesList:
                minPos = self.minMax(move, depth, alpha, beta)
                if v < self.staticEstimation(minPos):
                    v = self.staticEstimation(minPos)
                    self.alpha_beta_estimate = v
                    maxChoice = move
                if v >= beta:
                    return maxChoice
                else:
                    alpha = max(alpha, v)
            return maxChoice
        elif depth==0:
            self.positionsEvaluated += 1
        return boardPos


    def minMax(self, boardPos, depth, alpha, beta):
        '''
        Return the best move for the MIN player.
        '''
        minChoice: str
        if depth > 0:
            depth -= 1
            v = math.inf
            # find all possible moves
            possibleMovesList = self.generateAdd(boardPos)
            for move in possibleMovesList:
                maxPos = self.maxMin(move, depth, alpha, beta)
                if v > self.staticEstimation(maxPos):
                    v = self.staticEstimation(maxPos)
                    minChoice = move
                if v <= alpha:
                    return minChoice
                else:
                    beta = min(beta, v)

            return minChoice
        elif depth==0:
            self.positionsEvaluated += 1
        return boardPos



abOpening = ABOpening()
morrisVariantUtil = MorrisVariantUtil()
boardPosition = morrisVariantUtil.readInputFile(abOpening.inFile)
generatedPosition = abOpening.maxMin(boardPosition, abOpening.depth, -math.inf, math.inf)
print(f'Input position: {boardPosition} Output position: {generatedPosition}')
print(f'Position evaluated by static estimation: {abOpening.positionsEvaluated}')
print(f'Alpha Beta Estimate: {abOpening.alpha_beta_estimate}')
morrisVariantUtil.writeOutputFile(abOpening.outFile, generatedPosition)