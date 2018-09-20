def parseGraph(myFile):
    f = open("graphe1.txt","a")
    k = 1
    with open(myFile) as eulerGraphs:
        next(eulerGraphs)
        for line in eulerGraphs:
            if line in ['\n', '\r\n']:                      #empty line ?
                f.close()                                   #current graph is over
                k+=1                                        #N° of the next graph to create
                f = open("graphe"+str(k)+".txt", "a")       #Create the new file
                next(eulerGraphs)                           #Skip the header line
            else:
                f.write(line)

        f.close()


parseGraph("eulerGraphs.txt")
