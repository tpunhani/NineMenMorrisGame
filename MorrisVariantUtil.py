import math

class MorrisVariantUtil:

    '''
    Utility program to provide various functions for Morris game.
    '''

 
    def readInputFile(self, inFile):
        '''
        Read input file and return input board position.
        '''
        boardPos: str
        with open(inFile, 'r') as i:
            boardPos = i.readline()
        return boardPos

    def writeOutputFile(self, outFile, result):
        '''
        Write output position to the file.
        '''
        outputBoardFile =  open(outFile, 'w+')
        outputBoardFile.write(result)


    def generateRemove(self, boardPos, listBoardPositions):
        '''
        Remove one piece of the opponent from the board.
        '''
        copyListBoardPositions = listBoardPositions.copy()
        for location, value in enumerate(boardPos):
            if value=='B':
                if not self.closeMill(location, boardPos):
                    copyBoardPos = list(boardPos)
                    copyBoardPos[location] = 'x'
                    copyListBoardPositions.append(''.join(copyBoardPos))
                else:
                    copyListBoardPositions.append(boardPos)
        return copyListBoardPositions


    def generateHopping(self, boardPos):
        '''
        Move one piece to any place when only 3 pieces are left.
        '''
        hopList = []
        for alpha, alphaValue in enumerate(boardPos):
            if alphaValue == 'W':
                for beta, betaValue in enumerate(boardPos):
                    if betaValue == 'x':
                        copyBoard = list(boardPos)
                        copyBoard[alpha] = 'x'
                        copyBoard[beta] = 'W'
                        if self.closeMill(beta, copyBoard):
                            hopList = self.generateRemove(''.join(copyBoard), hopList)
                        else:
                            hopList.append(''.join(copyBoard))
        return hopList



    def generateMove(self, boardPos):
        '''
        Move one piece to it's neighbor when more than 3 pieces are left.
        '''
        moveList = []

        for location, value in enumerate(boardPos):
            if value == 'W':
                n = self.neighbors(location)
                for neighbor in n:
                    if boardPos[neighbor] == 'x':
                        copyBoardPos = list(boardPos)
                        copyBoardPos[location] = 'x'
                        copyBoardPos[neighbor] = 'W'
                        if self.closeMill(neighbor, copyBoardPos):
                            self.generateRemove(''.join(copyBoardPos), moveList)
                        else:
                            moveList.append(''.join(copyBoardPos))
        return moveList



    def closeMill(self, location, copyBoard):
        '''
        Check weather mill is closed or not.
        '''
        c = copyBoard[location]
        if c=='W' or c=='B':
            if location==0:
                if (copyBoard[6] == c and copyBoard[18] == c) or (copyBoard[2] == c and copyBoard[4]==c):
                    return True
                else:
                    return False

            if location==1:
                if (copyBoard[11] == c and copyBoard[20] == c):
                    return True
                else:
                    return False

            if location==2:
                if (copyBoard[0] == c and copyBoard[4] == c) or (copyBoard[7] == c and copyBoard[15]==c):
                    return True
                else:
                    return False

            if location==3:
                if (copyBoard[10] == c and copyBoard[17] == c):
                    return True
                else:
                    return False


            if location==4:
                if (copyBoard[0] == c and copyBoard[2] == c) or (copyBoard[8] == c and copyBoard[12]==c):
                    return True
                else:
                    return False

            if location==5:
                if (copyBoard[9] == c and copyBoard[14] == c):
                    return True
                else:
                    return False

            if location==6:
                if (copyBoard[7] == c and copyBoard[8] == c) or (copyBoard[0] == c and copyBoard[18]==c):
                    return True
                else:
                    return False

            if location==7:
                if (copyBoard[6] == c and copyBoard[8] == c) or (copyBoard[2] == c and copyBoard[15]==c):
                    return True
                else:
                    return False

            if location==8:
                if (copyBoard[4] == c and copyBoard[12] == c) or (copyBoard[6] == c and copyBoard[7]==c):
                    return True
                else:
                    return False

            if location==9:
                if (copyBoard[5] == c and copyBoard[14] == c) or (copyBoard[10] == c and copyBoard[11]==c):
                    return True
                else:
                    return False

            if location==10:
                if (copyBoard[9] == c and copyBoard[11] == c) or (copyBoard[3] == c and copyBoard[17]==c):
                    return True
                else:
                    return False

            if location==11:
                if (copyBoard[1] == c and copyBoard[20] == c) or (copyBoard[9] == c and copyBoard[10]==c):
                    return True
                else:
                    return False

            if location==12:
                if (copyBoard[4] == c and copyBoard[8] == c) or (copyBoard[13] == c and copyBoard[14]==c):
                    return True
                else:
                    return False

            if location==13:
                if (copyBoard[12] == c and copyBoard[14] == c) or (copyBoard[16] == c and copyBoard[19]==c):
                    return True
                else:
                    return False

            if location==14:
                if (copyBoard[5] == c and copyBoard[9] == c) or (copyBoard[12] == c and copyBoard[13]==c):
                    return True
                else:
                    return False

            if location==15:
                if (copyBoard[2] == c and copyBoard[7] == c) or (copyBoard[16] == c and copyBoard[17]==c):
                    return True
                else:
                    return False

            if location==16:
                if (copyBoard[13] == c and copyBoard[19] == c) or (copyBoard[15] == c and copyBoard[17]==c):
                    return True
                else:
                    return False

            if location==17:
                if (copyBoard[15] == c and copyBoard[16] == c) or (copyBoard[3] == c and copyBoard[10]==c):
                    return True
                else:
                    return False

            if location==18:
                if (copyBoard[0] == c and copyBoard[6] == c) or (copyBoard[19] == c and copyBoard[20]==c):
                    return True
                else:
                    return False

            if location==19:
                if (copyBoard[18] == c and copyBoard[20] == c) or (copyBoard[13] == c and copyBoard[16]==c):
                    return True
                else:
                    return False

            if location==20:
                if (copyBoard[1] == c and copyBoard[11] == c) or (copyBoard[18] == c and copyBoard[19]==c):
                    return True
                else:
                    return False

        return False



    def neighbors(self, location):
        '''
        Find all the neighbors of the current location.
        '''
        if location == 0:
            return [1, 2, 6]
        elif location == 1:
            return [0, 11]
        elif location == 2:
            return [3, 4, 7]
        elif location == 3:
            return [2, 10]
        elif location == 4:
            return [2, 5, 8]
        elif location == 5:
            return [4, 9]
        elif location == 6:
            return [0, 7, 18]
        elif location == 7:
            return [2, 6, 8, 15]
        elif location == 8:
            return [4, 7, 12]
        elif location == 9:
            return [5, 10, 14]
        elif location == 10:
            return [3, 9, 11, 17]
        elif location == 11:
            return [1, 10, 20]
        elif location == 12:
            return [8, 13]
        elif location == 13:
            return [12, 14, 16]
        elif location == 14:
            return [9, 13]
        elif location == 15:
            return [7, 16]
        elif location == 16:
            return [13, 15, 17, 19]
        elif location == 17:
            return [10, 16]
        elif location == 18:
            return [6, 19]
        elif location == 19:
            return [16, 18, 20]
        elif location == 20:
            return [11, 19]
        else:
            return []


    def swapWhiteAndBlack(self, boardPos):
        '''
        Swap white and black pieces.
        '''
        copyBoard = list(boardPos)
        for location, value in enumerate(copyBoard):
            if value == 'W':
                copyBoard[location] = 'B'
            elif value == 'B':
                copyBoard[location] = 'W'
        return ''.join(copyBoard)


    
    def countMills(self, boardPos, color):
        '''
        Count number of mills can be formed with the next move.
        '''
        copyBoard = list(boardPos)
        numMills = 0
        for location, value in enumerate(copyBoard):
            if value == 'x':
                copyBoard[location] = color
                if self.closeMill(location, copyBoard):
                    numMills += 1
        return numMills
            
