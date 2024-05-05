from util import readFromTXTFileAndGenerateArray
from functions import createOutputFile

v23_array_ = readFromTXTFileAndGenerateArray('/Users/efecini-plentific/Desktop/bip-0039:turkish.txt/do_not_change/final_v23.txt')
allseed_array_ = readFromTXTFileAndGenerateArray('/Users/efecini-plentific/Desktop/bip-0039:turkish.txt/HELPER_FILES/allseed.txt')

can_be_added = []

v23_array = []
allseed_array = []


for item in v23_array_:
  if len(item) > 3:
    v23_array.append(item[0:4])

for item in allseed_array_:
  if len(item) > 3:
    allseed_array.append(item[0:4])

print('--------------------START')
for item in v23_array:
  if item in allseed_array:
    print(item)
print('--------------------END')

#createOutputFile('can_be_added', can_be_added)

"""
for word in kaan_v3_array:
  if word not in final_array:
    print(word)

#print(final_array)
"""