def hygiene(board):
    
    good = list(board)
    for i in range(9):
        for j in range(9):
            if good[i][j] == "" or good[i][j] is None:
                good[i][j] = 0
    
    return good


def helper(_board):
    if isSolved(_board) == True:
        return _board 

    board = list(_board)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                dit = dict()
                for k in range(0, 10):
                    dit[k] = 0 
                
                for num in board[i]:
                    if num != 0:
                        dit[num] += 1
                
                for k in range(9):
                    if board[k][j] != 0:
                        dit[board[k][j]] += 1
                
                # found = False
                for num in range(1, 10):
                    if dit[num] == 0:
                        # found = True
                        board[i][j] = num 
                        res = helper(board)

                        if res != None and isSolved(res) == True:
                            return res

                board[i][j] = 0
                return None
    
    return None

def isSolved(board):
    for i in range(9):
        rowdict = dict()
        for num in range(0, 10):
            rowdict[num] = 0

        for j in range(9):
            if board[i][j] == 0:
                return False 

            if rowdict[board[i][j]] == 1:
                return False

            rowdict[board[i][j]] += 1
        
        for k in range(1, 10):
            if rowdict[k] == 0:
                return False
    

    # make sure no column repititions.
    for i in range(9):
        coldict = dict()
        for num in range(0, 10):
            coldict[num] = 0
        for j in range(9):
            if coldict[board[j][i]] == 1:
                return False
            if board[j][i] == 0:
                return False
            coldict[board[j][i]] += 1
        
        for k in range(1, 10):
            if coldict[k] == 0:
                return False


    # make sure every 3 x 3 grid has all numbers from 1 to 9.
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            freq = dict()
            for num in range(0, 10):
                freq[num] = 0
            for ii in range(i, i + 3):
                for jj in range(j, j + 3):
                    if freq[board[ii][jj]] != 0:
                        return False 
                    freq[board[ii][jj]] += 1
            for num in range(1, 10):
                if freq[num] != 1:
                    return False
    return True

def valid(board):
    
    for i in range(9):
        rowDict = dict()
        for k in range(0, 10):
            rowDict[k] = 0
        for j in range(9):
            rowDict[board[i][j]] = rowDict[board[i][j]] + 1
        
        for k in range(1, 10):
            if rowDict[k] > 1:
                return False           


    for i in (9):
        colDict = {}
        for k in range(0, 10):
            rowDict[k] = 0
        for j in range(9):
            rowDict[board[j][i]] = rowDict[board[j][i]] + 1
        
        for k in range(1, 10):
            if colDict[k] > 1:
                return False         

    return True


def solve(board):
    print("inside of solve function")
    n = len(board)

    assert n == 9
    assert len(board[0]) == n

    # make sure there are no blanks, if there are blanks it would set them to zero.
    # safe = hygiene(board)
    
    # isValid = valid(board)

    # if isValid is False or None:
    #     raise Exception(" there is something wrong with thiw board")

    final = helper(board)
    # print(final)

    if final != None:
        for row in final:
            print(row)



if __name__ == '__main__':
    board = [ 
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    res = solve(board)

    print(res)