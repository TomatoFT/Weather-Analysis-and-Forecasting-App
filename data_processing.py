from crawl_data import Data_Processing
import time
import os
start = time.time()
filelist = os.listdir('dataset')
# print(filelist)
c = 0
for file in filelist:
    filelist[c] = 'dataset/' + file
    c+=1
print(filelist)
filelist = sorted(filelist, key=os.path.getctime)
agent = Data_Processing(days=1427, place='hai-chau', list_file=filelist)
print('processing stage')
agent.pre_processing()
print('merge stage')
agent.merge_data()
print('Time to proceess:', time.time() - start, 'seconds')