![image](https://user-images.githubusercontent.com/4869523/152448346-24012b92-318d-4ac5-83ff-599f381cc63d.png)

# Data 603: Platforms for Big Data Processing

Instructor: Andy Enkeboll

# Final Project Submission
## Natural Language Processing in Spark: A Textual Analysis of Harry Potter
### By Michaella Steinruck

## Project Description:
As a lifelong Harry Potter fan, I wanted to see what would happen if I applied my new skillset to my old friend. I specifically wanted to get a neural network to create new material, but I quickly realized that was outside the scope of this project. Instead, I used a SparkNLP pipeline to extract some information from the text data like document, sentence, and word metadata, SparkML to remove stop words and retrieve word frequency information and perform topic modeling, and Spark SQL to explore and analyze the transformed text. The goal was to gain as much information as I could about the text to see if the outcome supported the knowledge and biases I already had about the series. Some of these included the most mentioned characters being Harry, Ron, Hermione, Dumbledore and Voldemort, the strongest character relationships being between Harry and Ron, Harry and Hermione, and Ron and Hermione. I also expected to see topics generated such as horcrux, dementor, and important character names.

## Data Location:
The data consists of 7 .txt files, each one containing one of the Harry Potter books. I've linked it here rather than uploading due to the nature of the data. 
https://github.com/formcept/whiteboard/tree/master/nbviewer/notebooks/data/harrypotter

## Github Contents
- `presentation.pdf`: final presentation given in class describing the goal of the project, what was accomplished, how it was accomplished, and future considerations.
- `preprocessing.ipynb`: Jupyter Notebooks that reads in each of the books, removes some page tagging, creates dataframe with content under `text` column, adds `titles` column, performs regex text cleaning, and exports to .csv
- `books_6_rows.csv`: .csv file containing each of the books in its own row in the `text` column, and a `titles` column
- `final.ipynb`: Jupyter Notebook containing all of the text analysis using Spark
- `README.md`: This document, describing the contents of the direcotry and the project
- `RUBRIC.md`: Evaluation metrics for the project
- `proposal.pdf`: Initial project proposal
- `progress.md`: Progress report for the project
- `initial_fdist.png`, `initial_info.png`, `initial_top_words.png`: Images used in progress report

## Running the Code
**Project Was Completed in Google Colab**
- preprocessing.ipynb:
  - if you would like to run the preprocssing, change any of the regex, etc, simply change the file paths saved in the list called `path_list` to the location of your .txt files. To export the new datframe to csv, change the path to your desired output location. 
- final_sparknlp.ipynb:
  - This notebook is set up to use the Google Colab environment. If not mounting to your Drive, comment out or delete the first cell. 
  - The second cell runs the Spark NLP setup.sh script from John Snow Labs. It us run every time the runtime starts.
  - All imports are at the top of the notebook
  - Change the filepath to load `books_6_rows.csv` from wherever you have it stored

## Potential Issues
I did have some issues with RAM trying to run pretrained models using SparkNLP. If you have a compatible host environment, there is potential for more modeling. The requirements listed by John Snow Labs are extensive and complicated. I'm not sure if it's just on my end, but it takes a not insignificant amount of time to run the complete notebook.

## Conclusion
While I did encounter some issues with RAM and execution time, the code runs without issues in the Colab environment. I would like to experiment with different data handling methods to see if I can decrease execution time, but for now having a working product will suffice. I managed to confirm some of my expectations about what I would find. Harry, Ron, Hermione and Dumbledore were the most mentioned characters. Depending on the book, Voldemort wasn't mentioned very many times, but he was one of the highest ones in later books. Harry and Ron did have the strongest relationship as expected, followed by Harry and Hermione, then Hermione and Ron. If I had more time (it takes a while to get this information) I would like to be able to get a list of every character interaction ranked by number of occcurances. I would have to find a more efficient way to do that first. The topics were interesting. I tried a variety of values before just picking 35 topics with 10 topic words. Some of them are actually helpful:
- The Chamber of Secrets
  - [kwikspell, mason, patrick, stall, flowerpot, rooster, mandrake, mandrakes, yeti, roosters]    
- This one is even better for The Prisoner of Azkaban
  - [lupin, pettigrew, marge, dementors, scabbers, boggart, trelawney, buckbeak, firebolt, crookshanks]
- These look like pretty accurate descriptions of The Goblet of Fire
  - [champions, ludo, karkaroff, beauxbatons, roberts, bagman, horntail, tents, troy, omnioculars] 
  - [champions, ludo, karkaroff, beauxbatons, bulgarian, bagman, bertha, horntail, amos, roberts]
- The Order of the Phoenix - this one is a little harder. It looks like some extras were mixed in  
  - [umbridge, pettigrew, lupin, luna, sirius, tonks, marge, ern, firebolt, dementors]
  - [umbridge, kreacher, tonks, luna, inquisitor, bellatrix, sirius, clipboard, grawp, prophecy]
- The Half Blood Prince
  - [slughorn, mclaggen, morfin, merope, horcrux, felix, hokey, felicis, demelza, romilda] 
- The Deathly Hallows
  - [hallows, xenophilius, horcrux, ariana, diadem, greyback, grindelwald, yaxley, aberforth, travers]

There were other topics mixed in that seemed more generic, but out of the 20 I displayed I was able to determine some topic words for all but one of the books. Overall I'd say there was some success here. At some point I had to cut myself off because the more things I found the more ideas I had to try. I will most likely be updating this in the future as I find time to do more. 
  
