import json
import os
import time
import math
from collections import Counter
# from sklearn.feature_extraction import FeatureHasher                          #Uncomment if you want to use FeatureHasher module
import numpy as np
from sklearn.ensemble import RandomForestClassifier

start_time = time.time()

result = []
matrix = []
i=0

def hashFunc(body):
    row = [0] * 1000                                                            #Hundred of buckets
    for word in body.lower().split():
        token = hash(word)%1000
        row[token] += 1
    return row

#STEP ONE: Create the feature hasher
for root, dirs, filenames in os.walk("C:/Users/César Bouyssi/Documents/DTU/CTBD/new/data/full/"):
    for filename in filenames:
        with open("C:/Users/César Bouyssi/Documents/DTU/CTBD/new/data/full/"+filename) as json_data:
            data = json.load(json_data)
            for article in data:
                if "topics" in article and "body" in article:
                    matrix.append(hashFunc(article["body"]))                    #Comment if you want to use FeatureHasher module
                    # currentWords = article["body"].lower().split()            #Uncomment if you want to use FeatureHasher module
                    # counter = Counter(currentWords)
                    # Data.append(counter)
                    if "earn" in article["topics"]:
                        result.append(1)
                    else:
                        result.append(0)
                    i+=1



# h = FeatureHasher(n_features=1000)                                            #Uncomment if you want to use FeatureHasher module
# f = h.transform(Data)
# Data.clear()
# Data = f.toarray()

print("--- Random Forest Classifier ---")


#STEP TWO: Training the random forest
clf = RandomForestClassifier(n_estimators=50)
clf = clf.fit(matrix[:math.floor(0.8*len(matrix))], result[:math.floor(0.8*len(result))])

#STEP THREE: Testing the random forest
print(clf.score(matrix[math.floor(0.8*len(matrix)):], result[math.floor(0.8*len(result)):]))






print("--- %s seconds ---" % (time.time() - start_time))
