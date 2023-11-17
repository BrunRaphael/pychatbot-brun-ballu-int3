import os
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

#Seperating Nomination from the "names.txt"
def isolement1(files_names):
    full_name = []
    for file_name in files_names:
        parts = file_name.split("_")
        full_name.extend(parts)
    return full_name

files_names = list_of_files(directory, "txt")
full_name = isolement1(files_names)
print(full_name)

#Getting only the names in a string
all_names = []
for j in range(len(full_name)):
    if j % 2 != 0:
        all_names.append(full_name[j])
print(all_names)

# Separating the names and ".txt"
def isolement2(files_names):
    all_names2 = []
    for file_name in files_names:
        parts2 = file_name.split(".txt")[0]
        all_names2.append(parts2)
    return all_names2

directory = "./speeches"
files_names = ['Chirac1.txt', 'Chirac2.txt', 'Giscard dEstaing.txt', 'Hollande.txt', 'Macron.txt', 'Mitterrand1.txt', 'Mitterrand2.txt', 'Sarkozy.txt']
all_names2 = isolement2(files_names)
print(all_names2)

for i in range(len(all_names2)):
    if  =< 9

