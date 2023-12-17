import os
import string
import math
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#1 : The defs
#1.1 : The defs of the "Basic functions"

def list_of_files(directory, extension):

    files_names = []

    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)

    return files_names


# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)


#This seperates Nomination from the names of the presidents
def isolement1(files_names):

    full_name = []

    for file_name in files_names:
        parts = file_name.split("_")
        full_name.extend(parts)

    return full_name


#This seperates the .txt at the end to only keep the names of the presidents
def isolement2(files_names):

    all_names2 = []

    for file_name in files_names:
        parts2 = file_name.split(".txt")[0]
        all_names2.append(parts2)

    return all_names2

directory = "./speeches"
files_names = ['Chirac1.txt', 'Chirac2.txt', 'Giscard dEstaing.txt', 'Hollande.txt', 'Macron.txt', 'Mitterrand1.txt', 'Mitterrand2.txt', 'Sarkozy.txt']



'''#Call isolement1
full_name = isolement1(files_names)
unique_full_name = []
seen_names = set()
for name in full_name:
    name_without_12 = name.replace('1', '').replace('2', '')
    if '1' in name or '2' in name:
        if name_without_12 not in seen_names:
            unique_full_name.append(name_without_12)
            seen_names.add(name_without_12)
    else:
        unique_full_name.append(name)
#It prints the names with no duplicates and no 1 or 2 in the names for isolement 1
print(unique_full_name)'''



#Call isolement2
all_names2 = isolement2(files_names)

unique_all_names2 = []

seen_names2 = set()

for name in all_names2:
    name_without_12 = name.replace('1', '').replace('2', '')

    if '1' in name or '2' in name:
        if name_without_12 not in seen_names2:
            unique_all_names2.append(name_without_12)
            seen_names2.add(name_without_12)
    else:
        unique_all_names2.append(name)

#It prints the names with no duplicates and no 1 or 2 in the names for isolement 2
print(unique_all_names2)



#This convertes every letter to lower case from the speeches
def convert_to_lowercase(file_path, output_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(content)



#It applys the conversion to lowercase on a random dictionnary
def process_files(directory, output_directory):

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path) and filename.endswith(".txt"):
            output_path = os.path.join(output_directory, filename)
            clean_text(file_path, output_path)



#This removes the punctuation and handling special characters
def clean_text(input_path, output_path):

    content = ""  # Initialize content before try block

    try:

        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()
        #It removes punctuation and handle special characters
        translator = str.maketrans('', '', string.punctuation)
        content = content.translate(translator)
        #It replaces special characters with spaces
        content = content.replace('’', ' ')  # apostrophe
        content = content.replace('-', ' ')  # dash
        content = content.replace('—', ' ')  # em dash
        content = content.replace('“', ' ')  # opening double quote
        content = content.replace('”', ' ')  # closing double quote

    except Exception as e:
        print(f"Error processing file: {input_path}")
        print(e)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(content)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#1.2 : The defs of the "Features to be developed"


#This calculates number of times a word appears in one .txt
def term_frequency(doc):

    word_count = {}

    words = doc.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


#This calculates the TF using the word count of the previous def
def calculate_term_frequency(corpus_directory):

    term_frequency_scores = Counter()


    for filename in os.listdir(corpus_directory):
        file_path = os.path.join(corpus_directory, filename)

        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                term_frequency_scores.update(term_frequency(content))

    return term_frequency_scores



#This calculates the IDF using the word count
def inverse_document_frequency(corpus_directory):

    document_count = 0

    word_document_count = Counter()

    for filename in os.listdir(corpus_directory):
        file_path = os.path.join(corpus_directory, filename)

        if os.path.isfile(file_path) and filename.endswith(".txt"):
            document_count += 1

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                words = set(content.split())
                word_document_count.update(words)

    idf_scores = {word: math.log(document_count / (1 + count)) for word, count in word_document_count.items()}

    return idf_scores



#This calculates and creates a matrix with the number count associated to the Asccicode of said character
def tf_idf_matrix(corpus_directory, term_frequency_scores):

    idf_scores = inverse_document_frequency(corpus_directory)

    tfidf_matrix = []

    unique_words = list(term_frequency_scores.keys())

    for filename in os.listdir(corpus_directory):
        file_path = os.path.join(corpus_directory, filename)

        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                tf_scores = term_frequency(content)
                tfidf_vector = [tf_scores.get(word, 0) * idf_scores.get(word, 0) for word in unique_words]
                tfidf_matrix.append(tfidf_vector)

    return tfidf_matrix, unique_words



#This creates a list with all the word with the biggest IDF and prints it at the end
def display_least_important_words(tfidf_matrix, unique_words):

    if not tfidf_matrix or not unique_words:
        print("TF-IDF matrix or unique words list is empty.")
        return

    least_important_words = []

    num_rows = len(tfidf_matrix)

    for idx, word in enumerate(unique_words):
        try:
            valid_rows = [
                row[idx] == 0
                for row in tfidf_matrix
                if row is not None and 0 <= idx < len(row)
            ]
            #This checks if there is no errors encountered with the index or the type

            if len(valid_rows) == num_rows and all(valid_rows):
                least_important_words.append(word)


        except (IndexError, TypeError) as e:
            #This prints the error for debugging purposes
            print(f"Error occurred for word '{word}' at index {idx}: {e}")
            pass  #This lets us keep going to the next word

    print("Least Important Words:")
    print(least_important_words)



#This prints the word with the biggest TF-IDF score and prints it at the end
def display_highest_tfidf_word(tfidf_matrix, unique_words):

    if not tfidf_matrix or not unique_words:
        print("TF-IDF matrix or unique words list is empty.")
        return

    max_tfidf_word = None

    max_tfidf_score = 0

    for idx, word in enumerate(unique_words):
        try:
            max_score = max(row[idx] for row in tfidf_matrix)

            if max_score > max_tfidf_score:

                max_tfidf_word = word

                max_tfidf_score = max_score

        except IndexError:
            #This prints the error for debugging purposes
            print(f"IndexError occurred for word '{word}' at index {idx}")

    if max_tfidf_word is not None:

        print(f"Word with the Highest TF-IDF Score: {max_tfidf_word}, Score: {max_tfidf_score}")

    else:

        print("No words found in the TF-IDF matrix.")


#This prints the word with the biggest TF in the .txt of Chirac's speeches because there are 2 difrent speeches
def most_repeated_word_by_chirac(tfidf_matrix, unique_words, president_name, corpus_directory):

    president_indices = [i for i, filename in enumerate(os.listdir(corpus_directory)) if president_name in filename]

    if not president_indices:

        #This prints the error for debugging purposes
        print(f"No files found for {president_name}.")
        return

    president_tfidf_matrix = [tfidf_matrix[i] for i in president_indices]

    if not president_tfidf_matrix or not unique_words:
        #This prints the error for debugging purposes in case of problem to calculate the TF
        print(f"TF-IDF matrix or unique words list is empty for {president_name}.")
        return

    most_repeated_word_index = None

    most_repeated_word_score = 0

    for idx, word in enumerate(unique_words):

        try:
            max_score = max(row[idx] for row in president_tfidf_matrix if 0 <= idx < len(row))
            if max_score > most_repeated_word_score:

                most_repeated_word_index = idx

                most_repeated_word_score = max_score

        except ValueError:

            #This prints the error for debugging purposes
            print(f"ValueError occurred for word '{word}' at index {idx}")

    if most_repeated_word_index is not None:
        most_repeated_word = unique_words[most_repeated_word_index]
        print(f"Most Repeated Word by {president_name}: {most_repeated_word}")

    else:
        #This prints the error for debugging purposes
        print(f"No words found in the TF-IDF matrix for {president_name}.")




#This calculates and prints the name of the presidant who said the most "Nation" according to the TF
def most_repeat_nation(tfidf_matrix, unique_words, corpus_directory):

    term_frequency_scores = calculate_term_frequency(corpus_directory)

    nation_indices = [i for i, word in enumerate(unique_words) if "nation" in word.lower()]

    if not nation_indices:
        #This prints the error for debugging purposes
        print("Word 'nation' not found in the list.")
        return

    president_mentions = {}

    for i, row in enumerate(tfidf_matrix):
        try:
            mentions = row[nation_indices[0]]  #It uses the first index if there are multiple variations like lowercase of uppercase
            president_name = os.listdir(corpus_directory)[i].split("_")[1].split(".")[0]

            if president_name not in president_mentions:
                president_mentions[president_name] = 0
            president_mentions[president_name] += mentions

        except IndexError:
            #This prints the error for debugging purposes in case of an IndexError
            print(f"IndexError occurred for row {i}")
    if not president_mentions:
        #This prints the error for debugging purposes
        print("No mentions of 'Nation' found in the TF-IDF matrix.")
        return

    most_mentions_president = max(president_mentions, key=president_mentions.get)
    most_mentions = president_mentions[most_mentions_president]
    print(f"President(s) who spoke about 'Nation': {', '.join(os.listdir(corpus_directory))}")
    print(f"President with the most mentions of 'Nation': {most_mentions_president}, Mentions: {most_mentions}")


#This prints the name of the first president to say the words "climat" or "écologie"
def first_president_to_talk_about_climate(tfidf_matrix, unique_words):

    climate_indices = [i for i, word in enumerate(unique_words) if "climat" in word.lower()]

    if not climate_indices:
        #This prints the error for debugging purposes
        print("Word 'climat' not found in the list.")
        return

    first_mention_index = None

    first_mention_score = float('inf')

    for i, row in enumerate(tfidf_matrix):
        try:
            mention_score = row[climate_indices[0]]

            president_name = os.listdir(corpus_directory)[i].split("_")[1].split(".")[0]

            if mention_score > 0 and mention_score < first_mention_score:

                first_mention_score = mention_score

                first_mention_index = i

        except IndexError:
            #This prints the error for debugging purposes in case of an IndexError
            print(f"IndexError occurred for row {i}")

    if first_mention_index is not None:

        first_mention_president = president_name
        print(f"First President to talk about 'Climat': {first_mention_president}")

    else:
        #This prints the error for debugging purposes
        print("No mentions of 'Climat' found in the TF-IDF matrix.")


#This creates a list with all the words that have been used in multiple .txt and to find it we use the list of unique words and substract it from the set of all words to have in the end the words used by multiple presidents
def words_mentioned_by_all_presidents(tfidf_matrix, unique_words, corpus_directory):

    president_count = len(os.listdir(corpus_directory))

    mentioned_by_all = []

    for word in unique_words:
        word_index = unique_words.index(word)

        if all(0 <= word_index < len(row) and row[word_index] > 0 for row in tfidf_matrix):

            mentioned_by_all.append(word)

    non_unique_words = set(unique_words) - set(mentioned_by_all)

    print("Words Mentioned by All Presidents:")
    print(non_unique_words)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2 : The calls of function
#2.1 : The call of the functions from "Basic Functions


#This apply the conversion to lowercase and the removal of special characters on "speeches" and creating the new dictonnary called "cleaned"
if __name__ == "__main__":
    main_directory = os.path.dirname(os.path.abspath(__file__))

    cleaned_directory = os.path.join(main_directory, "cleaned")

    process_files(cleaned_directory, cleaned_directory)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2.2 : The call of the functions from "Features to be developed"

if __name__ == "__main__":
    main_directory = os.path.dirname(os.path.abspath(__file__))

    cleaned_directory = os.path.join(main_directory, "cleaned")

    process_files(main_directory, cleaned_directory)  # Update the second argument with the correct output directory

    corpus_directory = cleaned_directory  # Use cleaned_directory as the corpus_directory

    term_frequency_scores = calculate_term_frequency(corpus_directory)

    tfidf_matrix, unique_words = tf_idf_matrix(corpus_directory, term_frequency_scores)

    display_least_important_words(tfidf_matrix, unique_words)

    display_highest_tfidf_word(tfidf_matrix, unique_words)

    most_repeated_word_by_chirac(tfidf_matrix, unique_words, "Chirac", corpus_directory)  # Provide the fourth argument

    most_repeated_word_by_chirac(tfidf_matrix, unique_words, "Hollande", corpus_directory)  # Provide a different fourth argument

    most_repeat_nation(tfidf_matrix, unique_words, corpus_directory)

    first_president_to_talk_about_climate(tfidf_matrix, unique_words)

    words_mentioned_by_all_presidents(tfidf_matrix, unique_words, corpus_directory)  # Provide the missing argument


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#PARTIE 2 DU PROJET



def chatbot_mode():

    while True:

        user_question = input("Ask a question (or type 'exit' to return to the main menu): ")

        if user_question.lower() == 'exit':
            print("Exiting Chatbot mode...")
            break

        # List containing the uncleaned .txt to use them later
        folder_path = "./speeches"

        # List of the names of the .txt
        list_file = os.listdir(folder_path)

        # Read the content of the .txt
        documents = []
        for file_name in list_file:
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                documents.append(content)

        # Create the TF-IDF Vector for the documents and the question
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents + [user_question])

        # Calculate the cosine similarity between the question and each document
        similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

        # Find the index of the document that is the most similar
        most_similar_index = similarities.argmax()

        # Show the name of the document that is the most similar
        most_similar_document_name = list_file[most_similar_index]
        print("Document le plus similaire :", most_similar_document_name)

        # Load the content the document that is the most similar
        most_similar_document_path = os.path.join(folder_path, most_similar_document_name)

        with open(most_similar_document_path, 'r', encoding='utf-8') as file:
            document_content = file.read()

        # Split the document into sentences using simple punctuation-based tokenization
        document_sentences = [sentence.strip() for sentence in document_content.split('.') if sentence.strip()]

        # Create TF-IDF vector for sentences in the document and the question
        vectorizer_s = TfidfVectorizer()
        tfidf_matrix_s = vectorizer_s.fit_transform(document_sentences + [user_question])

        # Calculate cosine similarity between the question and each sentence
        similarities_s = cosine_similarity(tfidf_matrix_s[-1], tfidf_matrix_s[:-1])

        # Find the index of the most similar sentence
        most_similar_sentence_index = similarities_s.argmax()

        # Display the TF-IDF and the most similar sentence
        most_similar_sentence = document_sentences[most_similar_sentence_index]

        # Add prefixes based on the question
        if "Comment" in user_question:
            response = "Après analyse, " + most_similar_sentence
        elif "Pourquoi" in user_question:
            response = "Car " + most_similar_sentence
        elif "Peux-tu" in user_question:
            response = "Oui, bien sûr ! " + most_similar_sentence
        else:
            response = "Car " + most_similar_sentence

        # Display the response
        print(response)


# Add this line at the end of the program to start execution
if __name__ == "__main__":
    corpus_directory = os.path.abspath("./cleaned")  # Update the directory to point to the correct path
    directory = "./cleaned"  # Update the directory to point to the correct path
    file_names = list_of_files(directory, "txt")
    print("File Names:", file_names)

    tfidf_matrix, unique_words = tf_idf_matrix(corpus_directory, term_frequency_scores)

    while True:
        print("\nMenu:")
        print("1. Access Part I functionalities")
        print("2. Access Chatbot mode")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            # Implement Part I functionalities
            print("Accessing Part I functionalities...")
            # Call your Part I functions here

        elif choice == "2":
            # Implement Chatbot mode
            print("Entering Chatbot mode...")
            # Call your Chatbot functions here
            chatbot_mode()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
