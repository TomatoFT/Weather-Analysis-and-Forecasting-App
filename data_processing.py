from crawl_data import Data_Processing
import time
import os
start = time.time()
path = 'datasetHN/dataset'
filelist = os.listdir(path)
c = 0
for file in filelist:
    filelist[c] = path+ '/' + file
    c+=1
print(filelist)
filelist = sorted(filelist, key=os.path.getctime)
agent = Data_Processing(days=1, list_file=filelist)
# agent.crawl_data(start_from=[2022,11,29])
print('processing stage')
agent.pre_processing()
print('merge stage')
agent.merge_data()
print('Time to proceess:', time.time() - start, 'seconds')