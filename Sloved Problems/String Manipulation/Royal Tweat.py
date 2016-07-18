##count = 0
##for x in range(int(input())):
##    count += input().lower().count("@britishmonarchy")
##
##print("Total Tweets Containing @BritishMonarchy = " + str(count))

##One Line 
print("Total Tweets Containing @BritishMonarchy = " + str(sum(
    [input().lower().count("@britishmonarchy")
     for x in range(int(input()))]
    )))
