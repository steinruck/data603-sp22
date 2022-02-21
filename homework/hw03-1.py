from mrjob.job import MRJob
import statistics

class yelpReviewAvgWC(MRJob):
    
    def mapper(self, _, line):
        (cols) = line.split(',')
        count = 0
        if (cols[4] != 'text'):
            for word in cols[4].split(' '):
                for i in word:
                    count += 1
            yield "average_count", count
        
    def reducer(self, key, avg_count):
        yield key, statistics.mean(avg_count)
    
if __name__ == '__main__':
    yelpReviewAvgWC.run()
