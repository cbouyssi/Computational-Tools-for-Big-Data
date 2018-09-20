from mrjob.job import MRJob
from mrjob.step import MRStep
import sqlite3
import re



class getReddit(MRJob):

    def mapper_init(self):
        # make sqlite3 database available to mapper
        self.sqlite_conn = sqlite3.connect('reddit.db')
        self.counter = 0

    def mapper(self, _, line):
        request = 'SELECT comments.subreddit_id, comments.id, comments.parent_id FROM comments'

        for subreddit_id, comment_id, parent_id in self.sqlite_conn.execute(request):
            self.counter+=1
            #print(self.counter, "/53850000")
            if(self.counter > 53850000):
                break
            yield subreddit_id, [comment_id, parent_id]

    def reducer(self, key, values):
        yield key, [x for x in values]
