from mrjob.job import MRJob
from mrjob.step import MRStep

class graphTester(MRJob):

    def steps(self):
        return [
            MRStep(mapper = self.mapper_get_nodes,
                reducer = self.reducer_get_deg),
            MRStep(mapper = self.mapper_group_deg,
                reducer = self.reducer_is_eulerian)
    ]

    def mapper_get_nodes(self, key, line):
        for node in line.split():
            yield node,1


    def reducer_get_deg(self, key, values):
        yield key, sum(values)

    def mapper_group_deg(self, key, values):
        yield values, 1

    def reducer_is_eulerian(self, key, values):
         yield key, sum(values)



if __name__ == '__main__':
    graphTester.run()
