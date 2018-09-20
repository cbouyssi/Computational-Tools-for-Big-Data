from  mrjob.job import MRJob
import re

class wordCount(MRJob):

	def mapper(self, key, line):
		for word in line.split():
			word = re.sub('\W','',word.lower())
			yield word, 1

	def reducer(self, key, values):
		yield key, sum(values)

if __name__ == '__main__':
	wordCount.run()
