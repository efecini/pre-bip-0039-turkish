from util import readFromTXTFileAndGenerateArray

v23_array_ = readFromTXTFileAndGenerateArray('/Users/efecini-plentific/Desktop/bip-0039:turkish.txt/do_not_change/final_v23.txt')
print('--------------------START')
for item in v23_array_:
  if len(item) < 3 or len(item) > 8 :
    print(item)
print('--------------------END')
