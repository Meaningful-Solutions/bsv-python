from collections import deque


def readBsv(fileName=None, text=None, sep=('][', ')(', '}{')):
    response = {}
    if(fileName is not None):
        f = open(fileName, 'r')
        unsplitBsv = f.read()
    elif(text is not None):
        unsplitBsv = text

    firstSep = unsplitBsv[0:2]
    splitBsv = deque(unsplitBsv.split(sep[0]))

    if (firstSep == sep[0]):
        #print 'first'
        cleanList = filter(lambda a: a != '', splitBsv)
        rows = len(splitBsv) - len(cleanList) - 1
        #print rows
        columns = [i for i, a in enumerate(splitBsv) if a != '']
        nbrOfColumns = len(columns) / rows
        #print nbrOfColumns
        cleanList = filter(lambda a: a != '', splitBsv)
        #print cleanList
        for c in range(nbrOfColumns):
            col = deque()
            for r in range(0, rows):
                col.append(cleanList[(nbrOfColumns * r) + c])

            colName = 'X' + str(c + 1)
            response[colName] = col

    if (firstSep == sep[1]):
        rows = splitBsv.count(sep[1]) - 1
        columns = [i for i, a in enumerate(splitBsv) if a != sep[1]]
        nbrOfColumns = len(columns) / rows
        cleanList = filter(lambda a: a != sep[1], splitBsv)
        for c in range(nbrOfColumns):
            col = deque()
            for r in range(0, rows):
                col.append(cleanList[(nbrOfColumns * r) + c])

            colName = 'X' + str(c + 1)
            response[colName] = col

    if (firstSep == sep[2]):
        response = {}
        hdr = sep[2] + sep[1]
        hdrTxt = splitBsv[0]
        splitHdr = hdrTxt.split(sep[2])
        splitHdr = splitHdr[1:len(splitHdr) - 1]
        splitBsv = [splitBsv[i] for i in range(1, len(splitBsv))]
        rows = 0
        for val in splitBsv:
            if val == sep[1]:
                rows = rows + 1

        for colName in splitHdr:
            response[colName] = deque()

        columns = len(response)
        cleanList = filter(lambda a: a != sep[1], splitBsv)
        for c, colName in enumerate(splitHdr):
            col = deque()
            for r in range(rows):
                col.append(cleanList[(columns * r) + c])

            response[colName] = col

    return response


def writeBsv(x, filepath=None, sep=('][', ')(', '}{')):
    response = ""
    hdrList = x.keys()
    response = sep[2] + sep[0] + sep[0].join(hdrList) + sep[0] + sep[2]
    nbrOfRows = len(x[hdrList[1]])
    for r in range(0, nbrOfRows):
        row = deque()
        for h, hdr in enumerate(hdrList):
            row.append(x[hdr][r])

        response = response + sep[1] + sep[0] + sep[0].join(row) + sep[0]
    response = response + sep[1] + '\n'
    if filepath is None:
        return response
    else:
        f = open(filepath, 'w')
        f.write(response)
        f.close()


#print readBsv(text='][b][s][][v][o][][m][g][')
#print readBsv(text=")(][b][s][v][)(][o][m][g][)(")
#print readBsv(text="}{Col1}{Col2}{)(][b][s][)(][v][o][)(][m][g][)(")