import math
runs = int(input())
for run in range(runs):
    h,m,s = [int(x) for x in input().split(":")]

    if(m%10==0):
        print("0")
        continue
    
    #X9 Min = math.ceil(m/10)*10-1 #the -1 is to account for secconds.
    #total mins = (X9 - m) *60
    #total secs = 60-s
    print(str(((math.ceil(m/10)*10-1)-m*60 + 60-s))

    
    
