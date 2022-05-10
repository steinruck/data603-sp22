![image](https://user-images.githubusercontent.com/4869523/152448346-24012b92-318d-4ac5-83ff-599f381cc63d.png)

# Data 603: Platforms for Big Data Processing

Instructor: Andy Enkeboll

# Final Project Submission
## Natural Language Processing in Spark: A Textual Analysis of Harry Potter
### By Michaella Steinruck

## Project Description:

## Data Location:
The data consists of 7 .txt files, each one containing one of the Harry Potter books. I've linked it here rather than uploading due to the nature of the data. 
https://github.com/formcept/whiteboard/tree/master/nbviewer/notebooks/data/harrypotter

## Github Contents
- presentation.pdf: final presentation given in class describing the goal of the project, what was accomplished, how it was accomplished, and future considerations.
- preprocessing.ipynb: Jupyter Notebooks that reads in each of the books, removes some page tagging, creates dataframe with content under `text` column, adds `titles` column, performs regex text cleaning, and exports to .csv
- books_6_rows.csv: .csv file containing each of the books in its own row in the `text` column, and a `titles` column
- 

## Running the Code
**Project Was Completed in Google Colab**
- preprocessing.ipynb:
  - if you would like to run the preprocssing, change any of the regex, etc, simply change the file paths saved in the list called `path_list` to the location of your .txt files. To export the new datframe to csv, change the path to your desired output location. 
- 
