from MorrisVariantUtil import MorrisVariantUtil
import sys
import math

class MiniMaxOpeningImproved:
    '''
    Program plays a move in the opening phase of the game with improved static estimation.
    '''


    def __init__(self) -> None:
        '''
        Take 3 arguments: input file, output file and depth of the game tree.
        '''
        self.inFile = sys.argv[1]
        self.outFile = sys.argv[2]
        self.depth = int(sys.argv[3])
        self.positionsEvaluated = 0
        self.minimax_estimate = 0


    def generateMovesOpening(self, boardPos):
        '''
        Return a list of all possible moves from current position.
        '''
        return self.generateAdd(boardPos)


    def generateAdd(self, boardPos):
        '''
        Return a list of all possible moves from current position.
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



    def maxMin(self, boardPos, depth):
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
                minPos = self.minMax(move, depth)
                if v < self.staticEstimation(minPos):
                    v = self.staticEstimation(minPos)
                    self.minimax_estimate = v
                    maxChoice = move
            return maxChoice
        elif depth==0:
            self.positionsEvaluated += 1
        return boardPos


    def minMax(self, boardPos, depth):
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
                maxPos = self.maxMin(move, depth)
                if v > self.staticEstimation(maxPos):
                    v = self.staticEstimation(maxPos)
                    minChoice = move
            return minChoice
        elif depth==0:
            self.positionsEvaluated += 1
        return boardPos


    def staticEstimation(self, board):
        '''
        Calculate the improved static estimation of the position.
        '''
        numWhitePieces = 0
        numBlackPieces = 0
        for value in board:
            if value == 'W':
                numWhitePieces += 1
            elif value == 'B':
                numBlackPieces += 1
        numWhiteMills = morrisVariantUtil.countMills(board, 'W')
        estimate = (numWhitePieces - numBlackPieces) + numWhiteMills
        return estimate

    

            
    

    


miniMaxOpeningImproved = MiniMaxOpeningImproved()
morrisVariantUtil = MorrisVariantUtil()
boardPosition = morrisVariantUtil.readInputFile(miniMaxOpeningImproved.inFile)
generatedPosition = miniMaxOpeningImproved.maxMin(boardPosition, miniMaxOpeningImproved.depth)
print(f'Input position: {boardPosition} Output position: {generatedPosition}')
print(f'Position evaluated by static estimation: {miniMaxOpeningImproved.positionsEvaluated}')
print(f'MINIMAX Estimate: {miniMaxOpeningImproved.minimax_estimate}')
morrisVariantUtil.writeOutputFile(miniMaxOpeningImproved.outFile, generatedPosition)