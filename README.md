# pychatbot-brun-ballu-int3
#The name of the group members : BRUN Raphael , BALLU Noé

#Link of the repository : https://github.com/BrunRaphael/pychatbot-brun-ballu-int3.git

Basic functions
In order to analyze the contents of these files, we first ask you to develop the following functions: 
- Extract the names of the presidents from the names of the text files provided ;
- Associate a first name with each president;
- Display the list of president's names (watch out for duplicates) ; 
- Convert the texts in the 8 files to lower case and store the contents in new files. The new files are to be stored in a new folder called "cleaned". This folder should be located in the main directory of the main.py program, and at the same level as the "speeches" directory.
- For each file stored in the "cleaned" directory, run through its text and remove any punctuation characters. 
The final result should be a file with words separated by spaces. Please note that some characters, such as the apostrophe (') or the dash (-), requires special treatment to avoid concatenating two words (e.g. "ellemême" should become "elle même" and not "ellemême"). Changes made at this phase should be stored in the same files in the "cleaned" directory.

Features to be developed 
Based on the above functions, write programs that allow you to : 
1. Display the list of least important words in the document corpus. A word is said to be unimportant if its TD-IDF = 0 in all files. 
2. Display the word(s) with the highest TD-IDF score
3. Indicate the most repeated word(s) by President Chirac
4. Indicate the name(s) of the president(s) who spoke of the "Nation" and the one who repeated it the most times.
5. Identify the first president to talk about climate (“climat”) and/or ecology (“écologie”)
6. Excepti the so-called "unimportant" words, which word(s) did all the president mention?

I. Question tokenization :
Tokenize the question into individual words in the same way as for the corpus documents. This involves 
dividing the question into words and removing punctuation, deleting capital letters, deleting any empty 
words and any additional processing carried out on the texts of the corpus documents. 
• Write a function that takes the text of the question as a parameter, and returns the list of words 
that make up the question.

II. Search for the question words in the Corpus :
• Write a function that identifies the terms in the question that are also present in the document 
corpus. Ignore terms absent from the corpus, as they will have no associated TF-IDF values. In other 
words, look for terms that form the intersection between the set of words in the corpus and the
set of words in the question.

III. Calculate the TF-IDF vector for the terms in question :
In this section, the TF-IDF matrix of the corpus must have N rows and M columns, where N = number of 
documents in the corpus (8 in our case) and M = number of words in the corpus (1681 in our case).

IV. Calculating similarity :
Now that the question vector has been generated, we need to find out which document in the corpus it is 
most similar to. To do this, we'll use cosine similarity. This is a measure used to evaluate how similar two 
vectors are in a vector space. In particular, it is often used in natural language processing to measure the 
similarity between two texts represented as vectors (for example, TF-IDF vectors).
Mathematically, cosine similarity measures the cosine of the angle between two vectors A and B in a 
multidimensional space. The smaller the angle, the higher the value of its cosine, and therefore the higher 
the similarity between the two vectors.

V. Calculating the most relevant document 
To find the most relevant document name, simply implement a function that takes as parameters the TFIDF matrix of the corpus, the TF-IDF vector of the question and the list of file names in the corpus. It must 
calculate the similarity of the question vector with each of the document vectors, then return the document 
name corresponding to the highest similarity value. 
At this level, the name of the file to be returned will be the one contained in the "./cleaned" directory, so 
we need to provide a function that supplies its equivalent in the "./speeches" directory.

VI. Generating a response
Generating an answer automatically is a complex process, involving the use of advanced methods for 
managing semantics in text. The aim here is to do it with the simplest of methods. Nevertheless, any 
improvement to the method described in this document is welcome, provided it does not call on predefined 
functions or word-processing modules. 
The method requested here is as follows: 
- In the TF-IDF vector of the question, locate the word with the highest TF-IDF score and return it.
- In the relevant document returned in step 5, locate the first occurrence of this word and return the 
sentence containing it as the answer. A sentence is defined here as the text surrounded by two ".

VII. Refine an answer 
To bring more soul to the generated response and remove its crude appearance, it is possible to make 
improvements, such as imposing a capital letter at the beginning of a sentence and a "." at the end. 
One suggestion is to set up responses according to the form of the question asked. To do this, create a 
dictionary of possible text forms, with associated model responses. This dictionary can also be enriched 
with polite formulas.

Main program
The final main program must have a menu offering the user two options: 
o Access Part I functionalities at the user's request 
o Access Chatbot mode, allowing the user to ask a question

#How the program works : 1-Open the file named "main.py". 2-Execute the program. 3-Finished!
