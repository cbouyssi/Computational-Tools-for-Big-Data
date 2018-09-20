from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MostUsedWords(MRJob):
    # SORT_VALUES = True

    def steps(self):
        return [MRStep(mapper=self.mapper_first,
                        combiner=self.combiner_first,
                       reducer=self.reducer_first),
                MRStep(combiner=self.combiner_second,
                       reducer=self.reducer_second)
                ]

    def mapper_first(self, key, line):
        for word in line.split():
            yield re.sub('\W', '', word.lower()), 1

    def combiner_first(self, key, values):
        yield None, (key, sum(values))

    def reducer_first(self, key, values):
        number=0
        words = {}
        for k, v in values:
            number += int(v)
            words[k]=v

        for k,v in words.items():
            yield k, (float(v)/number)


    def combiner_second(self, key, values):
        yield key, sum(values)

    def reducer_second(self, key, values):
        k = sum(values)
        if k > 10**-2:
            yield key, k



if __name__ == '__main__':
    MostUsedWords.run()
