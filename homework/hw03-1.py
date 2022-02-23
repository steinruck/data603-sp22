# save file on run 

# import modules
from mrjob.job import MRJob
import statistics

# create class for the job
class yelpReviewAvgWC(MRJob):
    
    # mapper function
    def mapper(self, _, line):
        (cols) = line.split(',') # reads the csv, splits at the comma
        count = 0 # set counter to 0
        if (cols[4] != 'text'): # col[4] = 'text' column. Skipping the row if string is 'text'
            for word in cols[4].split(): # splits string in each row at the space
                for i in word: # adds 1 to the counter for every word
                    count += 1
            yield "average_count", count # return the counter
            
    # reducer function
    def reducer(self, key, avg_count):
        yield key, statistics.mean(avg_count) # return the key and average using stats module

if __name__ == '__main__':
    yelpReviewAvgWC.run()
