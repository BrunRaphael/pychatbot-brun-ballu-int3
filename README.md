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

#How the program works : 1-Open the file named "main.py". 2-Execute the program. 3-Finished!
