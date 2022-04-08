### Problem statement
We haven't had *good* Harry Potter material (main timeline) since 2011. This project aims to create new material while also creating comprehensive lists about things like characters and spells. It will also attempt to provide text summarization using Natural Language Processing.

### Source Data
The source data can be found in several locations. I just picked one: https://github.com/formcept/whiteboard/tree/master/nbviewer/notebooks/data/harrypotter
This repository contains one text file for each Harry Potter book. For ease of use I removed all of the commas pre-ingest, and then placed a comma at the end of each page so it could be read into a list one page at a time. Future analysis might include some reconfiguring like splitting rows by sentence rather than page, but I am planning to tokenize the words so I'm still playing with the best way to do that. 

### Data Exploration
After getting the data into a semi usable form, we have three columns. 'text' contains text contents of the page, 'book' contains the title of the book that page belongs to, and 'page' is the page number where that text is found. There are 4643 rows and 3 columns at this point in the analysis, and each column has the datatype 'object'.

<img src='https://github.com/steinruck/data603-sp22/blob/project_progress/project/initial_info.png?raw=true'>

You can see from the info that there are some null values in the page column but not in the others. This is because there are a few rows that have empty strings in text field that will need to be addressed in future cleaning. As I move forward I will find more data I can pull out, including identifying spells used on each page, which could then be grouped by book and so on. I also want to identify names mentioned in each book and their counts. 

A basic frequency distribution on the entire dataset shows that 'harry' is the most repeated word throughout the series, followed by 'said', 'ron', 'hermione' and 'dumbledore'. 
<img src='https://github.com/steinruck/data603-sp22/blob/project_progress/project/initial_fdist.png?raw=true'>

To see the exact counts, I've include the top 10 most repeated words as well as their counts:
<img src='https://github.com/steinruck/data603-sp22/blob/project_progress/project/initial_top_words.png?raw=true'>

## Solution
My goal is to explore the components that make up the Harry Potter novels in order to craft a new one. The majority of this will be Natural Language Processing based with some Machine Learning componets. The goal is not to make a *good* addition to the series. Just to make an addition. I'm leaning towards a neural network method of attack, but it mostly depends on  what I can accomplish in this time frame. My main goal is to attempt various methods to evaluate the results. I plan to include Word2Vec but not until I am able to better understand the data I am working with and have it in a format I can use. I want to prove that a machine could have written a better addition to the universe than *The Cursed Child*.
