import json
import os
import time
import math
from collections import Counter
import numpy as np
from sklearn.ensemble import RandomForestClassifier

start_time = time.time()
count = 0
words = set()
def bagOfWords(body, bagOfWords):
    for word in body.lower().split() :
        bagOfWords.add(word)
    return bagOfWords

#FIRST STEP: Construct our list of unique words

for root, dirs, filenames in os.walk("C:/Users/César Bouyssi/Documents/DTU/CTBD/new/data/full/"):
    for filename in filenames:
        with open("C:/Users/César Bouyssi/Documents/DTU/CTBD/new/data/full/"+filename) as json_data:
            data = json.load(json_data)
            for article in data:
                if "topics" in article and "body" in article:
                    count+=1
                    words = bagOfWords(article["body"], words)

bag_of_words = np.zeros((count,len(words)), dtype = np.int)
result=np.zeros(count, dtype = np.int)


#SECOND STEP: Construct the bag of words
i=0
for root, dirs, filenames in os.walk("C:/Users/César Bouyssi/Documents/DTU/CTBD/new/data/full/"):
    for filename in filenames:
        with open("C:/Users/César Bouyssi/Documents/DTU/CTBD/new/data/full/"+filename) as json_data:
            data = json.load(json_data)
            for article in data:
                if "topics" in article and "body" in article:
                    currentWords = article["body"].lower().split()
                    counter = Counter(currentWords)
                    row = [counter.get(word, 0) for word in words]
                    bag_of_words[i] = row
                    if "earn" in article["topics"]:
                        result[i] = 1                                           #earn is in the topics list
                    else:
                        result[i] = 0                                           #earn is NOT in the topics list
                    i+=1

print(bag_of_words.shape)                                                       #should be : (nb_article, nb_unique_words)

print("--- Random Forest Classifier ---")


#Training the random forest
clf = RandomForestClassifier(n_estimators=50)
clf = clf.fit(bag_of_words[:math.floor(0.8*bag_of_words.shape[0])], result[:math.floor(0.8*len(result))])

#Testing the random forest
print(clf.score(bag_of_words[math.floor(0.8*bag_of_words.shape[0]):], result[math.floor(0.8*len(result)):]))






print("--- %s seconds ---" % (time.time() - start_time))
