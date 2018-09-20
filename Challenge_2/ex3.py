from ex3_mapReduce import getReddit
import queue
import time
start_time = time.time()
mr_job = getReddit(args=['dumbfile.txt'])

def getAverageDepth(tree):
    depth = 0
    numberOflastComment = 0
    q1 = queue.Queue()
    q2 = queue.Queue()
    for topComment in [ k for k in tree.keys() if k.startswith("t3")]:
        q1.put(topComment)
        q2.put(-1)
        while q1.empty() == False:
            tempComment = q1.get()
            tempDepth = q2.get()
            if tempComment in tree:
                for comment in tree[tempComment]:
                    q1.put(comment)
                    q2.put(tempDepth + 1)
            else:
                numberOflastComment += 1
                depth += tempDepth
    return depth / numberOflastComment



with mr_job.make_runner() as runner:
    runner.run()
    result = {}
    for line in runner.stream_output():
        tree = {}
        subredditID, comment = mr_job.parse_output_line(line)
        for tab in comment:
            if tab[1] in tree:
                tree[tab[1]].append(tab[0])
            else:
                tree[tab[1]] = []
                tree[tab[1]].append(tab[0])

        result[subredditID] = getAverageDepth(tree)

    for key in sorted(result, key=result.__getitem__, reverse=True)[:10]:
        print(key, result[key])
print("--- %s seconds ---" % (time.time() - start_time))
