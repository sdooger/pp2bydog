#TSIS 6 Files and Directories

#ex1
import os  

def directory(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def file(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def all(path):
    all_entries = os.listdir(path)
    return all_entries

path = '>>>directory'

directories = directory(path)
print("Directories:")
for i in directories:
    print(i)

files = file(path)
print("\nFiles:")
for j in files:
    print(file)

all_entries = all(path)
print("\nAll:")
for k in all_entries:
    print(k)


#ex2
import os

def check_access(path):
    access_info = {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }
    return access_info

path = 'aidoos/c'

access_info = check_access(path)

print(f"Path '{path}':")
print(f"Exists: {access_info['exists']}")
print(f"Readable: {access_info['readable']}")
print(f"Writable: {access_info['writable']}")
print(f"Executable: {access_info['executable']}")


#ex3
import os

def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return (True, filename, directory)
    else:
        return (False, None, None)

path = '>>>file_or_directory'

exists, filename, directory = path_info(path)

if exists:
    print(f"Path '{path}' exists.")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
else:
    print(f"Path '{path}' does not exist.")


#ex4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

file_path = '>>>text_file.txt'

line_count = count_lines(file_path)

print(f"Number of lines in '{file_path}': {line_count}")


#ex5
def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

file_path = '>>>output_file.txt'

my_list = ['apple', 'banana', 'cherry', 'date']

write_list_to_file(file_path, my_list)

print(f">>>'{file_path}'")


#ex6
import string

for letter in string.ascii_uppercase:
    file_name = f"{letter}.txt"
    with open(file_name, 'w') as file:
        file.write(f"This is file {file_name}\n")


#ex7
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
        for line in source:
            destination.write(line)

source_file_path = '>>>source_file.txt'
destination_file_path = '>>>destination_file.txt'

copy_file(source_file_path, destination_file_path)

print(f" '{source_file_path}' copy to '{destination_file_path}'")


#ex8
import os

def check_access(path):
    return os.path.exists(path) and os.access(path, os.F_OK)

def delete_file(path):
    if check_access(path):
        os.remove(path)
        print(f"File '{path}' udalen.")
    else:
        print(f"File '{path}' netu.")

file_path = '>>>file_to_delete.txt'

delete_file(file_path)

