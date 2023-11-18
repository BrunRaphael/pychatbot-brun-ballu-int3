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

print(unique_all_names2)


