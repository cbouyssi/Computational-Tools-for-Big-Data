from mrjob.job import MRJob
from mrjob.step import MRStep
import sqlite3
import re


class ReadReddit(MRJob):


    def mapper_init(self):
        self.sqlite_conn = sqlite3.connect('reddit.db')
        self.counter = 0


    def mapper(self, key, line):
        request = 'SELECT comments.subreddit_id, comments.author_id FROM comments'
        for sub_reddit_id, authors in self.sqlite_conn.execute(request):
            self.counter +=1
            # print(self.counter, "/53850000")
            if(self.counter > 53850000):
                break
            yield (sub_reddit_id, authors)

    def reducer(self, key, values):
        yield key, [x for x in values]


output = {}
counter = 0
mr_job = ReadReddit(args=['dumbfile.txt'])
with mr_job.make_runner() as runner:
    runner.run()
    for line in runner.stream_output():
        # counter +=1
        # print(counter, "/47172")
        key, value = mr_job.parse_output_line(line)
        output[key] = value




result = {}
minimum = []    #minimum = [key, result[key]]
counter_init = 0
while(1):
    if output == {}:
        break
    i = next(iter(output))
    current_list = set(output[i])
    del output[i]
    for j in output:
        if counter_init < 10:
            result[i + ' ' + j] = len(current_list.intersection(output[j]))
            min_key = min(result, key=result.get)
            minimum = [min_key, result[min_key]]
            counter_init +=1
        else:
            current_len = len(current_list.intersection(output[j]))
            if minimum[1] < current_len:
                del result[minimum[0]]
                result[i + ' ' + j] = current_len
                min_key = min(result, key=result.get)
                minimum = [min_key, result[min_key]]

print(result)






