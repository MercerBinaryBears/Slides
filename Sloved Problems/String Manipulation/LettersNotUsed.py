import string
allCharsSet = set(string.ascii_lowercase)
runs = int(input())
for run in range(runs):
    inputSet = set(input().lower())
    result = "".join(sorted(allCharsSet - inputSet))
    
    print("Letters missing in case #{0}: {1}".format(run+1,result))
