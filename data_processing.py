from crawl_data import Data_Processing
import time
start = time.time()
agent = Data_Processing(days=3)
# try: 
#     agent.crawl_data(start_from=[2021,12,20])
# except:
agent.crawl_data()
agent.pre_processing()
agent.merge_data()
print('Time to proceess:', time.time() - start, 'seconds')