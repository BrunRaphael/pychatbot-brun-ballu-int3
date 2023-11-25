import os
import string
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

#Seperating Nomination from the names of the presidents
def isolement1(files_names):
    full_name = []
    for file_name in files_names:
        parts = file_name.split("_")
        full_name.extend(parts)
    return full_name

#Seperating the .txt at the end to only keep the names of the presidents
def isolement2(files_names):
    all_names2 = []
    for file_name in files_names:
        parts2 = file_name.split(".txt")[0]
        all_names2.append(parts2)
    return all_names2

directory = "./speeches"
files_names = ['Chirac1.txt', 'Chirac2.txt', 'Giscard dEstaing.txt', 'Hollande.txt', 'Macron.txt', 'Mitterrand1.txt', 'Mitterrand2.txt', 'Sarkozy.txt']

# Using isolement1
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
#Printing the names with no duplicates and no 1 or 2 in the names for isolement 1
print(unique_full_name)

# Using isolement2
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
#Printing the names with no duplicates and no 1 or 2 in the names for isolement 2
print(unique_all_names2)

#Conveeting every letter to lower case from the speeches
def convert_to_lowercase(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(content)

#Apply the conversion to lowercase on a random dictionnary
def process_files(directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            output_path = os.path.join(output_directory, filename)
            clean_text(file_path, output_path)

#Removing the punctuation and handling special characters
def clean_text(input_path, output_path):
    content = ""  # Initialize content before try block
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()
        # Remove punctuation and handle special characters
        translator = str.maketrans('', '', string.punctuation)
        content = content.translate(translator)
        # Replace special characters with spaces
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

#Applying the conversion to lowercase and the removal of special characters on "speeches" and creating the new dictonnary called "cleaned"
if __name__ == "__main__":
    main_directory = os.path.dirname(os.path.abspath(__file__))
    cleaned_directory = os.path.join(main_directory, "cleaned")
    process_files(cleaned_directory, cleaned_directory)