import Board

def hGen(Board):

    rCount = -1
    endDist = 5


    for i in Board:
        rowDist = rowUtility(i)
        rCount = rCount + 1
        colcount = 0
        currentcol = []
        for j in i:
            currentcol.append(Board[rCount][colcount])
            colcount = colcount + 1
        colDist = rowUtility(currentcol)

        if(rowDist < endDist):
            endDist = rowDist

        if (colDist < endDist):
            endDist = colDist


    return endDist

def rowUtility(row):
    utility = 0
    maxChain = 0

    mcLocation = 0

    checker = [0,1,2,3,4,7,8]

    chainCount = 0

    while(chainCount <= 14):
        currentCL = chainLength(row, chainCount)
        if(currentCL > maxChain):
            maxChain = currentCL
            mcLocation = chainCount
        chainCount += 1



    if(openEnds(row, mcLocation > 0)):
        utility = 10**maxChain


    if row[mcLocation] == 0:
        utility = utility * -1

    return utility

def chainLength(row, index):
    ival = row[index]
    if(ival == None):
        return 0
    cLength = 1
    lcount = 0
    rcount = 0

    rclength = len(row) - 1

    while( ((index-lcount) >= 0) & (row[index-lcount] == ival) ):
        cLength += 1
        lcount += 1

    while (((index + rcount) <= rclength) & (row[index + rcount] == ival)):
        cLength += 1
        rcount += 1

    return cLength


def openEnds(row, index):
    openCount = 0
    ival = row[index]
    lcount = 0
    rcount = 0

    rclength = len(row) - 1

    while (((index - lcount) >= 0) and (row[index - lcount] == ival)):
        lcount += 1

    while (((index + rcount) <= rclength) and (row[index + rcount] == ival)):
        rcount += 1

    if(((index - lcount) >= 0) and (row[index - lcount] == None)):
        openCount += 1

    if (((index + rcount) <= rclength) and (row[index + rcount] == None)):
        openCount += 1


    return openCount



def utilGen2(board):
    utilVal = 0
    rowCount = 0
    colCount = 0
    activeCount = 0

    #add utility for rows
    while(rowCount <= 14):
        local_list = board[rowCount]
        print local_list
        utilVal += rowUtility(local_list)
        rowCount += 1

    #add utility for columns
    rowCount = 0
    while (rowCount <= 14):
        currentcol = []

        while(colCount <= 14):
            currentcol.append(board[rowCount][colCount])

        utilVal += rowUtility(currentcol)
        colCount += 1





    # #add utility for diagonals
    #
    # dlCount = 4
    # dbCount = 14
    # drCount = 4
    # dtCount = 4
    #
    #
    #
    #
    # while (dlCount <= 14):
    #     currentdia = []
    #
    #     dacount = 0
    #
    #
    #     while(dacount <= dlCount):
    #         currentdia.add(board[dlCount - dacount][dacount])
    #         dacount += 1
    #
    #     utilVal += rowUtility(currentdia)
    #
    #
    #     dacount += 1




    return utilVal

def utilGen(board):
    return 5


