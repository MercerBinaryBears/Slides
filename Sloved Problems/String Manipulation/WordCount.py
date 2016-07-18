import sys
inText = sys.stdin.read()
numLines = len(inText.splitlines())
numWords = len(str(inText).split())
numBytes = len(str(inText))

print("Lines = {0}\nWords = {1}\nBytes = {2}".format(numLines,numWords,numBytes))
