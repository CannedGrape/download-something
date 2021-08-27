
import os

from urllib.request import urlretrieve

inputPath='./raw_data/'
outputPath='./image/'

os.makedirs(outputPath, exist_ok=True)

imgUrl = ""

def downd(ifile, fileLines):
    for line in fileLines:
        imgUrl = line.strip('\n')
        print (imgUrl, end=" ")
        fileNameList = imgUrl.split('/')
        fileName = fileNameList[len(fileNameList) - 1]
        fileName = ifile + "." + fileName
        print("File:" , fileName, end=" ")
        try:
            urlretrieve(imgUrl, outputPath + fileName)    
        except:
            print ("Error!")
        else:
            print ("OK!")


for filePath, folders, files in os.walk(inputPath):
    for ifile in files:
        filePath=os.path.join(filePath,ifile)
        print (filePath)

        # read file
        with open(filePath, 'r') as f:
            fileLines = f.readlines()

        n = 1
        for line in fileLines:
            imgUrl = line.strip('\n')
            print ("["+str(n)+"]", imgUrl, end=" ")
            fileNameList = imgUrl.split('/')
            fileName = fileNameList[len(fileNameList) - 1]
            fileName = ifile + "." + fileName
            print("File:" , fileName, end=" ")
            try:
                urlretrieve(imgUrl, outputPath + fileName)    
            except:
                print ("Error!")
            else:
                print ("OK!")
                n = n + 1

