#In IDLE press Ctrl + D to end the input
import sys
print("Smiley Count = " + str(sum([sys.stdin.read().lower().count(":-)")])))
