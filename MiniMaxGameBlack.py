import sys
import math
from MorrisVariantUtil import MorrisVariantUtil


class MiniMaxGameBlack:
    '''
    Program plays a move for Black in the midgame/endgame phase of the game with alpha beta pruning.
    '''

    def __init__(self):
        '''
        Take 3 arguments: input file, output file and depth of the game tree.
        '''
        self.inFile = sys.argv[1]
        self.outFile = sys.argv[2]
        self.depth = int(sys.argv[3])
        self.positionsEvaluated = 0
        self.minimax_estimate = 0

    

    def generateMovesMidgameEndgame(self, boardPos):
        '''
        Return a list of all possible moves from board position.
        '''
        whiteCount = 0
        blackCount = 0
        for value in boardPos:
            if value == 'W':
                whiteCount += 1
            elif value == 'B':
                blackCount += 1
        
        if whiteCount == 3:
            return morrisVariantUtil.generateHopping(boardPos)
        else:
            return morrisVariantUtil.generateMove(boardPos)




    def maxMin(self, boardPos, depth):
        '''
        Return the best move for the MAX player.
        '''
        maxChoice : str
        if depth > 0:
            depth -= 1
            v = -math.inf
            # find all possible moves
            possibleMovesList = self.generateMovesMidgameEndgame(boardPos)
            for move in possibleMovesList:
                minPos = self.minMax(move, depth)
                if v < self.staticEstimation(minPos):
                    v = self.staticEstimation(minPos)
                    if self.minimax_estimate != 10000 or self.minimax_estimate != -10000:
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
            possibleMovesList = self.generateMovesMidgameEndgame(boardPos)
            for move in possibleMovesList:
                maxPos = self.maxMin(move, depth)
                if v > self.staticEstimation(maxPos):
                    v = self.staticEstimation(maxPos)
                    minChoice = move
            return minChoice
        elif depth==0:
            self.positionsEvaluated += 1
        return boardPos


    def staticEstimation(self, boardPos):
        '''
        Calculate the static estimation of the position.
        '''
        numWhitePieces = 0
        numBlackPieces = 0
        numBlackMoves = len(self.generateBlackMoves(boardPos))
        for value in boardPos:
            if value=='W':
                numWhitePieces += 1
            elif value=='B':
                numBlackPieces += 1

        if numBlackPieces <= 2:
            return 10000
        elif numWhitePieces <= 2:
            return -10000
        elif numBlackPieces == 0:
            return 10000
        else:
            return (1000*(numWhitePieces - numBlackPieces) - numBlackMoves)


    def generateBlackMoves(self, boardPos):
        '''
        Generate all possible moves for black pieces.
        '''
        copyBoardPos = list(boardPos)
        for location, value in enumerate(copyBoardPos):
            if value == 'W':
                copyBoardPos[location] = 'B'
            elif value == 'B':
                copyBoardPos[location] = 'W'

        blackMoves = self.generateMovesMidgameEndgame(''.join(copyBoardPos))
        finalBlackMoves = []
        for move in blackMoves:
            moveList = list(move)
            for loc, value in enumerate(moveList):
                if value == 'B':
                    moveList[loc] = 'W'
                elif value == 'W':
                    moveList[loc] = 'B'
            finalBlackMoves.append(''.join(moveList))

        return finalBlackMoves




    def checkForWin(self):
        if self.minimax_estimate == 10000:
            print('Congratulations! WINNER WINNER CHICKEN DINNER')



miniMaxGameBlack = MiniMaxGameBlack()
morrisVariantUtil = MorrisVariantUtil()
boardPosition = morrisVariantUtil.readInputFile(miniMaxGameBlack.inFile)
swappedBoardPosition = morrisVariantUtil.swapWhiteAndBlack(boardPosition)
generatedPosition = miniMaxGameBlack.maxMin(swappedBoardPosition, miniMaxGameBlack.depth)
blackPosition = morrisVariantUtil.swapWhiteAndBlack(generatedPosition)
print(f'Input position: {boardPosition} Output position: {blackPosition}')
print(f'Position evaluated by static estimation: {miniMaxGameBlack.positionsEvaluated}')
print(f'MINIMAX Estimate: {miniMaxGameBlack.minimax_estimate}')
morrisVariantUtil.writeOutputFile(miniMaxGameBlack.outFile, blackPosition)
miniMaxGameBlack.checkForWin()