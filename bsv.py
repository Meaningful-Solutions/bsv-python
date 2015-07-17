from collections import deque

def readBsv(fileName, sep=('][', ')(', '}{')):
    response = {}
    f = open(fileName, 'r')
    unsplitBsv = f.read()
    firstSep = unsplitBsv[0:2]
    splitBsv = deque(unsplitBsv.split(sep[0]))

    if (firstSep == sep[0]):
        rows = splitBsv.count('')
        columns = (len(splitBsv) - splitBsv.count('') - 1) / splitBsv.count('')
        cleanList = filter(lambda a: a != '', splitBsv)
        for c in range(columns):
            col = deque()
            for r in range(0, rows):
                col.append(cleanList[(columns * r) + c])

            #response.append(col)
            colName = 'X' + str(c + 1)
            response[colName] = col


    if (firstSep == sep[1]):
        rows = splitBsv.count(sep[1])
        columns = (len(splitBsv) - splitBsv.count(sep[1]) - 1) / splitBsv.count(sep[1])
        cleanList = filter(lambda a: a != sep[1], splitBsv)
        for c in range(columns):
            col = deque()
            for r in range(0, rows):
                col.append(cleanList[(columns * r) + c])

            #response.append(col)
            colName = 'X' + str(c + 1)
            response[colName] = col

    if (firstSep == sep[2]):
        response = {}
        hdr = sep[2] + sep[1]
        splitBsv.remove(sep[2])
        rows = splitBsv.count(sep[1])
        colName = splitBsv.popleft()
        while colName != hdr:
            response[colName] = deque()
            colName = splitBsv.popleft()

        columns = len(response)
        cleanList = filter(lambda a: a != sep[1], splitBsv)
        for c, colName in enumerate(response.keys()):
            col = deque()
            for r in range(rows + 1):
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
