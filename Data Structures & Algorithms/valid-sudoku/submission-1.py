import sys
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num = ["1","2","3","4","5","6","7","8","9"]
        for i in range(9):
            sud = []
            for j in range(9):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        for k in range(9):
            sud = []
            for l in range(9):
                
                if board[l][k] in sud:
                    return False
                    sys.exit()
                if board[l][k] not in sud and board[l][k]!= ".":
                    sud.append(board[l][k])        
        
        
        
        
        sud=[]
        for i in range(3):
            for j in range(3):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        sud=[]
        for i in range(3):
            for j in range(3,6):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        sud=[]
        for i in range(3):
            for j in range(6,9):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        
        sud=[]
        for i in range(3,6):
           
            for j in range(3):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        sud=[]
        for i in range(3,6):
           
            for j in range(3,6):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        sud=[]
        for i in range(3,6):
            
            for j in range(6,9):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        

        sud=[]
        for i in range(6,9):
            
            for j in range(3):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        sud=[]
        for i in range(6,9):
            
            for j in range(3,6):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        sud=[]
        for i in range(6,9):
            
            for j in range(6,9):
                
                if board[i][j] in sud:
                    return False
                    sys.exit()
                if board[i][j] not in sud and board[i][j]!= ".":
                    sud.append(board[i][j])
        
        return True
        




                