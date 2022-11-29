import os
path = ['dataset/'+ file for file in os.listdir('dataset')]
print([pa[28:36] for pa in path])
hcm, dn = [], []
for file in path:
    if file[28:36] == 'tan-binh':
        hcm.append(file)
    else:
        dn.append(file)
print(len(hcm))
print(len(dn))

for file in hcm:
    os.rename(file, 'datasetHCM/'+file)
for file in dn:
    os.rename(file, 'datasetDN/'+file)