import sqlite3
import time
import re
start_time = time.time()

conn = sqlite3.connect('reddit.db')
WORD_RE = re.compile(r"[\w']+")


def countUniqueWords(comments):
    temp = set()
    for body in comments:
        for word in WORD_RE.findall(body.lower()):
            temp.add(word)
    return len(temp)

result = {}
prev = ""
temp = []
request = 'SELECT comments.subreddit_id, comments.body FROM comments ORDER BY comments.subreddit_id'
for ID, body in conn.execute(request):
    if ID != prev:
        result[prev] = countUniqueWords(temp)
        prev = ID
    else:
        temp.append(body)

for key in sorted(result, key=result.__getitem__, reverse=True)[:10]:
    print(key, result[key])

print("--- %s seconds ---" % (time.time() - start_time))
