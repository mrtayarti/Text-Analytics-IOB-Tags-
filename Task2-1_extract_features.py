# This program is a part of assignment of CE807 Text Analytics
# Atiwat Onsuwan 1802514
import re
import os.path

# Create fucntion to read file and separate array member by space
def read_file(path):
    with open(path, "r") as file:
        return [re.split("\s+", line.rstrip('\n')) for line in file]

arr_data = (read_file('aij-wikiner-en-wp2'))

count = 0
new_arr = []
for i in arr_data:
    for x in range(len(i)):
            new_arr.append(arr_data[count][x])
    count+=1
    new_arr.append('')
result = []
del new_arr[0]
last_space = len(new_arr)-1
del new_arr[last_space]


print("Removing repeating spaces...")

# loop to remove the unnecessary space
c,wipe=0,100000
for clean in range(wipe):
    wipe=0
    c=0
    for i in new_arr:
        if new_arr[c] == '' and new_arr[c+1] == '':
            del new_arr[c]
            wipe+=1
        c+=1
    if wipe ==0:
        break
    else:
        print("Searching",wipe,"left")

#put word and iob tags into list splitting by pipe symbol
print("Splitting words and IOBs...")
for i in new_arr:
    result.append([x.strip() for x in i.split('|')])

arr_iob = []
print("Reformatting...") # reformat
for i in result:
    if i != ['']:
        store_str = str(i[0]) +" "+ str(i[2])
        arr_iob.append(store_str)
    else:
        arr_iob.append('')
del arr_iob[0]

#create a new file if not exist
if os.path.exists('wikiner.txt'):
    iob = open('wikiner.txt', 'w')
else:
    iob = open('wikiner.txt', 'x')
    iob = open('wikiner.txt', 'w')

y = ""
print("Adding into a new file...")
for i in arr_iob:
    y += "".join(i)
    y += "\n"

# write into new file for traning purpose
iob.write(y)
iob.close()
print("Done!")
