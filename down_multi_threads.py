
import os
import threading 
import socket

from urllib.request import urlretrieve

socket.setdefaulttimeout(128)

inputPath='./raw_data/'

imgUrl = ""

def downMultiThreads(outPrefix, fileLines, threadNum, threadTotal):
    fileLength = len(fileLines)
    e = int(fileLength / threadTotal) + 1
    start = (threadNum - 1) * e
    stop  = threadNum * e - 1
    if stop > fileLength:
        stop = fileLength

    for i in range(start, stop, 1):
        line = fileLines[i]
        imgUrl = line.strip('\n')
        outStr = imgUrl + "\n -> "
        fileNameList = imgUrl.split('/')
        fileName = fileNameList[len(fileNameList) - 1]
        fileName = outPrefix + fileName
        outStr = outStr + "File: " + fileName + "\n"

        try:
            urlretrieve(imgUrl, fileName)  
            #print(fileName)  
        except:
            outStr = outStr + "Fail!"
        else:
            outStr = outStr + "OK!"
        print (outStr)

for filePath, folders, files in os.walk(inputPath):
    for iFile in files:
        tempFilePath = os.path.join(filePath,iFile)
        print ("***", tempFilePath)

        os.makedirs('./image/' + filePath, exist_ok = True)

        # for Windows:
        outPrefix = '.\\image\\' + filePath.replace('/', '\\') + '\\'
        # for Linux:
        # outPrefix = './image/' + filePath + '/'

        # read file
        with open(tempFilePath, 'r') as f:
            fileLines = f.readlines()

        # single thread
        # downSingleThread(iFile, fileLines)

        # multi threads N
        N = 32
        t = []
        for i in range(0, N, 1):
            print ("Creating thread No.", i)
            t.append(threading.Thread(target=downMultiThreads, name='dMT', args=(outPrefix, fileLines, i, N, )))

        for i in range(0, N, 1):
            print ("Starting thread No.", i)
            t[i].start()

        for i in range(0, N, 1):
            t[i].join()

