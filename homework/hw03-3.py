# save file on run

# import modules
from mrjob.job import MRJob
import statistics

# create class for the job
class yelpCoolAvgRate(MRJob):
    
    # mapper function
    def mapper(self, _, line):
        (cols) = line.split(',') # reads the csv, splits at the comma
        if (cols[7] != 0) & (cols[3] != 'stars'): # col[7] = 'cool'. col[3] = 'stars' 
            # if 'cool' isn't 0 and 'stars' doesn't say 'stars'
            yield "'Cool' Average Rating:", int(cols[3]) # return those rows as integer

    # reducer function
    def reducer(self, key, star):
        yield key, statistics.mean(star) # get mean of stars for cool
        
if __name__ == '__main__':
    yelpCoolAvgRate.run()
