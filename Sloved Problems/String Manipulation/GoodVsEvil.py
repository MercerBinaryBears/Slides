runs = int(input())
for run in range(runs):
    name = input()
    gs = name.lower().count("g")
    es = name.lower().count("e")

    if(gs > es):
        alignment = "GOOD"
    elif(gs < es):
        alignment = "EVIL"
    elif(gs == es):
        alignment = "NEITHER"
    print("{0} is {1}".format(name, alignment))
