class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        out = list()
        
        board = [[None for x in range(8)] for y in range(8)]
        
        for queen in queens:
            board[queen[0]][queen[1]] = True
        
        #up vertical check
        i, j = king
        while i>= 0:
            if board[i][j] == True:
                print(i,j,"up")
                out.append([i,j])
                break
            i-=1
        #down vertical check
        i, j = king
        while i < 8:
            if board[i][j] == True:
                print(i,j,"down")
                out.append([i,j])
                break
            i+=1
        #left check
        i, j = king
        while j>= 0:
            if board[i][j] == True:
                print(i,j,"left")
                out.append([i,j])
                break
            j-=1
        #right check
        i, j = king
        while j < 8:
            if board[i][j] == True:
                print(i,j,"right")
                out.append([i,j])
                break
            j+=1
        
        #top left check
        i, j = king
        while i >= 0 and j >=0:
            if board[i][j] == True:
                print(i,j,"tl")
                out.append([i,j])
                break
            j-=1
            i-=1
            
        #top right check
        i, j = king
        while i >= 0 and j < 8:
            if board[i][j] == True:
                print(i,j,"tr")
                out.append([i,j])
                break
            j+=1
            i-=1
        
        #bottom right check
        i, j = king
        while i < 8 and j < 8:
            if board[i][j] == True:
                print(i,j,"br")
                out.append([i,j])
                break
            j+=1
            i+=1
        #bottom left check
        i, j = king
        while i < 8 and j >=0:
            if board[i][j] == True:
                print(i,j,"bl")
                out.append([i,j])
                break
            j-=1
            i+=1
        
        return out
        