# save file on run 

# import modules
from mrjob.job import MRJob

# create class for the job
class yelpReviewCountByMonth(MRJob):

    # mapper function    
    def mapper(self, _, line):
        (cols) = line.split(',') # reads the csv, splits at the comma
        if (cols[1] != 'date'): # col[1] = date. if contents is not 'date'
            date = ("-".join(cols[1].split("-")[:2])) # split at '-', keep 2 parts, join back
            yield date, 1 # return 1 for each date

     # reducer function
    def reducer(self, date, count):
        yield date, sum(count) # add each occurence of date. Return list of dates and counts

if __name__ == '__main__':
    yelpReviewCountByMonth.run()
